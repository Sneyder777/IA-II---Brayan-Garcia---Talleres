"""
generar_imagen_prueba.py
------------------------
Genera una imagen en escala de grises con poco contraste (simula una foto
con mala iluminación) para poder practicar Umbralización y Morfología
Matemática sin depender de tener una foto real a la mano.

Uso:
    python src/generar_imagen_prueba.py
"""

import os
import cv2
import numpy as np


def generar_imagen(ruta_salida: str, alto: int = 400, ancho: int = 500) -> None:
    # Fondo gris oscuro de bajo contraste (simula mala iluminación)
    imagen = np.full((alto, ancho), 60, dtype=np.uint8)

    # "Objeto de interés": un rectángulo y un círculo más claros que el fondo
    cv2.rectangle(imagen, (120, 120), (280, 280), 180, -1)
    cv2.circle(imagen, (380, 200), 70, 200, -1)

    # Ruido leve tipo gaussiano para que no sea una imagen perfecta
    ruido = np.random.normal(0, 8, (alto, ancho)).astype(np.int16)
    imagen = np.clip(imagen.astype(np.int16) + ruido, 0, 255).astype(np.uint8)

    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    cv2.imwrite(ruta_salida, imagen)
    print(f"Imagen de prueba (bajo contraste) generada en: {ruta_salida}")


if __name__ == "__main__":
    generar_imagen("data/muestra_gris.jpg")
