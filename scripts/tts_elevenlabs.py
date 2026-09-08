#!/usr/bin/env python3
"""Genera el VO de El Espejo Bíblico con ElevenLabs.

Pensado para correr en la máquina de Yair: la API de ElevenLabs está
bloqueada desde el entorno remoto de Claude Code, así que este script
no se puede probar allí.

    export ELEVENLABS_API_KEY=...

    python3 tts_elevenlabs.py --voices              # tus voces, con su id
    python3 tts_elevenlabs.py --models              # modelos disponibles
    python3 tts_elevenlabs.py vo_largo.txt salida.mp3 --voice-id <ID>

Ajustes por defecto pensados para el tono del canal: narración reflexiva
y sostenida durante cinco minutos. Cámbialos con --stability, --similarity
y --style si tu oído pide otra cosa.
"""
import argparse, json, os, sys, urllib.request, urllib.error

API = "https://api.elevenlabs.io/v1"
LIMITE = 4500  # margen bajo el tope por petición de eleven_multilingual_v2


def _key():
    k = os.environ.get("ELEVENLABS_API_KEY")
    if not k:
        sys.exit("Falta ELEVENLABS_API_KEY en el entorno.")
    return k


def _pedir(path, cuerpo=None, binario=False):
    datos = json.dumps(cuerpo).encode() if cuerpo else None
    cab = {"xi-api-key": _key()}
    if cuerpo:
        cab["Content-Type"] = "application/json"
    req = urllib.request.Request(f"{API}/{path}", data=datos, headers=cab)
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            return (r.read(), r.headers.get("request-id")) if binario else json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code} en {path}: {e.read().decode()[:600]}")


def listar_voces():
    for v in _pedir("voices").get("voices", []):
        etiquetas = ", ".join(f"{k}={x}" for k, x in (v.get("labels") or {}).items())
        print(f"{v['voice_id']}  {v['name']:24} {etiquetas}")


def listar_modelos():
    for m in _pedir("models"):
        multi = "multilingüe" if m.get("can_do_text_to_speech") else ""
        print(f"{m['model_id']:34} {m.get('name','')}  {multi}")


def trocear(texto, limite=LIMITE):
    """Corta por párrafos, nunca a mitad de frase: un corte sucio se oye."""
    trozos, actual = [], ""
    for parrafo in texto.split("\n\n"):
        parrafo = parrafo.strip()
        if not parrafo:
            continue
        if len(actual) + len(parrafo) + 2 > limite and actual:
            trozos.append(actual)
            actual = parrafo
        else:
            actual = f"{actual}\n\n{parrafo}" if actual else parrafo
    if actual:
        trozos.append(actual)
    return trozos


def sintetizar(texto, voice_id, modelo, ajustes):
    """Encadena los trozos con previous_request_ids para que la prosodia
    no se reinicie en cada corte — sin esto, cada trozo suena a locutor
    distinto."""
    audio, previos = b"", []
    trozos = trocear(texto)
    for i, trozo in enumerate(trozos, 1):
        cuerpo = {"text": trozo, "model_id": modelo, "voice_settings": ajustes}
        if previos:
            cuerpo["previous_request_ids"] = previos[-3:]
        datos, rid = _pedir(f"text-to-speech/{voice_id}", cuerpo, binario=True)
        audio += datos
        if rid:
            previos.append(rid)
        print(f"  trozo {i}/{len(trozos)} — {len(trozo)} caracteres", file=sys.stderr)
    return audio


def main():
    p = argparse.ArgumentParser()
    p.add_argument("texto", nargs="?")
    p.add_argument("salida", nargs="?")
    p.add_argument("--voice-id")
    p.add_argument("--model", default="eleven_multilingual_v2")
    p.add_argument("--stability", type=float, default=0.75)
    p.add_argument("--similarity", type=float, default=0.75)
    p.add_argument("--style", type=float, default=0.0)
    p.add_argument("--no-speaker-boost", action="store_true")
    p.add_argument("--voices", action="store_true")
    p.add_argument("--models", action="store_true")
    a = p.parse_args()

    if a.voices:
        return listar_voces()
    if a.models:
        return listar_modelos()
    if not (a.texto and a.salida and a.voice_id):
        p.error("hacen falta el texto, la salida y --voice-id (mira --voices)")

    ajustes = {
        "stability": a.stability,
        "similarity_boost": a.similarity,
        "style": a.style,
        "use_speaker_boost": not a.no_speaker_boost,
    }
    audio = sintetizar(open(a.texto).read().strip(), a.voice_id, a.model, ajustes)
    with open(a.salida, "wb") as f:
        f.write(audio)
    print(f"{a.salida} — {len(audio)/1024:.0f} KB")


if __name__ == "__main__":
    main()
