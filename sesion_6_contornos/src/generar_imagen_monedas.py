"""
generar_imagen_monedas.py
--------------------------
Genera una imagen sintética con "monedas" (círculos) de distintos tamaños
sobre un fondo uniforme, para poder practicar el pipeline completo:
Grises -> Umbralización -> Limpieza morfológica -> Contornos.

Uso:
    python src/generar_imagen_monedas.py
"""

import os
import cv2
import numpy as np


def generar_imagen(ruta_salida: str, alto: int = 400, ancho: int = 600) -> None:
    # Fondo uniforme claro
    imagen = np.full((alto, ancho, 3), 220, dtype=np.uint8)

    # "Monedas" de distintos tamaños (círculos oscuros, como monedas metálicas)
    monedas = [
        (100, 100, 45),   # (x, y, radio) -> grande
        (250, 120, 25),    # pequeña
        (400, 100, 50),    # grande
        (150, 280, 20),    # pequeña
        (350, 290, 35),    # mediana/grande
        (500, 250, 15),    # pequeña
    ]

    for (x, y, r) in monedas:
        cv2.circle(imagen, (x, y), r, (90, 90, 90), -1)
        cv2.circle(imagen, (x, y), r, (60, 60, 60), 2)  # borde un poco más oscuro

    # Un poco de ruido para que no sea perfecto
    ruido = np.random.normal(0, 5, imagen.shape).astype(np.int16)
    imagen = np.clip(imagen.astype(np.int16) + ruido, 0, 255).astype(np.uint8)

    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    cv2.imwrite(ruta_salida, imagen)
    print(f"Imagen de prueba (monedas de distinto tamaño) generada en: {ruta_salida}")


if __name__ == "__main__":
    generar_imagen("data/monedas.jpg")
