# Sesión 5 — Gradientes y Detección de Bordes: Respuestas

## Taller Analítico: Calculando el Gradiente

Matriz 3x3 con un borde vertical perfecto (mitad izquierda negra, mitad
derecha blanca):

```
0    0   255
0    0   255
0    0   255
```

### Punto 1 — Convolución con Sobel X (Gx)

Kernel Sobel X:

```
-1   0   1
-2   0   2
-1   0   1
```

Multiplicación elemento a elemento y suma total (producto punto):

```
Fila 1: (-1*0) + (0*0)   + (1*255) = 255
Fila 2: (-2*0) + (0*0)   + (2*255) = 510
Fila 3: (-1*0) + (0*0)   + (1*255) = 255

Gx = 255 + 510 + 255 = 1020
```

**El gradiente en X es 1020**, un valor muy alto (fuera del rango normal de
0-255 antes de normalizar), lo que indica un **cambio de intensidad muy
fuerte en la dirección horizontal** — exactamente lo que se espera al cruzar
un borde vertical perfecto.

### Punto 2 — Convolución con Sobel Y (Gy)

Kernel Sobel Y:

```
-1  -2  -1
 0   0   0
 1   2   1
```

Multiplicación elemento a elemento y suma total:

```
Fila 1: (-1*0) + (-2*0) + (-1*255) = -255
Fila 2: (0*0)  + (0*0)  + (0*255)  = 0
Fila 3: (1*0)  + (2*0)  + (1*255)  = 255

Gy = -255 + 0 + 255 = 0
```

**El gradiente en Y es 0** porque las tres filas de la matriz son
**idénticas** (0, 0, 255 en cada una): no hay ningún cambio de intensidad al
moverse verticalmente (de arriba hacia abajo). Esto indica que el borde
detectado es **puramente vertical**: la intensidad cambia solo al moverse de
izquierda a derecha, nunca de arriba a abajo. Un Gy = 0 combinado con un Gx
grande es la firma matemática exacta de un borde vertical perfecto.
