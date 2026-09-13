"""
Taller de Laboratorio 1: Transformación de Espacios
----------------------------------------------------
1. Crea un píxel BGR amarillo puro: [0, 255, 255]
2. Calcula su valor en escala de grises con la fórmula ponderada
   Y = 0.299*R + 0.587*G + 0.114*B  (usando NumPy, sin funciones de OpenCV)
3. Imprime el resultado
4. Corrobora el proceso usando cv2.cvtColor sobre una imagen real

Uso:
    python src/taller_lab1_grayscale.py --img data/muestra.jpg
"""

import argparse
import cv2
import numpy as np


def gris_manual_pixel(pixel_bgr: np.ndarray) -> float:
    """Calcula el valor de gris de UN píxel en formato BGR con la fórmula ponderada."""
    b, g, r = pixel_bgr[0], pixel_bgr[1], pixel_bgr[2]
    # W = [0.114, 0.587, 0.299] ajustado al orden BGR
    return 0.114 * b + 0.587 * g + 0.299 * r


def gris_manual_imagen(imagen: np.ndarray) -> np.ndarray:
    """
    Versión vectorizada (producto punto) aplicada a toda la imagen,
    equivalente a lo que hace cv2.cvtColor(..., COLOR_BGR2GRAY) por dentro.
    """
    pesos = np.array([0.114, 0.587, 0.299])  # orden BGR
    gris = np.dot(imagen[..., :3], pesos)
    return gris.astype(np.uint8)


def main():
    parser = argparse.ArgumentParser(description="Taller de Laboratorio 1: Escala de grises")
    parser.add_argument("--img", default="data/muestra.jpg", help="Ruta de una imagen real")
    args = parser.parse_args()

    print("=== Paso 1 y 2: píxel amarillo puro ===")
    pixel = np.array([0, 255, 255])  # BGR: Azul=0, Verde=255, Rojo=255
    print(f"pixel (BGR) = {pixel}")

    valor_gris = gris_manual_pixel(pixel)
    print("\n=== Paso 3: resultado ===")
    print(f"Y = 0.299*R + 0.587*G + 0.114*B "
          f"= 0.299*{pixel[2]} + 0.587*{pixel[1]} + 0.114*{pixel[0]} = {valor_gris:.3f}")
    print(
        f"\nEl amarillo puro se ve en gris con una intensidad ≈ {round(valor_gris)} / 255, "
        "es decir, MUY CLARO (casi blanco), porque el ojo humano (y por tanto la "
        "fórmula) le da muchísimo peso al canal Verde, que en el amarillo está al máximo."
    )

    print("\n=== Paso 4: corroboración con una imagen real usando OpenCV ===")
    imagen = cv2.imread(args.img)
    if imagen is None:
        raise FileNotFoundError(
            f"No se encontró la imagen en '{args.img}'. "
            "Corran primero: python src/generar_imagen_prueba.py"
        )

    img_gris_manual = gris_manual_imagen(imagen)
    img_gris_opencv = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    diferencia = np.abs(img_gris_manual.astype(int) - img_gris_opencv.astype(int))
    print(f"Diferencia máxima entre método manual y cv2.cvtColor: {diferencia.max()} "
          "(valores de 0-1 son solo redondeo de cv2, confirmando que la fórmula es la misma)")

    cv2.imwrite("output/gris_manual.jpg", img_gris_manual)
    cv2.imwrite("output/gris_opencv.jpg", img_gris_opencv)
    print("\nGuardadas: output/gris_manual.jpg y output/gris_opencv.jpg")


if __name__ == "__main__":
    main()
