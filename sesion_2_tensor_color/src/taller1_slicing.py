"""
Taller Analítico 1: Operaciones con Tensores
---------------------------------------------
Cubre:
1. Slicing avanzado sobre un tensor de imagen (imagen[100:200, 300:400, 1])
2. Extracción de canales individuales (B, G, R) sin usar bucles for
3. Creación de una versión "solo canal rojo" de la imagen

Uso:
    python src/taller1_slicing.py --img data/muestra.jpg
"""

import argparse
import cv2
import numpy as np


def analizar_recorte(imagen: np.ndarray) -> None:
    """Punto 1 del taller: recorte = imagen[100:200, 300:400, 1]"""
    alto, ancho, canales = imagen.shape
    print(f"Dimensiones de la imagen cargada: {imagen.shape} (Alto, Ancho, Canales)")

    # Ajustamos el recorte a los límites reales de la imagen para que el
    # ejemplo siempre corra, sin importar el tamaño de la foto que usen.
    y0, y1 = min(100, alto), min(200, alto)
    x0, x1 = min(300, ancho), min(400, ancho)

    recorte = imagen[y0:y1, x0:x1, 1]  # canal índice 1 = Verde en BGR
    print(f"\nrecorte = imagen[{y0}:{y1}, {x0}:{x1}, 1]")
    print(f"Shape del recorte: {recorte.shape}  -> (alto_recorte, ancho_recorte)")
    print(
        "Contenido: es una matriz 2D (ya NO es un tensor de 3 canales) con la "
        "intensidad del canal VERDE únicamente, en la región de filas "
        f"{y0}-{y1} y columnas {x0}-{x1} de la imagen original."
    )

    # Nota conceptual para una imagen 1920x1080 (como pide el enunciado):
    print(
        "\nNota (para una imagen de 1920x1080): "
        "imagen[100:200, 300:400, 1] daría un recorte de shape (100, 100), "
        "es decir 100 filas x 100 columnas, conteniendo solo los valores del "
        "canal Verde de esa región rectangular."
    )


def separar_canales(imagen: np.ndarray):
    """Extracción de canales usando slicing (sin bucles for)."""
    canal_azul = imagen[:, :, 0]
    canal_verde = imagen[:, :, 1]
    canal_rojo = imagen[:, :, 2]
    return canal_azul, canal_verde, canal_rojo


def imagen_solo_roja(imagen: np.ndarray) -> np.ndarray:
    """Apaga los canales azul y verde dejando solo la información roja."""
    resultado = np.copy(imagen)
    resultado[:, :, 0] = 0  # Azul a 0
    resultado[:, :, 1] = 0  # Verde a 0
    return resultado


def eficiencia_slicing_vs_for() -> None:
    print("\n--- Punto 2: ¿Por qué el slicing es más eficiente que un doble for? ---")
    print(
        "NumPy almacena la imagen como un bloque contiguo de memoria (C-contiguous).\n"
        "img[:, :, 0] no copia dato por dato: crea una VISTA (view) que reutiliza el\n"
        "mismo bloque de memoria con un 'stride' distinto, así que el costo es O(1)\n"
        "en tiempo de creación (no recorre nada) y las operaciones posteriores se\n"
        "ejecutan en C usando vectorización SIMD del procesador.\n\n"
        "Un doble for en Python, en cambio, ejecuta el bytecode del intérprete\n"
        "píxel por píxel (alto*ancho iteraciones), con overhead de tipos dinámicos\n"
        "en cada acceso imagen[i][j][k]. Además rompe la localidad de caché porque\n"
        "salta de forma poco predecible por la memoria. Por eso el slicing puede ser\n"
        "cientos de veces más rápido que los bucles anidados equivalentes."
    )


def main():
    parser = argparse.ArgumentParser(description="Taller Analítico 1: Slicing de tensores")
    parser.add_argument("--img", default="data/muestra.jpg", help="Ruta de la imagen a usar")
    args = parser.parse_args()

    imagen = cv2.imread(args.img)
    if imagen is None:
        raise FileNotFoundError(
            f"No se encontró la imagen en '{args.img}'. "
            "Corran primero: python src/generar_imagen_prueba.py"
        )

    print("=== 1. Descomposición del tensor y slicing avanzado ===\n")
    analizar_recorte(imagen)

    canal_azul, canal_verde, canal_rojo = separar_canales(imagen)
    print(f"\nShapes individuales -> Azul: {canal_azul.shape}, "
          f"Verde: {canal_verde.shape}, Rojo: {canal_rojo.shape}")

    roja = imagen_solo_roja(imagen)
    cv2.imwrite("output/imagen_solo_roja.jpg", roja)
    print("\nGuardada: output/imagen_solo_roja.jpg (solo canal rojo activo)")

    eficiencia_slicing_vs_for()


if __name__ == "__main__":
    main()
