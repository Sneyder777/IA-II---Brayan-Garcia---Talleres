# Sesión 4 — Convolución: Respuestas

## Taller Analítico: Calculando la Convolución

Imagen (I), sección 3x3 con un "ruido de sal" en el centro (valor 250):

```
10   20   30
15  250   15
20   10   20
```

Kernel (K) de filtro de media 3x3, cada celda vale 1/9:

```
1/9  1/9  1/9
1/9  1/9  1/9
1/9  1/9  1/9
```

### Punto 1 — Nuevo valor del píxel central

La convolución con un kernel de media equivale a sumar todos los valores de
la región y dividir entre 9 (el número de celdas):

```
Suma = 10 + 20 + 30 + 15 + 250 + 15 + 20 + 10 + 20 = 390
Nuevo valor = 390 / 9 = 43.33 ≈ 43
```

El píxel central pasa de **250** a aproximadamente **43**.

### Punto 2 — ¿Por qué el filtro de media difumina/suaviza la imagen?

Porque cada nuevo píxel deja de depender únicamente de su propio valor y pasa
a ser un **promedio de su vecindad**. El valor atípico (250, un pico de ruido)
queda "repartido" entre los 9 píxeles de la ventana en lugar de mantenerse
aislado: su influencia se diluye proporcionalmente (1/9 de su valor original)
mientras que los 8 vecinos —todos con valores bajos y similares entre sí—
dominan el resultado final. El efecto visual es que las transiciones bruscas
de intensidad (como el ruido, pero también los bordes reales) se vuelven
graduales, es decir, la imagen se ve "borrosa" o suavizada.

---

## Taller de Laboratorio: Estrategias de Suavizado

Al correr `src/taller_lab_suavizado.py` con un kernel agresivo de 7x7 sobre
una imagen con ruido de Sal y Pimienta:

- El **Filtro de Media** y el **Filtro Gaussiano** dejan manchas grises
  alrededor de cada punto de ruido, porque promedian linealmente todos los
  valores bajo el kernel — incluidos los extremos de 0 y 255 del ruido —, así
  que ese ruido "contamina" el resultado en vez de desaparecer.
- El **Filtro de Mediana** elimina casi por completo el ruido sin dejar
  manchas, porque no promedia: ordena los valores bajo el kernel y toma el
  del medio. Como el ruido disperso normalmente es minoría dentro de cada
  ventana, sus valores extremos quedan en los bordes del arreglo ordenado y
  nunca resultan elegidos como mediana.

**Conclusión:** para ruido de tipo impulso (sal y pimienta), el Filtro de
Mediana es claramente superior a los filtros lineales (Media y Gaussiano).
