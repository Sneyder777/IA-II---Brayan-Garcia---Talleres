# Sesión 12 — Redes Neuronales Densas (MLP): Respuestas

## Taller Analítico: Contando Parámetros

Arquitectura: 3 entradas (Edad, Ingresos, Deuda) → 1 Capa Oculta con 4 neuronas
→ 1 Capa de Salida con 1 neurona.

### Punto 1 — Pesos (W) entre Capa de Entrada y Capa Oculta

Cada una de las 3 entradas se conecta con cada una de las 4 neuronas ocultas
(red totalmente conectada / Fully Connected):

```
Pesos = 3 entradas × 4 neuronas ocultas = 12 pesos
```

### Punto 2 — Sesgos de la Capa Oculta

Cada neurona oculta tiene su propio sesgo (bias), independientemente de cuántas
entradas reciba:

```
Sesgos (capa oculta) = 4 neuronas × 1 sesgo cada una = 4 sesgos
```

### Punto 3 — Pesos y Sesgo entre Capa Oculta y Capa de Salida

Cada una de las 4 neuronas ocultas se conecta con la única neurona de salida:

```
Pesos (oculta -> salida) = 4 neuronas ocultas × 1 neurona de salida = 4 pesos
Sesgo (salida) = 1 neurona de salida × 1 sesgo = 1 sesgo
```

### Punto 4 — Total de parámetros entrenables

```
Total = Pesos(entrada→oculta) + Sesgos(oculta) + Pesos(oculta→salida) + Sesgo(salida)
Total = 12 + 4 + 4 + 1
Total = 21 parámetros entrenables
```

**Esta pequeña red neuronal tiene 21 parámetros que el algoritmo de
entrenamiento deberá ajustar.**

---

## Taller de Laboratorio: Explorando las Matrices

Al correr `src/taller_lab_mlp_matrices.py`:

- **Paso 1-2 (un solo cliente):** el código imprime `Z1` (los valores puros de
  la combinación lineal en la capa oculta, sin límite de rango) y `A1` (los
  mismos valores después de pasar por la sigmoide). Se observa cómo cada valor
  de `Z1` — que puede ser cualquier número real, positivo o negativo — queda
  "comprimido" dentro del rango abierto (0, 1) en `A1`: valores muy negativos
  de Z1 se acercan a 0, valores muy positivos se acercan a 1, y un Z1 igual a 0
  produce exactamente 0.5.

- **Paso 3-4 (Reto Dimensional, batch de 2 clientes):** al cambiar `X` de un
  vector de 3 valores a una matriz de shape `(2, 3)` (dos clientes, tres
  características cada uno), el mismo código —sin ninguna modificación en las
  matrices de pesos `W1`, `b1`, `W2`, `b2`— calcula automáticamente las salidas
  de ambos clientes en una sola operación (`np.dot`). El resultado `Z1` pasa a
  tener shape `(2, 4)`: una fila de 4 activaciones por cada cliente. Esto
  confirma que el álgebra lineal (y por extensión, el hardware de una GPU) es
  capaz de procesar múltiples ejemplos en paralelo sin cambiar ni una línea de
  la arquitectura del modelo — es la base matemática de por qué el Deep
  Learning se entrena en "lotes" (batches) en lugar de un ejemplo a la vez.
