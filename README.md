# IA II — Talleres

Repositorio de talleres de **Inteligencia Artificial II**.

| | |
|---|---|
| **Autor** | Brayan Sneyder Garcia Camacho |
| **Materia** | Inteligencia Artificial II |
| **Lenguaje** | Python 3.10+ |
| **Librerías base** | OpenCV, NumPy |
| **Licencia** | MIT |

## Objetivo

Resolver y documentar los talleres de la materia con commits diarios, de modo que el
historial del repositorio refleje el avance real. Cada taller es autocontenido: su código,
sus recursos de entrada y sus resultados viven en su propia carpeta.

## Ruta de talleres

| Taller | Carpeta | Tema | Estado |
|---|---|---|---|
| 01 | `taller_1/` | (completar según el contenido de esta carpeta) | ✅ |
| 02 | `sesion_2_tensor_color/` | Tensor de color (BGR), slicing de canales, escala de grises, histogramas | ✅ |
| 03 | `sesion_3_segmentacion/` | Umbralización, Erosión, Dilatación, Apertura, Cierre | ✅ |
| 04 | `sesion_4_convolucion/` | Convolución 2D, Filtro de Media, Gaussiano y Mediana | ✅ |
| 05 | `sesion_5_gradientes_bordes/` | Operadores de Sobel, Algoritmo de Canny | ✅ |
| 06 | `sesion_6_contornos/` | `findContours`, Bounding Box, Momentos espaciales, área y centroide | ✅ |

> Los talleres numerados con el prefijo `taller-NN/` siguen la plantilla base del repo.
> Los talleres de las clases del docente Amaury Giovanni Méndez Aguirre se agregan como
> `sesion_N_tema/`, siguiendo la numeración de sesión de la asignatura.

## Estructura

```
.
├── README.md                        # este archivo
├── requirements.txt                 # dependencias del repositorio
├── verificar_entorno.py             # comprueba que OpenCV y NumPy estén bien instalados
├── taller_1/                        # taller base del repositorio
│   ├── README.md
│   ├── main.py
│   ├── recursos/
│   └── resultados/
└── sesion_N_tema/                   # una carpeta por sesión de clase
    ├── src/                         # scripts de Python (incluye generador de imagen de prueba)
    ├── docs/                        # respuestas_analiticas.md con las respuestas escritas
    ├── data/                        # imágenes de entrada (contenido no versionado)
    └── output/                      # resultados generados al correr los scripts
```

## Instalación

```bash
git clone https://github.com/Sneyder777/IA-II---Brayan-Garcia---Talleres.git
cd IA-II---Brayan-Garcia---Talleres

python -m venv .venv
# Windows:        .venv\Scripts\activate
# Linux / macOS:  source .venv/bin/activate

pip install -r requirements.txt
python verificar_entorno.py
```

## Uso

```bash
# Taller base
python taller_1/main.py

# Sesiones de clase (ejemplo con la Sesión 6)
cd sesion_6_contornos
python src/generar_imagen_monedas.py
python src/taller_lab_clasificador_formas.py --img data/monedas.jpg --umbral-area 1500
```

Consulta el `docs/respuestas_analiticas.md` de cada sesión para ver las respuestas
a las preguntas de discusión, y la carpeta `output/` para los resultados de ejemplo.

## Convención de commits

Mensajes cortos en presente, con prefijo del taller o sesión:

```
taller-01: agrega lectura y conversión a escala de grises
sesion-6: agrega clasificador de formas por contornos
docs: actualiza tabla de talleres
```
