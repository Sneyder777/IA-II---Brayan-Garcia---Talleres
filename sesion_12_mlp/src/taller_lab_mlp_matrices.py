"""
Taller de Laboratorio: Explorando las Matrices
----------------------------------------------------
Misión Práctica:
1. Ejecutar el código base (Perceptrón Multicapa manual con NumPy) y observar
   la probabilidad de salida.
2. Imprimir Z1 y A1, analizar cómo la sigmoide transforma los valores.
3. El Reto Dimensional: procesar 2 clientes al mismo tiempo (batch de 2x3).
4. Confirmar que np.dot calcula ambas salidas sin cambiar las matrices de pesos.

Uso:
    python src/taller_lab_mlp_matrices.py
"""

import numpy as np


def sigmoide(x):
    """Función de Activación Sigmoide (devuelve un valor entre 0 y 1)."""
    return 1 / (1 + np.exp(-x))


def forward_pass(X, W1, b1, W2, b2):
    """Propagación hacia adelante para 1 o varios clientes a la vez (batch)."""
    Z1 = np.dot(X, W1) + b1
    A1 = sigmoide(Z1)

    Z2 = np.dot(A1, W2) + b2
    salida_final = sigmoide(Z2)

    return Z1, A1, Z2, salida_final


def main():
    # Pesos y sesgos de la red (idénticos al material de la sesión)
    W1 = np.array([
        [0.1,  0.2, -0.3,  0.4],
        [-0.5, 0.6,  0.7, -0.8],
        [0.9, -0.1,  0.2,  0.3]
    ])
    b1 = np.array([0.1, -0.2, 0.3, -0.4])  # 4 Sesgos (capa oculta)

    W2 = np.array([0.5, -0.6, 0.7, 0.8])
    b2 = np.array([-0.1])

    # === Paso 1: un solo cliente ===
    print("=== Paso 1: Forward pass con 1 cliente ===")
    X_uno = np.array([0.5, 0.8, 0.2])
    Z1, A1, Z2, salida = forward_pass(X_uno, W1, b1, W2, b2)

    # Paso 2: imprimir Z1 y A1
    print(f"X (entrada): {X_uno}")
    print(f"Z1 (combinación lineal, capa oculta, valores puros): {Z1}")
    print(f"A1 (después de la sigmoide, rango 0-1): {A1}")
    print(f"Predicción de la Red (Probabilidad): {np.round(salida[0], 4)}")

    print(
        "\nAnálisis: los valores de Z1 son números reales sin límite (pueden ser "
        "negativos o mayores a 1). Al pasar por la función sigmoide, CADA valor de "
        "Z1 se 'comprime' al rango abierto (0, 1) — valores muy negativos de Z1 se "
        "acercan a 0, valores muy positivos se acercan a 1, y Z1=0 da exactamente "
        "0.5. Esto es lo que permite interpretar la salida de cada neurona como "
        "algo similar a una probabilidad o nivel de activación."
    )

    # === Paso 3: el Reto Dimensional (batch de 2 clientes) ===
    print("\n=== Paso 3 y 4: El Reto Dimensional (2 clientes en batch, X de 2x3) ===")
    X_batch = np.array([
        [0.5, 0.8, 0.2],
        [0.1, 0.9, 0.9]
    ])

    Z1_batch, A1_batch, Z2_batch, salida_batch = forward_pass(X_batch, W1, b1, W2, b2)

    print(f"X (2 clientes, shape {X_batch.shape}):\n{X_batch}")
    print(f"\nZ1 (shape {Z1_batch.shape}):\n{Z1_batch}")
    print(f"\nA1 (shape {A1_batch.shape}):\n{A1_batch}")
    print(f"\nPredicción de la Red para ambos clientes:")
    for i, prob in enumerate(salida_batch):
        print(f"  Cliente {i + 1}: {np.round(prob, 4)}")

    print(
        "\nConfirmación: usando np.dot(X, W1) con X de shape (2, 3) y W1 de shape "
        "(3, 4), NumPy calcula automáticamente las salidas de AMBOS clientes en "
        "una sola operación matricial, sin necesidad de modificar W1, b1, W2 ni "
        "b2 ni de usar un ciclo for. El resultado Z1 tiene shape (2, 4): una fila "
        "de 4 valores por cada cliente. Este es el poder del cálculo tensorial que "
        "permite a las GPUs procesar miles de ejemplos en paralelo."
    )


if __name__ == "__main__":
    main()
