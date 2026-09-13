"""
generar_imagen_prueba.py
------------------------
Genera una imagen en escala de grises con formas geométricas claras
(rectángulo, círculo, triángulo) y una zona de textura (ruido de alta
frecuencia) para poder practicar detección de bordes con Sobel y Canny.

Uso:
    python src/generar_imagen_prueba.py
"""

import os
import cv2
import numpy as np


def generar_imagen(ruta_salida: str, alto: int = 400, ancho: int = 500) -> None:
    imagen = np.full((alto, ancho), 30, dtype=np.uint8)

    # Formas geométricas claras (alto contraste con el fondo)
    cv2.rectangle(imagen, (40, 40), (180, 180), 220, -1)
    cv2.circle(imagen, (330, 110), 80, 200, -1)
    pts = np.array([[100, 350], [200, 250], [300, 350]], np.int32)
    cv2.fillPoly(imagen, [pts], 180)

    # Zona de textura compleja (simula un "paisaje con edificios"):
    # ruido de alta frecuencia en una región rectangular
    x0, y0, x1, y1 = 340, 250, 480, 380
    textura = np.random.randint(60, 200, (y1 - y0, x1 - x0), dtype=np.uint8)
    imagen[y0:y1, x0:x1] = textura

    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    cv2.imwrite(ruta_salida, imagen)
    print(f"Imagen de prueba (formas + textura) generada en: {ruta_salida}")


if __name__ == "__main__":
    generar_imagen("data/muestra_formas.jpg")
