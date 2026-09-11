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
| — | — | Aún no hay talleres publicados | — |

> Cada nuevo taller se agrega como `taller-01/`, `taller-02/`… y se registra en esta tabla.

## Estructura

```
.
├── README.md              # este archivo
├── requirements.txt       # dependencias del repositorio
├── verificar_entorno.py   # comprueba que OpenCV y NumPy estén bien instalados
└── taller-NN/             # una carpeta por taller
    ├── README.md          # enunciado, solución y conclusiones
    ├── main.py            # código del taller
    ├── recursos/          # imágenes / datos de entrada
    └── resultados/        # salidas generadas
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
python taller-01/main.py
```

## Convención de commits

Mensajes cortos en presente, con prefijo del taller:

```
taller-01: agrega lectura y conversión a escala de grises
docs: actualiza tabla de talleres
```
