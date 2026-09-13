# Sesión 6 — Extracción de Características y Contornos: Respuestas

## Taller Analítico: Bounding Box

Coordenadas de las 4 esquinas de un contorno irregular:

```
A(2, 4)   B(8, 2)   C(10, 7)   D(3, 9)
```

### Punto 1 — Coordenadas extremas

```
X_min = min(2, 8, 10, 3) = 2
Y_min = min(4, 2, 7, 9)  = 2
X_max = max(2, 8, 10, 3) = 10
Y_max = max(4, 2, 7, 9)  = 9
```

**El Bounding Box queda definido por la esquina superior izquierda (2, 2) y
la esquina inferior derecha (10, 9).**

### Punto 2 — Ancho (W) y alto (H)

```
W = X_max - X_min = 10 - 2 = 8
H = Y_max - Y_min = 9 - 2  = 7
```

**El Bounding Box mide 8 unidades de ancho por 7 unidades de alto.**

---

## Taller de Laboratorio: Clasificador de Formas

Al correr `src/taller_lab_clasificador_formas.py` sobre la imagen sintética
de monedas (generada con `generar_imagen_monedas.py`), el pipeline completo
(Grises → Umbralización de Otsu → Apertura morfológica → `findContours`)
detecta cada moneda como un contorno independiente, calcula su área con
`cv2.contourArea` y su centroide con los momentos espaciales (`cv2.moments`).

La lógica empresarial aplicada usa un umbral de área (parámetro
`--umbral-area`, por defecto 1500 px²) para decidir el color del Bounding
Box:

- **Azul**: el área del objeto es mayor al umbral → se clasifica como
  "GRANDE".
- **Rojo**: el área es menor o igual al umbral → se clasifica como
  "pequeño".

Este umbral puede ajustarse según el caso real (por ejemplo, si las monedas
de la foto real son más grandes o pequeñas que las de la imagen sintética),
simplemente pasando `--umbral-area <valor>` al ejecutar el script.
