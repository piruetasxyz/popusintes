# Configuración de kicad-visor (https://github.com/piruetasxyz/kicad-visor)
# para las placas de popusintes, que están como submódulos en placas/.
#
# kicad-visor busca todos los .kicad_pro bajo la raíz. Acá se excluyen los
# que no van en el sitio. Los patrones son relativos a la raíz, con "./"
# al principio, y "*" también calza con "/".

# Videos turntable: el estilo estándar de popusintes, el mismo que usa cada
# placa en .github/workflows/girar-placa.yml (mantener ambos iguales). Gira
# como un disco, vista desde arriba en ángulo, cuadrado de 1080x1080, fondo
# rosado, 6 s: 1 video por placa (kicad-visor por defecto hace 24).
#
# El tiempo de render depende de giros × formatos × segundos; los fondos
# casi no cuestan (solo se vuelve a codificar el video), así que agregar
# colores es barato y agregar giros o formatos es caro.
turntables = [("z", "ccw")]
aspects = {"square": (1080, 1080)}
backgrounds = {"pink": "#ff9ecf"}
turntable_seconds = 6

exclude = [
    # Los de siempre de kicad-visor.
    "**/*-backups/**",
    "**/.venv/**",
    "**/env/**",
    "**/node_modules/**",
    # Submódulos dentro de los submódulos, y plantillas.
    "**/terceros/**",
    "**/plantillas/**",
    # cuadra/hardware tiene por ahora una copia de chufe-v-0-rev-a, que
    # pisaría la página de chufe (las carpetas del sitio usan el nombre del
    # proyecto). Sacar esta línea cuando cuadra tenga su propio proyecto.
    "./placas/cuadra/**",
    # Copia antigua de suma: suma ahora está en su propio repositorio.
    "./placas/popusintes-esquematicos-placas/suma/**",
    # Revisiones antiguas: solamente se publica la más reciente de cada
    # placa, para que la primera exportación de videos no tarde horas.
    # Al publicar una revisión nueva, agregar aquí la anterior.
    "**/atenu-v-0-rev-a/**",
    "**/suma-v-0-rev-a/**",
    "**/ataconso-v-0-rev-b/**",
]
