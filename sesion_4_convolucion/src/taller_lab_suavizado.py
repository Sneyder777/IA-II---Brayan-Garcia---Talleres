"""
Taller de Laboratorio: Estrategias de Suavizado
--------------------------------------------------
Desafío Práctico:
1. Cargar/crear una imagen con ruido de Sal y Pimienta.
2. Aplicar los tres filtros (Media, Gaussiano, Mediana) con Kernel 7x7.
3. Guardar los tres resultados para comparar.
4. Análisis crítico: por qué el Filtro de Mediana ignora los extremos
   mientras que el Filtro de Media crea "manchas" grises.

Uso:
    python src/taller_lab_suavizado.py --img data/imagen_ruidosa.jpg
"""

import argparse
import cv2
import numpy as np


def main():
    parser = argparse.ArgumentParser(description="Taller: Estrategias de suavizado")
    parser.add_argument("--img", default="data/imagen_ruidosa.jpg",
                         help="Ruta de la imagen con ruido")
    parser.add_argument("--kernel", type=int, default=7,
                         help="Tamaño del kernel (impar), por defecto 7x7")
    args = parser.parse_args()

    imagen = cv2.imread(args.img)
    if imagen is None:
        raise FileNotFoundError(
            f"No se encontró la imagen en '{args.img}'. "
            "Corran primero: python src/generar_imagen_ruidosa.py"
        )

    k = args.kernel

    # 1. Filtro de Media (promedio simple)
    blur_media = cv2.blur(imagen, (k, k))

    # 2. Filtro Gaussiano (pesos según campana de Gauss)
    blur_gauss = cv2.GaussianBlur(imagen, (k, k), 0)

    # 3. Filtro de Mediana (excelente para ruido sal y pimienta)
    blur_mediana = cv2.medianBlur(imagen, k)

    cv2.imwrite("output/1_original_ruidosa.jpg", imagen)
    cv2.imwrite("output/2_filtro_media.jpg", blur_media)
    cv2.imwrite("output/3_filtro_gaussiano.jpg", blur_gauss)
    cv2.imwrite("output/4_filtro_mediana.jpg", blur_mediana)

    print(f"Filtros aplicados con kernel {k}x{k}. Resultados guardados en output/:")
    print("  1_original_ruidosa.jpg")
    print("  2_filtro_media.jpg")
    print("  3_filtro_gaussiano.jpg")
    print("  4_filtro_mediana.jpg")

    print(
        "\n=== Análisis crítico ===\n"
        "El Filtro de Media y el Gaussiano son operaciones LINEALES: calculan un "
        "promedio (ponderado o no) de todos los píxeles bajo el kernel, incluyendo "
        "los valores extremos de 0 y 255 del ruido sal y pimienta. Como esos "
        "extremos SÍ participan en la suma, 'contaminan' el promedio y generan una "
        "mancha gris alrededor de cada punto de ruido, en vez de eliminarlo.\n\n"
        "El Filtro de Mediana es una operación NO lineal: ordena todos los valores "
        "bajo el kernel de menor a mayor y toma el valor central (la mediana "
        "estadística). Si el ruido de sal/pimienta es una minoría de píxeles dentro "
        "de la ventana (lo usual con ruido disperso), esos valores extremos quedan "
        "en los bordes de la lista ordenada y NUNCA caen en la posición central, "
        "así que son directamente descartados en vez de promediados. Por eso la "
        "Mediana elimina el ruido de impulso sin dejar manchas grises."
    )


if __name__ == "__main__":
    main()
