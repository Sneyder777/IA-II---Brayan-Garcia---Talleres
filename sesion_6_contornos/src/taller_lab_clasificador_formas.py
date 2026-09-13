"""
Taller de Laboratorio: Clasificador de Formas
------------------------------------------------
Misión Práctica (Proyecto Integrador del Módulo 1):
1. Cargar una imagen con varios objetos (monedas) de distintos tamaños
   sobre un fondo uniforme.
2. Aplicar todo el pipeline: Grises -> Umbralización -> Limpieza
   Morfológica -> Detección de Contornos.
3. Imprimir en consola el área de cada objeto encontrado.
4. Lógica empresarial: si el área es mayor a "X" píxeles, dibujar un
   Bounding Box AZUL (objeto grande); si es menor, dibujar uno ROJO
   (objeto pequeño).

Uso:
    python src/taller_lab_clasificador_formas.py --img data/monedas.jpg --umbral-area 1500
"""

import argparse
import cv2
import numpy as np


def procesar_pipeline(imagen_color: np.ndarray):
    """Aplica el pipeline completo de las 6 clases: Grises -> Umbralización
    (Otsu) -> Limpieza morfológica (Apertura) -> Contornos."""
    # 1. Conversión a grises
    gris = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2GRAY)

    # 2. Umbralización con el método de Otsu (calcula el mejor T automáticamente)
    # Usamos THRESH_BINARY_INV porque las monedas son más oscuras que el fondo
    _, binaria = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # 3. Limpieza morfológica: Apertura para quitar ruido pequeño
    kernel = np.ones((5, 5), np.uint8)
    limpia = cv2.morphologyEx(binaria, cv2.MORPH_OPEN, kernel)

    # 4. Detección de contornos (solo el contorno externo de cada objeto)
    contornos, _ = cv2.findContours(limpia, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return gris, binaria, limpia, contornos


def clasificar_y_dibujar(imagen_color: np.ndarray, contornos, umbral_area: float):
    resultado = imagen_color.copy()
    reporte = []

    for i, cnt in enumerate(contornos, start=1):
        area = cv2.contourArea(cnt)

        # Filtramos ruido menor (objetos demasiado pequeños para ser válidos)
        if area < 50:
            continue

        x, y, w, h = cv2.boundingRect(cnt)

        # Lógica empresarial: grande (azul) vs pequeño (rojo)
        if area > umbral_area:
            color = (255, 0, 0)  # Azul (BGR) -> objeto grande
            categoria = "GRANDE"
        else:
            color = (0, 0, 255)  # Rojo (BGR) -> objeto pequeño
            categoria = "pequeño"

        cv2.rectangle(resultado, (x, y), (x + w, y + h), color, 2)

        # Centroide usando momentos espaciales
        M = cv2.moments(cnt)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(resultado, (cx, cy), 4, (0, 255, 0), -1)
        else:
            cx, cy = x + w // 2, y + h // 2

        reporte.append((i, area, categoria, (cx, cy)))

    return resultado, reporte


def main():
    parser = argparse.ArgumentParser(description="Taller: Clasificador de formas por área")
    parser.add_argument("--img", default="data/monedas.jpg",
                         help="Ruta de la imagen con varios objetos")
    parser.add_argument("--umbral-area", type=float, default=1500,
                         help="Área (en píxeles) que separa objeto grande de pequeño")
    args = parser.parse_args()

    imagen_color = cv2.imread(args.img)
    if imagen_color is None:
        raise FileNotFoundError(
            f"No se encontró la imagen en '{args.img}'. "
            "Corran primero: python src/generar_imagen_monedas.py"
        )

    gris, binaria, limpia, contornos = procesar_pipeline(imagen_color)
    resultado, reporte = clasificar_y_dibujar(imagen_color, contornos, args.umbral_area)

    cv2.imwrite("output/1_grises.jpg", gris)
    cv2.imwrite("output/2_binaria_otsu.jpg", binaria)
    cv2.imwrite("output/3_limpia_morfologia.jpg", limpia)
    cv2.imwrite("output/4_clasificacion_final.jpg", resultado)

    print(f"Se encontraron {len(reporte)} objetos válidos.\n")
    print("=== Reporte de áreas por objeto ===")
    for idx, area, categoria, centro in reporte:
        print(f"Objeto {idx}: área = {area:.1f} px^2  -> {categoria}  (centro aprox: {centro})")

    print(f"\nUmbral de área usado para clasificar: {args.umbral_area} px^2")
    print("Guardadas en output/: grises, binaria (Otsu), limpia (morfología) "
          "y la clasificación final con Bounding Boxes.")


if __name__ == "__main__":
    main()
