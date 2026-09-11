"""Verifica que el entorno tenga OpenCV y NumPy listos para los talleres."""

import sys


def main() -> int:
    try:
        import cv2
        import numpy as np
    except ImportError as e:
        print(f"[ERROR] Falta una dependencia: {e.name}")
        print("Ejecuta: pip install -r requirements.txt")
        return 1

    print(f"Python : {sys.version.split()[0]}")
    print(f"OpenCV : {cv2.__version__}")
    print(f"NumPy  : {np.__version__}")

    lienzo = np.zeros((60, 160, 3), dtype=np.uint8)
    cv2.putText(lienzo, "OK", (45, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
    print(f"Prueba : imagen {lienzo.shape} creada y dibujada correctamente")
    print("\nEntorno listo.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
