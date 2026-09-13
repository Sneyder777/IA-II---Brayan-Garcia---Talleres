# Taller Analítico 1: Operaciones con Tensores

## Pregunta 1
**Si ejecutamos `recorte = imagen[100:200, 300:400, 1]` sobre una imagen de 1920x1080,
¿cuáles son las dimensiones exactas (shape) de la variable `recorte` resultante y qué
información específica contiene?**

- `shape` resultante: **(100, 100)** → 100 filas x 100 columnas.
- Es una **matriz 2D**, no un tensor de 3 canales, porque al fijar el índice `1` en la
  tercera dimensión se elimina esa dimensión.
- Contiene únicamente los valores de intensidad del **canal Verde** (índice 1 en el
  orden BGR de OpenCV), correspondientes a la región rectangular de la imagen original
  delimitada por las filas 100 a 199 y las columnas 300 a 399.

## Pregunta 2
**¿Por qué es computacionalmente más eficiente aislar un canal usando Slicing
(`img[:, :, 0]`) en lugar de crear dos ciclos `for` anidados para iterar sobre la
altura y anchura?**

- NumPy almacena la imagen en un **bloque contiguo de memoria** (arreglo C-contiguous).
  `img[:, :, 0]` no copia los datos: crea una **vista (view)** que reutiliza el mismo
  bloque de memoria cambiando únicamente el "stride" (paso) con el que se recorre,
  por lo que su costo de creación es prácticamente O(1).
- Las operaciones posteriores sobre esa vista se ejecutan en **código C compilado**
  dentro de NumPy, aprovechando **vectorización SIMD** del procesador (varias
  operaciones por ciclo de reloj).
- Un doble `for` en Python, en cambio, ejecuta el **intérprete** de Python
  instrucción por instrucción para cada uno de los `alto * ancho` píxeles, con el
  overhead de resolver tipos dinámicos en cada acceso `imagen[i][j][k]`.
- Además, el acceso aleatorio píxel a píxel desde Python **rompe la localidad de
  caché** de la CPU, mientras que las operaciones vectorizadas de NumPy están
  optimizadas para aprovecharla.
- Resultado práctico: el slicing/vectorización puede ser entre 10x y varios cientos
  de veces más rápido que el doble bucle equivalente, dependiendo del tamaño de la
  imagen.

---

## Taller de Laboratorio 1: pregunta de reflexión
**¿Qué valor de gris (intensidad de 0 a 255) arroja un amarillo puro (BGR = [0, 255, 255])?**

Aplicando `Y = 0.299*R + 0.587*G + 0.114*B` con R=255, G=255, B=0:

```
Y = 0.299*255 + 0.587*255 + 0.114*0 = 225.93 ≈ 226
```

El resultado (≈226/255) es un gris **muy claro, cercano al blanco**. Esto ocurre
porque la fórmula pondera fuertemente el canal Verde (0.587), y el amarillo tiene
ese canal al máximo (255), a diferencia del canal Azul (peso 0.114) que en el
amarillo puro vale 0.

## Taller de Laboratorio 2: conclusión de ejemplo
Al correr `src/taller_lab2_histograma.py` sobre la imagen de muestra generada
(`generar_imagen_prueba.py`), el script imprime la intensidad media de cada canal
y concluye cuál domina la iluminación general. **Reemplacen esta sección con la
conclusión real que obtengan al correrlo sobre su propia fotografía**, describiendo
si el histograma está desplazado a la izquierda (subexpuesta), a la derecha
(sobreexpuesta) o distribuido en todo el rango (buen contraste).
