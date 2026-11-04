# Revisión de manijadj.com y propuesta de mejora

Análisis de la web original ([manija10-star/manijadj-web](https://github.com/manija10-star/manijadj-web), versión "Primera versión de la web") y explicación de cada cambio del rediseño.

## 1. Lo que ya funcionaba bien (y se mantiene)

- **Identidad clara**: negro, blanco roto y un solo dorado; Montserrat fina con mucho espaciado; el lema en caligrafía. El rediseño no añade colores ni tipografías.
- **Portada con la cara visible**: nombre encima de la cabeza y lema debajo. Se respeta la misma foto, el mismo encuadre y el mismo orden.
- **Ligera y sin dependencias**: un solo `index.html` y fotos ya optimizadas. Se mantiene: sin frameworks, sin librerías y sin paso de compilación.
- **YouTube respetuoso con la privacidad**: `youtube-nocookie` y carga solo al pulsar play. Se mantiene.
- **Enlaces compartibles por sección** (`#sesiones`, `#booking`…). Siguen funcionando: ahora llevan a esa sección de la página.

## 2. Problemas encontrados

### Experiencia
1. **Todo estaba escondido en capas.** La portada era una pantalla fija y cada sección se abría encima. No había nada que recorrer con el scroll y quien no pulsaba el menú no veía sesiones, fotos ni fechas.
2. **En móvil no se podía saltar de una sección a otra.** El menú de las capas se ocultaba por debajo de 960 px, así que había que cerrar y volver a abrir desde la portada.
3. **Casi sin movimiento**: solo el fundido de las capas y un zoom al pasar el ratón por las fotos.
4. **Los vídeos se reproducían dentro de miniaturas pequeñas** (rejilla de 4 columnas), con un reproductor diminuto.
5. **El visor de fotos era muy básico**: sin anterior/siguiente, sin teclado ni gestos, sin botón de cerrar, sin pie de foto ni contador, y se abría de golpe.
6. **Las fechas no distinguían pasado y futuro.** A día de hoy (noviembre de 2026) todas las fechas de la lista ya han pasado y se mostraban igual que si fueran próximas, así que cada fecha había que moverla a mano.
7. **Tarea pendiente del README**: "Crush" en la portada no enlazaba a crushculture.es.

### Accesibilidad
8. Al abrir una capa, **el foco no entraba en ella** y el contenido de detrás seguía siendo navegable con el teclado.
9. **El visor no era un diálogo**: no se le podía dar foco ni recorrer con el teclado.
10. **Contraste insuficiente en textos pequeños**: `#5e5e5e` sobre `#0a0a0a` (~3:1) en las descripciones de las fechas. Para texto pequeño hace falta 4,5:1.
11. **"Reducir movimiento"** solo se tenía en cuenta para las capas.

### SEO
12. Casi todo el contenido estaba en capas ocultas (`visibility: hidden`) y la página no tenía datos estructurados.

## 3. Qué incluye el rediseño

### Estructura
- **Una sola página con scroll**: portada → el sonido → sesiones → fechas → galería → bio → booking → pie. La portada se queda fija y la siguiente sección se desliza por encima.
- **Barra de navegación** que aparece al dejar la portada, con la sección activa subrayada en dorado y una línea de progreso. En móvil hay menú a pantalla completa y un acceso directo a Booking.
- **Los mismos `#enlaces`** de antes: `manijadj.com/#booking` lleva directo a Booking, sin intro.

### Animaciones
| Elemento | Detalle |
|---|---|
| Intro | Letras que suben una a una, línea dorada que se dibuja y telón hacia arriba. Espera a que cargue la foto de portada (máximo 3,6 s). |
| Portada | Foto que se aleja al cargar, parallax con el ratón y con el scroll, lema "escrito a mano" con una máscara, menú escalonado. |
| Ondas de sonido | Canvas con líneas finas (una dorada) que fluyen sobre la foto, se agitan con el scroll y se curvan al pasar el ratón: "la música fluye". Se repiten en Booking. |
| Letras que reaccionan | Montserrat se carga como fuente variable: con el ratón cerca, las letras de MANIJA ganan grosor. Al terminar la intro pasa una ola de grosor por el nombre, también en móvil. |
| El sonido | La frase de la bio sobre cómo es un set se ilumina con el scroll y su grosor crece de 200 a 600 ("suaves" fino, "lo más alto" en dorado). Debajo, una forma de onda tipo software de DJ con cabezal y tiempo del set. |
| Marquee | Velocidad e inclinación según el scroll, y cambio de sentido al subir. |
| Títulos | Entran letra a letra desde una máscara. Las etiquetas dibujan su línea. |
| Fotos | Se descubren como un telón con un zoom de salida. |
| Vinilo | Sale de detrás del vídeo destacado. Gira con inercia: acelera y frena suavemente, a 33⅓ rpm mientras suena. Con ecualizador animado. |
| Galería | Tira horizontal fijada mientras se hace scroll, con tamaños y alturas variados, parallax interno, contador y barra de progreso. |
| Visor | Transición FLIP: la foto vuela desde su miniatura y vuelve a ella al cerrar. Deslizamiento entre fotos. |
| Booking | Palabra gigante en contorno en movimiento, email con subrayado animado y botones magnéticos. |
| Global | Grano de película, cursor propio ("Play"/"Ver") y fechas de residencia con pulso. |

### Funciones nuevas
- **Reproductor tipo cine** para las sesiones: grande, con el título, se cierra con `Esc` y para el vídeo al cerrar. Si suena el destacado y se abre otra sesión, el destacado se pausa.
- **Fechas automáticas**: se ordenan solas en "Próximas" y "Últimas fechas" según el día. Si no hay próximas, aparece "Próximas fechas en preparación".
- **Cifras automáticas**: el número de sesiones y las horas de música se calculan con las duraciones.
- **Copiar email** con un botón (y aviso para lectores de pantalla).
- **"Crush" enlazado** en la portada y en el pie (pendiente del README original).
- **Tarjeta de residencia** con foto de la cabina de Crush.
- Cierre de la galería con un enlace a Instagram.

### Accesibilidad
- Diálogos reales (`role="dialog"`, `aria-modal`): el foco entra y vuelve al botón de origen y el fondo queda inactivo (`inert`).
- Visor con flechas del teclado, botones anterior/siguiente, contador y pie de foto (el texto alternativo).
- Enlace "Saltar al contenido", foco visible en dorado y textos con contraste AA (el gris oscuro pasa de `#5e5e5e` a `#7a7a7a`).
- Títulos divididos en letras sin romper la lectura: el lector de pantalla lee el título entero.
- **Reducir movimiento**: sin intro, parallax, cursor ni galería horizontal, y todo se muestra quieto.
- **Sin JavaScript** se ve todo el contenido y, si el script fallara, a los 6 s se muestra todo igualmente.
- Auditoría con axe-core (WCAG 2.1 AA): sin incidencias, salvo las palabras de "El sonido" antes de iluminarse. Es el propio efecto: se iluminan al llegar a ellas y con "reducir movimiento" salen encendidas desde el principio.

### Rendimiento
- Un único bucle `requestAnimationFrame`. Las posiciones se miden al cargar o redimensionar, nunca en cada fotograma.
- Las ondas, el vinilo y la galería solo se calculan cuando están en pantalla, y la portada deja de pintarse al quedar tapada.
- La foto de portada se precarga y el resto de fotos y miniaturas se cargan en diferido.
- En móvil se ignoran los cambios de alto de la barra del navegador para evitar saltos.

### SEO
- Todo el contenido visible en una sola página, con títulos de sección reales.
- Datos estructurados JSON-LD (`MusicGroup`) con Instagram, YouTube y SoundCloud.
- Se mantienen el título, la descripción, Open Graph y la URL canónica originales. Se añaden `theme-color` y `og:locale`.

## 4. Pendiente (necesita material nuevo)
- Fotos de la próxima sesión de estudio: portada horizontal con aire sobre la cabeza y versión vertical para móvil (ver "Mantenimiento" en el README).
- `video/hero.mp4` opcional para la portada.
