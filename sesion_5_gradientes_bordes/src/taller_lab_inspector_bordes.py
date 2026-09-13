"""
Taller de Laboratorio: Inspector de Bordes
--------------------------------------------
Desafío Práctico:
1. Cargar una imagen con formas geométricas y texturas complejas.
2. Generar Sobel X (bordes verticales), Sobel Y (bordes horizontales)
   y Canny (bordes finales combinados).
3. Guardar un panel de comparación de los tres.
4. Experimentar con distintos umbrales de Canny (10-50 y 200-250).

Uso:
    python src/taller_lab_inspector_bordes.py --img data/muestra_formas.jpg
"""

import argparse
import cv2
import numpy as np


def calcular_sobel(imagen_gris: np.ndarray):
    sobel_x = cv2.Sobel(imagen_gris, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(imagen_gris, cv2.CV_64F, 0, 1, ksize=3)

    sobel_x_abs = cv2.convertScaleAbs(sobel_x)
    sobel_y_abs = cv2.convertScaleAbs(sobel_y)
    return sobel_x_abs, sobel_y_abs


def construir_panel(imagenes: list, titulos: list) -> np.ndarray:
    """Arma un panel horizontal simple con etiquetas de texto sobre cada imagen."""
    alto, ancho = imagenes[0].shape[:2]
    panel = np.zeros((alto + 30, ancho * len(imagenes)), dtype=np.uint8)

    for i, (img, titulo) in enumerate(zip(imagenes, titulos)):
        panel[30:, i * ancho:(i + 1) * ancho] = img
        cv2.putText(panel, titulo, (i * ancho + 10, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255, 1, cv2.LINE_AA)
    return panel


def main():
    parser = argparse.ArgumentParser(description="Taller: Inspector de bordes")
    parser.add_argument("--img", default="data/muestra_formas.jpg",
                         help="Ruta de una imagen en escala de grises o color")
    args = parser.parse_args()

    imagen = cv2.imread(args.img, cv2.IMREAD_GRAYSCALE)
    if imagen is None:
        raise FileNotFoundError(
            f"No se encontró la imagen en '{args.img}'. "
            "Corran primero: python src/generar_imagen_prueba.py"
        )

    # Paso 2: Sobel X, Sobel Y y Canny "por defecto"
    sobel_x_abs, sobel_y_abs = calcular_sobel(imagen)
    bordes_canny = cv2.Canny(imagen, 50, 150)

    cv2.imwrite("output/1_sobel_x_vertical.jpg", sobel_x_abs)
    cv2.imwrite("output/2_sobel_y_horizontal.jpg", sobel_y_abs)
    cv2.imwrite("output/3_canny_50_150.jpg", bordes_canny)

    # Paso 3: panel de comparación
    panel = construir_panel(
        [imagen, sobel_x_abs, sobel_y_abs, bordes_canny],
        ["Original", "Sobel X", "Sobel Y", "Canny(50,150)"]
    )
    cv2.imwrite("output/4_panel_comparacion.jpg", panel)

    # Paso 4: experimentación con distintos umbrales de Canny
    canny_bajo = cv2.Canny(imagen, 10, 50)
    canny_alto = cv2.Canny(imagen, 200, 250)
    cv2.imwrite("output/5_canny_10_50.jpg", canny_bajo)
    cv2.imwrite("output/6_canny_200_250.jpg", canny_alto)

    pixeles_borde_bajo = int(np.sum(canny_bajo == 255))
    pixeles_borde_medio = int(np.sum(bordes_canny == 255))
    pixeles_borde_alto = int(np.sum(canny_alto == 255))

    print("=== Cantidad de píxeles de borde detectados por Canny ===")
    print(f"Umbrales (10, 50):   {pixeles_borde_bajo} píxeles de borde")
    print(f"Umbrales (50, 150):  {pixeles_borde_medio} píxeles de borde")
    print(f"Umbrales (200, 250): {pixeles_borde_alto} píxeles de borde")

    print(
        "\n=== Análisis ===\n"
        "Con umbrales BAJOS (10, 50) el algoritmo es muy permisivo: detecta como "
        "'borde' incluso variaciones de intensidad pequeñas, por lo que aparecen "
        "muchos bordes falsos en la zona de textura (ruido de alta frecuencia), "
        "aumentando el conteo de píxeles de borde.\n\n"
        "Con umbrales ALTOS (200, 250) el algoritmo es muy estricto: solo detecta "
        "cambios de intensidad muy fuertes, así que ignora bordes reales pero "
        "sutiles (como el contorno del círculo si su contraste no es extremo), "
        "reduciendo el conteo de píxeles de borde y dejando contornos incompletos.\n\n"
        "El punto óptimo para esta imagen suele estar en un rango intermedio "
        "(cercano a 50-150), donde se detectan claramente los bordes de las "
        "figuras geométricas (rectángulo, círculo, triángulo) sin capturar tanto "
        "ruido de la zona de textura."
    )

    print("\nGuardadas en output/: sobel_x, sobel_y, canny (3 variantes) y el panel comparativo.")


if __name__ == "__main__":
    main()
