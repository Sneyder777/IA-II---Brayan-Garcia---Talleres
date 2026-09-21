"""
Taller de Laboratorio: Clasificador Universal (KNN)
------------------------------------------------------
Misión Práctica:
1. Transcribir el código base de KNN.
2. Ampliar el dataset a al menos 10 puntos, con 3 dimensiones
   (Edad, Salario, Número de Hijos).
3. Actualizar las etiquetas correspondientes.
4. Experimentar con K=1 y K=5.
5. Reflexionar sobre la Maldición de la Dimensionalidad.

Uso:
    python src/taller_lab_knn_clasificador.py
"""

import numpy as np
from sklearn.neighbors import KNeighborsClassifier


def construir_dataset():
    """
    Dataset ampliado: [Edad, Salario (miles), Número de Hijos]
    Etiqueta: 0 = NO COMPRA, 1 = COMPRA
    """
    X_entrenamiento = np.array([
        [20, 30, 0],   # No compra: joven, salario bajo, sin hijos
        [22, 28, 0],
        [25, 32, 1],
        [40, 50, 2],   # Compra: adulto, salario alto
        [42, 55, 1],
        [35, 45, 2],
        [45, 60, 3],
        [50, 65, 2],
        [23, 29, 0],
        [38, 48, 1],
    ])

    Y_entrenamiento = np.array([0, 0, 0, 1, 1, 1, 1, 1, 0, 1])

    return X_entrenamiento, Y_entrenamiento


def entrenar_y_predecir(X, Y, nuevo_cliente, k):
    modelo_knn = KNeighborsClassifier(n_neighbors=k)
    modelo_knn.fit(X, Y)
    prediccion = modelo_knn.predict(nuevo_cliente)
    return prediccion[0]


def main():
    X_entrenamiento, Y_entrenamiento = construir_dataset()
    nuevo_cliente = np.array([[30, 40, 1]])  # Edad 30, Salario 40, 1 hijo

    print(f"Dataset de entrenamiento ({X_entrenamiento.shape[0]} puntos, "
          f"{X_entrenamiento.shape[1]} dimensiones):")
    for fila, etiqueta in zip(X_entrenamiento, Y_entrenamiento):
        print(f"  {fila} -> {'COMPRA' if etiqueta == 1 else 'NO COMPRA'}")

    print(f"\nNuevo cliente a clasificar: {nuevo_cliente[0]}")

    # Paso 4: experimentar con K=1 y K=5
    pred_k1 = entrenar_y_predecir(X_entrenamiento, Y_entrenamiento, nuevo_cliente, k=1)
    pred_k5 = entrenar_y_predecir(X_entrenamiento, Y_entrenamiento, nuevo_cliente, k=5)

    print(f"\nCon K=1 -> Clase predicha: {'COMPRA' if pred_k1 == 1 else 'NO COMPRA'}")
    print(f"Con K=5 -> Clase predicha: {'COMPRA' if pred_k5 == 1 else 'NO COMPRA'}")

    print(
        "\n=== Pregunta de análisis: Maldición de la Dimensionalidad ===\n"
        "Si en lugar de 3 columnas tuviéramos 1,000 columnas (como los píxeles de "
        "una imagen), la Distancia Euclidiana pierde su poder discriminativo. "
        "Matemáticamente, a medida que aumenta el número de dimensiones, el volumen "
        "del espacio crece exponencialmente, y los puntos de datos quedan cada vez "
        "más dispersos entre sí. El efecto observable es que la distancia entre el "
        "punto MÁS cercano y el punto MÁS lejano tiende a volverse casi igual "
        "(todas las distancias convergen a valores similares), por lo que el "
        "concepto de 'vecino cercano' deja de ser significativo: ya no hay una "
        "diferencia clara entre quién es 'vecino' y quién no. Esto degrada "
        "seriamente el rendimiento de KNN en datasets de alta dimensionalidad, y es "
        "la razón por la que en visión por computador se prefiere extraer "
        "características relevantes (como en la Sesión 6) en lugar de usar los "
        "píxeles crudos como entrada directa a KNN."
    )


if __name__ == "__main__":
    main()
