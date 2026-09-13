"""
generar_imagen_prueba.py
------------------------
Genera una imagen sintética (data/muestra.jpg) en formato BGR para poder
correr los talleres aunque no tengan todavía una foto propia a la mano.

Uso:
    python src/generar_imagen_prueba.py

Si ya tienen su propia imagen, simplemente cópienla a data/muestra.jpg
(o pasen la ruta con --img en los otros scripts) y no necesitan este paso.
"""

import os
import cv2
import numpy as np


def generar_imagen(ruta_salida: str, alto: int = 480, ancho: int = 640) -> None:
    # Fondo con degradado (para que el histograma no sea un solo pico)
    imagen = np.zeros((alto, ancho, 3), dtype=np.uint8)

    # Degradado horizontal en el canal Rojo y vertical en el canal Verde
    for x in range(ancho):
        imagen[:, x, 2] = int(255 * x / ancho)          # Rojo (índice 2 en BGR)
    for y in range(alto):
        imagen[y, :, 1] = int(255 * y / alto)            # Verde (índice 1 en BGR)

    # Un poco de Azul constante + ruido para variar el histograma
    imagen[:, :, 0] = 80
    ruido = np.random.randint(0, 40, (alto, ancho), dtype=np.uint8)
    imagen[:, :, 0] = cv2.add(imagen[:, :, 0], ruido)

    # Un cuadrado amarillo intenso en el centro (útil para el Taller de Laboratorio 1)
    cy, cx = alto // 2, ancho // 2
    imagen[cy - 40:cy + 40, cx - 40:cx + 40] = [0, 255, 255]  # BGR amarillo puro

    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    cv2.imwrite(ruta_salida, imagen)
    print(f"Imagen de prueba generada en: {ruta_salida}")


if __name__ == "__main__":
    generar_imagen("data/muestra.jpg")
