"""
generar_imagen_ruidosa.py
--------------------------
Genera una imagen con ruido tipo "Sal y Pimienta" (píxeles completamente
blancos y negros dispersos al azar) para poder practicar filtros de
suavizado (Media, Gaussiano, Mediana).

Uso:
    python src/generar_imagen_ruidosa.py
"""

import os
import cv2
import numpy as np


def agregar_ruido_sal_pimienta(imagen: np.ndarray, cantidad: float = 0.05) -> np.ndarray:
    salida = np.copy(imagen)
    total_pixeles = imagen.shape[0] * imagen.shape[1]

    # Ruido de "sal" (píxeles blancos)
    num_sal = int(total_pixeles * cantidad / 2)
    coords_x = np.random.randint(0, imagen.shape[0], num_sal)
    coords_y = np.random.randint(0, imagen.shape[1], num_sal)
    salida[coords_x, coords_y] = 255

    # Ruido de "pimienta" (píxeles negros)
    num_pimienta = int(total_pixeles * cantidad / 2)
    coords_x = np.random.randint(0, imagen.shape[0], num_pimienta)
    coords_y = np.random.randint(0, imagen.shape[1], num_pimienta)
    salida[coords_x, coords_y] = 0

    return salida


def generar_imagen(ruta_salida: str, alto: int = 400, ancho: int = 500) -> None:
    # Imagen base con algunas formas para poder ver cómo el ruido afecta bordes
    imagen = np.full((alto, ancho), 120, dtype=np.uint8)
    cv2.rectangle(imagen, (100, 100), (250, 250), 200, -1)
    cv2.circle(imagen, (370, 180), 60, 40, -1)

    imagen_ruidosa = agregar_ruido_sal_pimienta(imagen, cantidad=0.06)

    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    cv2.imwrite(ruta_salida, imagen_ruidosa)
    print(f"Imagen con ruido sal y pimienta generada en: {ruta_salida}")


if __name__ == "__main__":
    generar_imagen("data/imagen_ruidosa.jpg")
