# Sesión 9 — KNN: Respuestas

## Taller Analítico: La Votación Espacial

Dataset histórico:
- Cliente A(20, 30) → NO COMPRA
- Cliente B(40, 50) → COMPRA
- Cliente C(35, 45) → COMPRA

Punto nuevo: (30, 40)

### Punto 1 — Distancias Euclidianas

```
d(Nuevo, A) = √[(30-20)² + (40-30)²] = √[100 + 100] = √200 ≈ 14.14
d(Nuevo, B) = √[(30-40)² + (40-50)²] = √[100 + 100] = √200 ≈ 14.14
d(Nuevo, C) = √[(30-35)² + (40-45)²] = √[25 + 25]   = √50  ≈ 7.07
```

### Punto 2 — Clasificación con K = 1

El vecino más cercano es **C** (distancia ≈ 7.07, la menor de las tres).
Como C es COMPRA, con **K=1 el nuevo cliente se clasifica como COMPRA**.

### Punto 3 — Clasificación con K = 3

Con K=3 se consultan los 3 puntos disponibles (todo el dataset). La votación es:

```
A -> NO COMPRA
B -> COMPRA
C -> COMPRA
```

2 votos a favor de COMPRA contra 1 de NO COMPRA → **con K=3 el resultado también es
COMPRA**.

**¿Hubo cambio en la decisión?** No. Aunque K=1 solo mira al vecino más cercano
(C) y K=3 consulta a los tres, la mayoría también favorece a COMPRA porque dos de
los tres puntos del dataset (B y C) pertenecen a esa clase. En un dataset más
grande, K=1 y K=3 sí podrían dar resultados distintos si el vecino más cercano
fuera un "outlier" rodeado de vecinos de la clase contraria.

---

## Taller de Laboratorio: Clasificador Universal

Al correr `src/taller_lab_knn_clasificador.py` con un dataset ampliado a 10 puntos
y 3 dimensiones (Edad, Salario, Número de Hijos), tanto K=1 como K=5 clasifican
al nuevo cliente de forma consistente con el patrón general del dataset
(clientes con mayor edad y salario tienden a "COMPRA").

### Pregunta de análisis: Maldición de la Dimensionalidad

Si en lugar de 3 columnas tuviéramos 1,000 (como los píxeles de una imagen), la
Distancia Euclidiana deja de ser útil: en espacios de muy alta dimensión, el
volumen del espacio crece exponencialmente y los puntos quedan extremadamente
dispersos entre sí. Como consecuencia, la distancia entre el vecino más cercano y
el más lejano tiende a converger hacia un valor similar — todo empieza a estar
"igual de lejos" de todo —, por lo que el concepto mismo de "vecino más cercano"
pierde su poder discriminativo. Esta es la razón práctica por la que, en visión
por computador, se prefiere extraer características relevantes (área, perímetro,
histogramas, etc., como en sesiones anteriores) en lugar de alimentar a KNN
directamente con los píxeles crudos de una imagen.
