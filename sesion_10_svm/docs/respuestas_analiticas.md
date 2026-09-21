# Sesión 10 — SVM: Respuestas

## Taller Analítico: Dibujando el Margen

Puntos:
- Clase A (Círculos): (2,2), (3,3), (4,2)
- Clase B (Equis): (6,6), (7,8), (8,7)

### Punto 1 — Línea óptima

La línea que separa ambas clases con el mayor margen posible pasa entre los
puntos más cercanos de cada grupo. Verificado con el modelo `SVC(kernel='linear')`
de Scikit-Learn sobre este mismo dataset, la frontera óptima queda equidistante
entre el segmento formado por (3,3) y (4,2) de la Clase A, y el punto (6,6) de la
Clase B — es decir, una línea diagonal (pendiente negativa a positiva, aprox.
perpendicular a la dirección que va de (3.5, 2.5) hacia (6,6)).

### Punto 2 — Vectores de Soporte

Ejecutando el modelo real, los **Vectores de Soporte son exactamente 3 puntos**:

```
(3, 3)  -> Clase A
(4, 2)  -> Clase A
(6, 6)  -> Clase B
```

Estos son los puntos más cercanos a la frontera de decisión en cada clase. Los
demás puntos — (2,2) de la Clase A, y (7,8) y (8,7) de la Clase B — están más
alejados del margen y **no influyen** en la posición final de la línea.

### Punto 3 — ¿Cambiaría la línea si agregamos A(1,1)?

**No, la línea no cambiaría.** El punto (1,1) está incluso más lejos del grupo B
que el punto (2,2), que ya de por sí no era un Vector de Soporte. Según la teoría
de SVM, el hiperplano óptimo depende ÚNICAMENTE de los Vectores de Soporte (los
puntos más cercanos al margen); cualquier punto adicional que quede "detrás" de
esos vectores de soporte, más lejos de la frontera, es irrelevante para el
cálculo del margen. Esto se puede confirmar reentrenando el modelo con ese punto
agregado: los vectores de soporte y la frontera de decisión permanecen iguales.

---

## Taller de Laboratorio: Fronteras No Lineales

Al ejecutar `src/taller_lab_svm_fronteras.py`:

- **Parte 1 (Kernel lineal, dataset original):** los Vectores de Soporte
  obtenidos por el modelo son `(3,3)`, `(4,2)` y `(6,6)` — coinciden exactamente
  con los identificados a mano en el Taller Analítico.
- **Parte 2 (punto trampa [5,5] como Clase A):** al agregar este punto, que
  queda geométricamente muy cerca del grupo B, el kernel lineal se ve forzado a
  ajustar su frontera; los nuevos vectores de soporte pasan a ser `(5,5)` y
  `(6,6)`, es decir, el margen se vuelve mucho más estrecho pero aún logra
  separar ambas clases con una línea recta.
- **Kernel RBF:** al cambiar a `kernel='rbf'`, el modelo usa muchos más puntos
  como vectores de soporte (proyecta los datos a una dimensión superior donde
  puede trazar una frontera curva), logrando una separación más flexible.

### Punto 5 — Reflexión: ¿cuándo fallaría un kernel lineal?

Un kernel lineal fallaría por completo en escenarios donde una clase queda
"rodeada" topológicamente por otra, sin que exista ninguna línea recta capaz de
separarlas:

- **Medicina:** al diagnosticar con dos biomarcadores, los pacientes "sanos"
  suelen agruparse en un rango central de valores, mientras que el riesgo
  aparece tanto en valores muy bajos como muy altos de un biomarcador. Una recta
  no puede separar un grupo central de dos extremos — se necesita una frontera
  curva/circular, que es justamente lo que el Kernel RBF puede modelar.
- **Reconocimiento facial:** las variaciones de iluminación, ángulo y expresión
  hacen que las fronteras entre identidades sean altamente no lineales en el
  espacio de características, por lo que un kernel lineal sería insuficiente y
  se requeriría RBF (o un enfoque de Deep Learning).
