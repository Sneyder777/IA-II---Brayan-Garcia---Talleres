"""
Taller de Laboratorio 2: Análisis Estadístico (Histogramas)
------------------------------------------------------------
1. Carga una imagen RGB/BGR
2. Separa la imagen en sus 3 canales (B, G, R)
3. Calcula el histograma de cada canal por separado
4. Grafica los tres histogramas superpuestos (azul, verde, rojo)
5. Concluye cuál es el color dominante en la iluminación general

Uso:
    python src/taller_lab2_histograma.py --img data/muestra.jpg
"""

import argparse
import cv2
import numpy as np
import matplotlib
matplotlib.use("Agg")  # permite generar la imagen sin necesitar una pantalla
import matplotlib.pyplot as plt


def calcular_histogramas(imagen: np.ndarray):
    colores = ("b", "g", "r")
    histogramas = {}
    for i, color in enumerate(colores):
        hist = cv2.calcHist([imagen], [i], None, [256], [0, 256])
        histogramas[color] = hist
    return histogramas


def graficar_histogramas(histogramas: dict, ruta_salida: str) -> None:
    plt.figure(figsize=(9, 5))
    nombres = {"b": "Azul", "g": "Verde", "r": "Rojo"}
    for color, hist in histogramas.items():
        plt.plot(hist, color=color, label=nombres[color])

    plt.title("Distribución de Intensidades por Canal (BGR)")
    plt.xlabel("Valor del Píxel (0-255)")
    plt.ylabel("Frecuencia (Cantidad de píxeles)")
    plt.legend()
    plt.xlim([0, 256])
    plt.tight_layout()
    plt.savefig(ruta_salida)
    print(f"Gráfico guardado en: {ruta_salida}")


def color_dominante(histogramas: dict) -> str:
    """
    Aproxima el 'color dominante en la iluminación general' comparando
    la intensidad media ponderada de cada canal (no solo el pico del histograma,
    porque el pico puede estar en zonas oscuras sin representar la iluminación).
    """
    nombres = {"b": "Azul", "g": "Verde", "r": "Rojo"}
    medias = {}
    for color, hist in histogramas.items():
        niveles = np.arange(256)
        total_pixeles = hist.sum()
        media = float((hist.flatten() * niveles).sum() / total_pixeles)
        medias[color] = media

    dominante = max(medias, key=medias.get)
    print("\nIntensidad media por canal:")
    for color, media in medias.items():
        print(f"  {nombres[color]}: {media:.2f}")

    return nombres[dominante]


def main():
    parser = argparse.ArgumentParser(description="Taller de Laboratorio 2: Histograma por canal")
    parser.add_argument("--img", default="data/muestra.jpg", help="Ruta de la imagen a analizar")
    parser.add_argument("--out", default="output/histograma_canales.png",
                         help="Ruta donde guardar el gráfico")
    args = parser.parse_args()

    imagen = cv2.imread(args.img)
    if imagen is None:
        raise FileNotFoundError(
            f"No se encontró la imagen en '{args.img}'. "
            "Corran primero: python src/generar_imagen_prueba.py"
        )

    print(f"Imagen cargada: {args.img} -> shape {imagen.shape}")

    histogramas = calcular_histogramas(imagen)
    graficar_histogramas(histogramas, args.out)

    dominante = color_dominante(histogramas)
    print(f"\nConclusión: el color dominante en la iluminación general es el {dominante.upper()}.")


if __name__ == "__main__":
    main()
