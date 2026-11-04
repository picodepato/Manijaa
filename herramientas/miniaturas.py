#!/usr/bin/env python3
"""Genera las versiones ligeras (WebP de hasta 1000 px de ancho) de las fotos de img/.

La web las usa en la galería, la residencia y la bio para que en el móvil se
descarguen fotos bastante más ligeras que los JPG originales (hasta un 70 % menos). El visor de fotos
sigue abriendo el JPG original a tamaño completo.

Uso (desde la carpeta de la web):
    pip install pillow
    python3 herramientas/miniaturas.py

Si cambias una foto de img/, vuelve a ejecutarlo. Si no puedes, borra su .webp
de img/webp/: la web usará automáticamente el JPG original.
"""
from pathlib import Path

from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "img"
DESTINO = ORIGEN / "webp"
ANCHO = 1000  # suficiente para móviles de pantalla 3x; nunca se amplía el original
CALIDAD = 74
OMITIR = {"hero.jpg"}  # la portada necesita la foto completa


def main() -> None:
    DESTINO.mkdir(exist_ok=True)
    for foto in sorted(ORIGEN.glob("*.jpg")):
        if foto.name in OMITIR:
            continue
        salida = DESTINO / (foto.stem + ".webp")
        with Image.open(foto) as im:
            im = im.convert("RGB")
            if im.width > ANCHO:
                im = im.resize((ANCHO, round(im.height * ANCHO / im.width)), Image.LANCZOS)
            im.save(salida, "WEBP", quality=CALIDAD, method=6)
        print(f"{foto.name:24s} {foto.stat().st_size // 1024:4d} KB  ->  {salida.relative_to(RAIZ)}  {salida.stat().st_size // 1024:3d} KB")


if __name__ == "__main__":
    main()
