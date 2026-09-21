"""
Taller de Laboratorio: Fronteras No Lineales (SVM)
------------------------------------------------------
Misión Práctica:
1. Transcribir y ejecutar el código base (kernel lineal). Ver Vectores de Soporte.
2. Agregar un punto "trampa": X=[5,5] con etiqueta 0 (Clase A).
3. Reentrenar el modelo lineal (puede fallar o verse forzado).
4. Cambiar a kernel='rbf'. Reentrenar y predecir.
5. Reflexionar sobre cuándo un kernel lineal fallaría en el mundo real.

Uso:
    python src/taller_lab_svm_fronteras.py
"""

import numpy as np
from sklearn.svm import SVC


def parte_1_kernel_lineal():
    print("=== Parte 1: SVM con Kernel Lineal (dataset original) ===")
    X = np.array([[2, 2], [3, 3], [4, 2], [6, 6], [7, 8], [8, 7]])
    Y = np.array([0, 0, 0, 1, 1, 1])

    modelo_svm = SVC(kernel='linear')
    modelo_svm.fit(X, Y)

    vectores = modelo_svm.support_vectors_
    print(f"Vectores de Soporte encontrados por el modelo:\n{vectores}")

    nuevo_punto = np.array([[5, 4]])
    pred = modelo_svm.predict(nuevo_punto)
    print(f"El punto [5,4] pertenece a la clase: {pred[0]}")

    return X, Y


def parte_2_punto_trampa(X, Y):
    print("\n=== Parte 2: Agregando el punto 'trampa' [5,5] como Clase A (0) ===")
    X_nuevo = np.vstack([X, [5, 5]])
    Y_nuevo = np.append(Y, 0)

    print("Nuevo dataset:")
    for punto, etiqueta in zip(X_nuevo, Y_nuevo):
        print(f"  {punto} -> Clase {etiqueta}")

    # Paso 3: reentrenar con kernel lineal (probablemente forzado / peor margen)
    modelo_lineal = SVC(kernel='linear')
    modelo_lineal.fit(X_nuevo, Y_nuevo)
    print(f"\n[Kernel LINEAL] Vectores de soporte:\n{modelo_lineal.support_vectors_}")
    print(f"[Kernel LINEAL] Precisión sobre el propio dataset de entrenamiento: "
          f"{modelo_lineal.score(X_nuevo, Y_nuevo):.2f}")

    # Paso 4: cambiar a kernel RBF
    modelo_rbf = SVC(kernel='rbf')
    modelo_rbf.fit(X_nuevo, Y_nuevo)
    print(f"\n[Kernel RBF] Vectores de soporte:\n{modelo_rbf.support_vectors_}")
    print(f"[Kernel RBF] Precisión sobre el propio dataset de entrenamiento: "
          f"{modelo_rbf.score(X_nuevo, Y_nuevo):.2f}")

    nuevo_punto = np.array([[5, 4]])
    pred_lineal = modelo_lineal.predict(nuevo_punto)
    pred_rbf = modelo_rbf.predict(nuevo_punto)
    print(f"\nPredicción para [5,4] -> Lineal: {pred_lineal[0]}, RBF: {pred_rbf[0]}")


def parte_5_reflexion():
    print(
        "\n=== Punto 5: Reflexión ===\n"
        "El 'Kernel Trick' (RBF) permite al SVM aislar puntos que están 'rodeados' "
        "por la clase enemiga, proyectando los datos a una dimensión donde sí son "
        "separables. En el mundo real, esto es crítico en escenarios donde una "
        "clase puede estar rodeada topológicamente por otra sin que exista una "
        "frontera recta posible:\n\n"
        "- MEDICINA: en el diagnóstico de una enfermedad basado en dos biomarcadores, "
        "es común que los pacientes 'sanos' formen un grupo central y los pacientes "
        "en riesgo aparezcan tanto por valores muy bajos como muy altos de un "
        "biomarcador (ej. niveles de una hormona). Una línea recta no puede separar "
        "'sano' (en el centro) de 'en riesgo' (en ambos extremos) — se necesita una "
        "frontera curva/circular, que es exactamente lo que RBF puede modelar.\n\n"
        "- RECONOCIMIENTO FACIAL: las variaciones de iluminación, ángulo y expresión "
        "hacen que las imágenes de una misma persona no formen un grupo compacto y "
        "linealmente separable en el espacio de características; las fronteras "
        "entre identidades suelen ser altamente no lineales, por lo que kernels "
        "como RBF (o redes neuronales, que son aproximadores universales similares) "
        "son necesarios para lograr buena precisión."
    )


def main():
    X, Y = parte_1_kernel_lineal()
    parte_2_punto_trampa(X, Y)
    parte_5_reflexion()


if __name__ == "__main__":
    main()
