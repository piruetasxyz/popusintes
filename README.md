# popusintes

## About

popusintes is the open source hardware Eurorack synthesizer line by [piruetas](https://piruetas.xyz). This repository is its hub website, <https://piruetas.xyz/popusintes/>: links to every module and to the tools made for them, and a page per board (schematic, board layers, 3D renders and turntable videos) generated with [kicad-visor](https://github.com/piruetasxyz/kicad-visor).

## Acerca de

Sitio de popusintes, la línea de sintetizadores eurorack de código abierto de [piruetas](https://piruetas.xyz): <https://piruetas.xyz/popusintes/>.

- `index.html`: la portada, con los módulos, la alimentación y las herramientas. Se escribe a mano.
- `placas/`: los repositorios de cada placa, como submódulos de git.
- `kicad-visor-config.py`: qué placas se publican.
- `.github/workflows/publicar.yml`: arma y publica el sitio.

## Cómo funciona

En cada push a `main`, cada lunes, o a mano desde la pestaña Actions, el workflow:

1. lleva cada submódulo de `placas/` al último commit de su rama principal,
2. exporta con kicad-visor todas las placas a `placas/` del sitio,
3. agrega `index.html` y publica todo en GitHub Pages.

Para activarlo, una vez: Settings > Pages > Build and deployment > Source: "GitHub Actions".

La primera ejecución renderiza los videos de todas las placas y puede tardar bastante (los videos se configuran en `kicad-visor-config.py`). Los frames quedan en caché aunque la ejecución se corte, así que si se acaba el tiempo basta con volver a correrla. Después solo se renderizan las placas que cambian.

## Agregar una placa

```bash
git submodule add https://github.com/piruetasxyz/<repo>.git placas/<repo>
```

Luego agregar su tarjeta en `index.html`, con enlace a `placas/<proyecto>/`, donde `<proyecto>` es el nombre del `.kicad_pro`.

## Nueva revisión de una placa

Solo se publica la revisión más reciente de cada placa. Al publicar una nueva:

1. en `kicad-visor-config.py`, agregar la revisión anterior a `exclude`,
2. en `index.html`, cambiar los enlaces e imágenes de esa placa al nombre nuevo.

## Ver el sitio localmente

```bash
git clone --recurse-submodules https://github.com/piruetasxyz/popusintes.git
cd popusintes
kicad-visor export . --output _site/placas
cp index.html _site/
open _site/index.html
```

## Acerca de piruetas

[piruetas](https://piruetas.xyz) es un estudio de arte chileno fundado en 2022 por [montoyamoraga](https://montoyamoraga.io), con base en Santiago de Chile.

- web: [piruetas.xyz](https://piruetas.xyz)
- github: [github.com/piruetasxyz](https://github.com/piruetasxyz)
- instagram: [@piruetas.xyz](https://instagram.com/piruetas.xyz)
