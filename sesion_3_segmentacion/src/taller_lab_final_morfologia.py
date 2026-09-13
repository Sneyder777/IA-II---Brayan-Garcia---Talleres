"""
Taller de Laboratorio Final: Limpiando la Visión
--------------------------------------------------
Desafío Práctico: Tratamiento de Ruido

1. Carga una imagen en escala de grises de bajo contraste.
2. Aplica cv2.threshold con un valor estático que introduzca ruido intencional.
3. Construye un Elemento Estructurante de 3x3.
4. Aplica Apertura (Erosión + Dilatación) para limpiar el fondo.
5. Aplica Cierre (Dilatación + Erosión) en una variable diferente.
6. Guarda las 3 imágenes (Original binarizada, Apertura, Cierre) y concluye
   cuál operación fue más efectiva.

Uso:
    python src/taller_lab_final_morfologia.py --img data/muestra_gris.jpg
"""

import argparse
import cv2
import numpy as np


def binarizar_con_ruido(imagen_gris: np.ndarray, T: int = 100) -> np.ndarray:
    """
    Paso 2: Umbralización estática. Usamos un T relativamente permisivo
    para que, junto con el ruido de la imagen, aparezcan píxeles blancos
    sueltos en el fondo (ruido de sal) que luego limpiaremos con morfología.
    """
    _, binaria = cv2.threshold(imagen_gris, T, 255, cv2.THRESH_BINARY)
    return binaria


def aplicar_apertura(imagen_binaria: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """Apertura = Erosión seguida de Dilatación. Elimina ruido externo (sal)
    sin encoger permanentemente el objeto principal."""
    erosionada = cv2.erode(imagen_binaria, kernel, iterations=1)
    apertura = cv2.dilate(erosionada, kernel, iterations=1)
    return apertura


def aplicar_cierre(imagen_binaria: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """Cierre = Dilatación seguida de Erosión. Rellena huecos internos
    (ruido de pimienta) dentro del objeto."""
    dilatada = cv2.dilate(imagen_binaria, kernel, iterations=1)
    cierre = cv2.erode(dilatada, kernel, iterations=1)
    return cierre


def main():
    parser = argparse.ArgumentParser(description="Taller: Limpieza morfológica de ruido")
    parser.add_argument("--img", default="data/muestra_gris.jpg",
                         help="Ruta de una imagen en escala de grises")
    parser.add_argument("--umbral", type=int, default=100,
                         help="Valor T de umbralización estática")
    args = parser.parse_args()

    imagen_gris = cv2.imread(args.img, cv2.IMREAD_GRAYSCALE)
    if imagen_gris is None:
        raise FileNotFoundError(
            f"No se encontró la imagen en '{args.img}'. "
            "Corran primero: python src/generar_imagen_prueba.py"
        )

    # Paso 2: binarización con ruido intencional
    binaria = binarizar_con_ruido(imagen_gris, T=args.umbral)
    cv2.imwrite("output/1_binaria_con_ruido.jpg", binaria)

    # Paso 3: elemento estructurante 3x3
    kernel = np.ones((3, 3), np.uint8)

    # Paso 4 y 5: Apertura y Cierre
    apertura = aplicar_apertura(binaria, kernel)
    cierre = aplicar_cierre(binaria, kernel)

    cv2.imwrite("output/2_apertura.jpg", apertura)
    cv2.imwrite("output/3_cierre.jpg", cierre)

    # Métrica simple para comparar cuál "limpió" más ruido de fondo:
    # contamos píxeles blancos aislados aproximando con la diferencia
    # de píxeles blancos totales entre binaria original y cada resultado.
    blancos_original = int(np.sum(binaria == 255))
    blancos_apertura = int(np.sum(apertura == 255))
    blancos_cierre = int(np.sum(cierre == 255))

    print("=== Conteo de píxeles blancos (255) ===")
    print(f"Binaria original: {blancos_original}")
    print(f"Después de Apertura: {blancos_apertura} "
          f"(diferencia: {blancos_original - blancos_apertura})")
    print(f"Después de Cierre:   {blancos_cierre} "
          f"(diferencia: {blancos_cierre - blancos_original})")

    print(
        "\nConclusión: la Apertura reduce el conteo de blancos porque erosiona primero, "
        "eliminando puntos blancos aislados sobre el fondo oscuro (ruido de sal), y "
        "luego dilata para devolver su tamaño al objeto principal sin el ruido. "
        "El Cierre, en cambio, aumenta o mantiene el conteo de blancos porque dilata "
        "primero, rellenando huecos negros dentro del objeto (ruido de pimienta), y "
        "luego erosiona para no dejarlo más grande de lo normal. "
        "Para ESTA imagen (ruido tipo sal sobre el fondo), la Apertura es la más "
        "efectiva, porque el problema principal son puntos blancos sueltos en el "
        "fondo, no huecos dentro del objeto."
    )

    print("\nGuardadas: output/1_binaria_con_ruido.jpg, "
          "output/2_apertura.jpg, output/3_cierre.jpg")


if __name__ == "__main__":
    main()
