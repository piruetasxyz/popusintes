# Configuración de kicad-visor (https://github.com/piruetasxyz/kicad-visor)
# para las placas de popusintes, que están como submódulos en placas/.
#
# kicad-visor busca todos los .kicad_pro bajo la raíz. Acá se excluyen los
# que no van en el sitio. Los patrones son relativos a la raíz, con "./"
# al principio, y "*" también calza con "/".

# Videos turntable, más cortos y menos que los de kicad-visor por defecto
# (2 giros × 3 formatos × 4 fondos, de 6 s: 24 videos por placa). Acá: un
# giro, un formato y dos fondos, de 4 s: 2 videos por placa.
#
# El tiempo de render depende de giros × formatos × segundos; los fondos
# casi no cuestan (solo se vuelve a codificar el video), así que agregar
# colores es barato y agregar giros o formatos es caro.
turntables = [("z", "ccw")]  # gira como un disco, vista desde arriba en ángulo
aspects = {"square": (1080, 1080)}
backgrounds = {"white": "#ffffff", "pink": "#ff9ecf"}
turntable_seconds = 4

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
