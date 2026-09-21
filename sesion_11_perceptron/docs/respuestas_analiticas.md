# Sesión 11 — El Perceptrón: Respuestas

## Taller Analítico: Calculando el Disparo

Perceptrón para aprobar crédito. Pesos: W1 = 0.8 (Ingresos), W2 = -0.5 (Deudas).
Sesgo: b = -10.

Cliente: Ingresos (X1) = 50, Deudas (X2) = 20.

### Punto 1 — Cálculo de Z

```
Z = (X1 · W1) + (X2 · W2) + b
Z = (50 · 0.8) + (20 · -0.5) + (-10)
Z = 40 - 10 - 10
Z = 20
```

### Punto 2 — Función Escalón

```
Z = 20  →  Z ≥ 0  →  Salida = 1
```

**La neurona SÍ dispara: el crédito se aprueba (Salida = 1).**

### Punto 3 — ¿Por qué tiene sentido que W2 sea negativo?

Porque W2 pondera la variable "Deudas". En el contexto del negocio, entre MÁS
deudas tenga un cliente, MENOS probable debería ser que se le apruebe un
crédito nuevo. Un peso negativo logra exactamente ese efecto matemático: a
medida que X2 (deudas) aumenta, el término `X2 · W2` se vuelve más negativo,
restando valor a Z y acercando la decisión hacia el rechazo (Z < 0). Si W2
fuera positivo, el modelo aprobaría MÁS crédito mientras más deudas tuviera el
cliente, lo cual sería contrario a la lógica de negocio. El signo del peso es,
en esencia, la forma en que la red "codifica" si una variable ayuda o perjudica
la decisión final.

---

## Taller de Laboratorio: Hackeando los Pesos — Compuerta OR

Al correr `src/taller_lab_perceptron_or.py`:

- El perceptrón original (`W=[0.5, 0.5]`, `b=-0.8`) resuelve correctamente la
  compuerta **AND**: solo dispara 1 cuando ambas entradas son 1.
- Modificando **únicamente el sesgo** de `-0.8` a `-0.4` (dejando los mismos
  pesos `W=[0.5, 0.5]`), el perceptrón resuelve la compuerta **OR**:

| Entradas | Z = 0.5·X1 + 0.5·X2 - 0.4 | Salida |
|---|---|---|
| [1, 1] | 0.6 | 1 |
| [1, 0] | 0.1 | 1 |
| [0, 1] | 0.1 | 1 |
| [0, 0] | -0.4 | 0 |

**Pesos y sesgo finales: W = [0.5, 0.5], b = -0.4**

Con el sesgo de -0.8 (AND) se necesitaba que AMBAS entradas estuvieran activas
para que la suma de pesos (1.0) superara el umbral. Al subir el sesgo a -0.4,
basta con que UNA sola entrada esté activa (0.5 > 0.4) para que Z sea positivo,
mientras que con ambas entradas en 0 el sesgo negativo por sí solo mantiene a Z
por debajo de cero. Este mismo tipo de ajuste automático de pesos y sesgos es
justamente lo que un algoritmo de entrenamiento (como el que se vería en
próximas sesiones) hace de forma iterativa en lugar de manual.
