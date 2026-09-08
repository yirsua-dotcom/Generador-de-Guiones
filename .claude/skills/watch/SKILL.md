---
name: watch
description: Radar de inteligencia de contenido para el canal de YouTube "El Espejo Bíblico" de Yair (psicología bíblica y sabiduría judía en español). Invócala cuando Yair escriba /watch o pida explícitamente un radar, un chequeo del canal, "qué está pasando en el nicho", "qué hace la competencia", "cómo van mis videos" o "qué parashá toca". Reúne cuatro módulos - temas en tendencia dentro del nicho, movimientos de canales competidores, lectura del rendimiento de sus videos publicados, y el calendario litúrgico judío de las próximas semanas - y los convierte en ideas de video accionables listas para pasar a la skill espejo-biblico-produccion. Es una skill de diagnóstico y planificación: NO escribe guiones, prompts de imagen ni paquetes SEO.
---

# /watch — Radar de contenido de El Espejo Bíblico

Esta skill responde una sola pregunta: **¿qué debería grabar Yair esta semana, y por qué?**

No produce contenido. Produce el diagnóstico que decide qué contenido producir. Cuando el radar termina y Yair elige una idea, el trabajo pasa a la skill `espejo-biblico-produccion`, que es la que escribe guion, prompts, SEO y VO.

---

## Cómo se invoca

| Invocación | Qué corre |
|---|---|
| `/watch` | Los cuatro módulos, informe completo |
| `/watch temas` | Solo módulo 1 — radar de temas |
| `/watch competencia` | Solo módulo 2 — canales del nicho |
| `/watch rendimiento` | Solo módulo 3 — cómo van sus videos |
| `/watch calendario` | Solo módulo 4 — parashá y festividades |

Si Yair invoca `/watch` a secas, corre los cuatro. Los módulos 1, 2 y 4 son autónomos (búsqueda web). El módulo 3 depende de datos que solo Yair tiene — ver abajo.

**Regla de fecha:** antes de cualquier módulo, confirma la fecha de hoy. Todo este radar es perecedero; un informe con fechas de hace un año es peor que ningún informe.

---

## Módulo 1 — Radar de temas

Busca qué se está moviendo **ahora** en el nicho del canal y tradúcelo a ideas de video, no a un resumen de noticias.

Barre estos frentes con búsqueda web:

1. **Parashá de la semana** — qué porción toca y qué tensión psicológica contiene (ver módulo 4 para la fecha exacta).
2. **Festividad o fecha judía cercana** — cualquier cosa en las próximas 3 semanas es material con demanda de búsqueda garantizada y previsible.
3. **Conversación viva** — qué se está discutiendo en el mundo judío e israelí que tenga lectura emocional o psicológica, no solo noticiosa.
4. **Emociones que buscan los hispanohablantes** — ansiedad, culpa, abandono, rechazo, ira, duda. Busca qué formulación concreta de esas búsquedas está creciendo ("cómo superar el rechazo", "por qué me siento vacío"), porque ese es el puente entre el nicho y la audiencia amplia.
5. **Series abiertas del canal** — El Espejo del Alma, Yeshua/Mashiaj (10 capítulos), Sabiduría Judía Aplicada, Israel: Historias Reales. Una serie a medias es la idea más barata y con mejor retención que existe: siempre revisa si el siguiente capítulo es la mejor jugada de la semana antes de proponer algo nuevo.

**Cómo entregar cada idea.** Una idea sin ángulo es ruido. Cada propuesta lleva:

- **Personaje o texto ancla** — el pasaje, sabio o figura concreta.
- **Emoción humana** — qué siente el espectador que la busca.
- **Gancho de 8 segundos** — la primera frase literal del video, ya escrita. Sin "hoy hablaremos de".
- **Por qué ahora** — la razón de calendario, tendencia o continuidad de serie. Si no hay razón de "ahora", la idea baja de prioridad.
- **Pilar y formato** — a qué serie pertenece y si va Short+Largo o solo Short.

Propón entre 3 y 5 ideas, ordenadas por prioridad, no una lista larga sin jerarquía.

**Precisión:** si una idea se apoya en un dato histórico, una cifra o una fecha, verifícalo antes de proponerlo. El canal ya tiene la regla de no publicar números sin comprobar, y el radar no es excepción.

**Framing:** todo lo que toque a Yeshúa o cristianismo se propone como *"así lo entiende la tradición judía"*, nunca como afirmación teológica absoluta. Lo geopolítico sobre Israel se propone con imparcialidad y reconociendo lecturas legítimas distintas. Esta regla aplica desde el radar, no solo desde el guion — una idea mal encuadrada arrastra el error hasta la publicación.

---

## Módulo 2 — Vigilar la competencia

Objetivo: encontrar **el hueco**, no copiar lo que ya existe.

Revisa los canales y frentes listados en `references/canales_a_vigilar.md`. Para cada uno mira qué publicaron en las últimas ~2 semanas y qué les está funcionando.

Lo que importa observar:

- **Ganchos y títulos** — la fórmula concreta que usan en los primeros segundos y en el título. Esto es lo más transferible.
- **Formato** — Short vs largo, duración real, si usan puente Short→Largo.
- **Temas saturados** — qué está haciendo todo el mundo esta semana. Saturado no significa prohibido: significa que solo entras si tienes un ángulo distinto.
- **Huecos** — qué emoción, personaje o texto nadie está tocando y encaja con los pilares del canal. Aquí está el valor real del módulo.

