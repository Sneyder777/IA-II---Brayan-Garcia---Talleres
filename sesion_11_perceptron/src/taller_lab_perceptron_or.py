"""
Taller de Laboratorio: Hackeando los Pesos
----------------------------------------------
Misión Práctica: La Compuerta OR

1. Transcribir el código del perceptrón.
2. Verificar que el código actual (entrenado para AND) da 0 con [1,0], [0,1], [0,0].
3. El Reto: modificar manualmente pesos y sesgo para resolver la Compuerta OR.
4. Reglas del OR: 1 para [1,1],[1,0],[0,1]; 0 solo para [0,0].
5. Anotar los pesos y el sesgo encontrados.

Uso:
    python src/taller_lab_perceptron_or.py
"""

import numpy as np


def funcion_escalon(z):
    return 1 if z >= 0 else 0


def perceptron(X, W, b):
    Z = np.dot(X, W) + b
    return funcion_escalon(Z)


def probar_compuerta(nombre: str, W: np.ndarray, b: float):
    print(f"\n=== Probando compuerta {nombre} con W={W}, b={b} ===")
    entradas_prueba = [
        np.array([1, 1]),
        np.array([1, 0]),
        np.array([0, 1]),
        np.array([0, 0]),
    ]
    for entradas in entradas_prueba:
        salida = perceptron(entradas, W, b)
        print(f"  Entradas {entradas} -> Salida: {salida}")


def main():
    # Paso 2: verificar el perceptrón entrenado para AND
    pesos_and = np.array([0.5, 0.5])
    sesgo_and = -0.8
    probar_compuerta("AND (original)", pesos_and, sesgo_and)

    # Paso 3: "hackear" los pesos para resolver la Compuerta OR
    # Regla encontrada manualmente:
    #   Z = 0.5*X1 + 0.5*X2 - 0.4
    #   [0,0] -> Z=-0.4 (<0)  -> 0
    #   [1,0] -> Z= 0.1 (>=0) -> 1
    #   [0,1] -> Z= 0.1 (>=0) -> 1
    #   [1,1] -> Z= 0.6 (>=0) -> 1
    pesos_or = np.array([0.5, 0.5])
    sesgo_or = -0.4
    probar_compuerta("OR (hackeada)", pesos_or, sesgo_or)

    print(
        "\n=== Pesos y sesgo encontrados para la Compuerta OR ===\n"
        f"W = {pesos_or}\n"
        f"b = {sesgo_or}\n\n"
        "Razonamiento: bajamos el sesgo de -0.8 (AND) a -0.4 (OR). Con -0.8, se "
        "necesitaban AMBAS entradas activas (0.5+0.5=1.0 > 0.8) para superar el "
        "umbral. Con -0.4, basta con que UNA sola entrada esté activa "
        "(0.5 > 0.4) para que Z sea positivo y la neurona dispare, mientras que "
        "con ambas entradas en 0 el sesgo negativo por sí solo mantiene a Z por "
        "debajo de cero."
    )


if __name__ == "__main__":
    main()