**Cómo entregarlo:** 3-4 observaciones concretas, cada una con su implicación para Yair. "El canal X publicó sobre Yosef" no sirve. "Tres canales cubrieron Yosef como historia de éxito y ninguno como historia de rechazo fraterno — ese es tu ángulo, y es exactamente tu pilar" sí sirve.

Nunca propongas copiar un video ajeno. El output es siempre un ángulo diferenciado.

---

## Módulo 3 — Rendimiento de sus videos

**Limitación que debes declarar de entrada, siempre:** no hay acceso automático a YouTube Analytics en esta skill. No inventes métricas, no estimes vistas, no supongas retención. Si no hay datos, el módulo no corre.

Al invocar este módulo, pide a Yair una de estas tres cosas:

1. **Export CSV de YouTube Studio** — Analytics → Avanzado → Exportar. Es la opción más completa y la preferida.
2. **Capturas de pantalla** de las pantallas de Analytics (Vistas, Retención de audiencia, CTR de miniaturas).
3. **Los números a mano** — para cada video: título, fecha, vistas, CTR, retención media, duración media vista.

Con los datos en mano, analiza contra las líneas base ya conocidas del canal:

- **Retención histórica ~30%**, con la caída más fuerte en los primeros 1-2 minutos.
- **CTR objetivo 4-5%+.**
- **Miniaturas de "pregunta directa"** rinden mejor que las descriptivas.

Y responde a estas preguntas, en este orden:

1. **¿Qué video superó su propia línea base y por qué?** Aísla la variable: ¿fue el tema, el gancho, la miniatura, el día de publicación?
2. **¿Dónde exactamente cae la retención?** Si el dato es por segundo, señala el timestamp. Un desplome a los 0:40 es un problema de gancho; a los 3:00 es un problema de re-hooks parejos.
3. **¿El puente Short→Largo está funcionando?** Compara las vistas del Short contra las del largo emparejado. Si el Short vuela y el largo no se mueve, el corte del "gancho cortado" está mal puesto.
4. **¿Qué pilar rinde mejor?** Esto debe alimentar la rotación de publicación, no quedarse como dato suelto.
5. **¿Qué comentarios se repiten?** Una pregunta repetida en comentarios es un video pedido por la audiencia — y es la idea con mejor tasa de acierto que existe.

**Cierre obligatorio del módulo:** una sola recomendación concreta y accionable para el próximo video. No cinco. Una.

---

## Módulo 4 — Calendario litúrgico

Da a Yair el horizonte de producción, con margen suficiente para grabar a tiempo.

Verifica siempre con búsqueda web — el calendario es lunisolar y cambia cada año. Fuentes fiables: hebcal.com, chabad.org. Los datos guardados en `espejo-biblico-produccion/references/calendario_y_fechas_judias.md` solo sirven si la fecha de hoy cae dentro del rango ya verificado ahí; fuera de ese rango, vuelve a verificar.

Entrega:

- **Parashá de esta semana** — nombre, fecha del Shabat, y en una frase la tensión psicológica que contiene (que es el ángulo del canal, no el resumen del texto).
- **Parashá de la semana siguiente** — para que pueda adelantar producción.
- **Festividades en las próximas 4 semanas** — con fecha exacta y días de antelación con que debe estar listo el contenido.
- **Ventanas de silencio** — Shabat y festividades mayores son pausa de publicación, no descuido. Márcalas explícitamente en el plan.

**Regla de anticipación:** la Parashá Semanal se publica jueves o viernes, antes de que empiece Shabat. Si al correr el radar ya es miércoles, dilo de frente: la parashá de esta semana está en riesgo de tiempo y hay que decidir entre producirla hoy o saltar a la siguiente.

Para festividades mayores, avisa con 2-3 semanas de antelación — un video de Rosh Hashaná publicado el día de Rosh Hashaná llegó tarde.

---

## Formato del informe

Entrega el radar en el terminal, en este orden y sin relleno:

```
RADAR — [fecha de hoy]

⚡ LO PRIMERO
[La única decisión que importa esta semana, en dos frases.]

📅 CALENDARIO
[Parashá de la semana + fecha. Próxima festividad + días restantes.]

🎯 IDEAS (prioridad descendente)
1. [Título tentativo] — [pilar] — [formato]
   Ancla: … | Emoción: … | Por qué ahora: …
   Gancho: "…"
2. …

👀 COMPETENCIA
[3-4 observaciones con su implicación.]

📊 RENDIMIENTO
[Solo si Yair aportó datos. Si no: qué datos hacen falta.]

➡️ SIGUIENTE PASO
[Qué producir, y el recordatorio de que espejo-biblico-produccion lo escribe.]
```

Si el informe sale largo o Yair quiere conservarlo o compartirlo, ofrécele publicarlo como artifact — una línea, sin insistir.

---

## Límites de esta skill

- **No escribe guiones.** Llega hasta el gancho de 8 segundos y para. El guion completo es trabajo de `espejo-biblico-produccion`.
- **No genera prompts de imagen, SEO, miniaturas ni VO.** Mismo motivo.
- **No inventa métricas.** Sin datos de Yair, el módulo 3 declara que no puede correr.
- **No propone copiar** un video de otro canal. Siempre ángulo propio.
