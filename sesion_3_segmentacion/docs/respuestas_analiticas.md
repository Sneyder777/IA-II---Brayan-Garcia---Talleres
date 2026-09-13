# Sesión 3 — Segmentación: Respuestas

## Taller Analítico 1: Función Escalón

Matriz original (intensidades de gris):

```
 80  120  140
 90  200  210
 50  130  250
```

### Punto 1 — Umbralización binaria con T = 135

Regla: `f(x,y) = 255 si I(x,y) >= 135`, si no `f(x,y) = 0`.

| Valor | ¿>= 135? | Resultado |
|---|---|---|
| 80  | No  | 0   |
| 120 | No  | 0   |
| 140 | Sí  | 255 |
| 90  | No  | 0   |
| 200 | Sí  | 255 |
| 210 | Sí  | 255 |
| 50  | No  | 0   |
| 130 | No  | 0   |
| 250 | Sí  | 255 |

**Matriz resultante:**

```
  0    0   255
  0  255   255
  0    0   255
```

### Punto 2 — Error de elegir T = 135 si el objetivo era aislar valores > 100

Si el objetivo real era "aislar todo lo mayor a 100", los valores **120** y **130**
deberían haber quedado en 255 (blanco), porque ambos son mayores a 100. Sin
embargo, con T = 135 ambos quedan en 0 (negro) porque no alcanzan ese umbral
más estricto.

**Efecto visual en la imagen segmentada:** el objeto de interés aparecería
**incompleto o "mordido"** — perdería partes de su silueta en las zonas donde
la intensidad estaba entre 100 y 134. Esto puede fragmentar el objeto en
varias piezas desconectadas o reducir su área real, lo cual arruina cálculos
posteriores como el área o el centroide (temas de la Sesión 6). En resumen:
un T demasiado alto "recorta" partes válidas del objeto.

---

## Taller de Laboratorio Final: Limpiando la Visión

Al correr `src/taller_lab_final_morfologia.py` sobre la imagen sintética de
bajo contraste (generada con `generar_imagen_prueba.py`), la umbralización
estática deja ruido de sal (puntos blancos sueltos) sobre el fondo oscuro.

- La **Apertura** (Erosión + Dilatación) eliminó ese ruido de sal sin afectar
  de forma permanente el tamaño del rectángulo y el círculo principales,
  porque la erosión inicial borra los puntos aislados (que no tienen vecinos
  blancos alrededor) y la dilatación posterior devuelve su tamaño original al
  objeto grande.
- El **Cierre** (Dilatación + Erosión) no ayuda tanto aquí porque su fortaleza
  es rellenar huecos *dentro* del objeto (ruido de pimienta), no eliminar
  puntos sueltos en el fondo; de hecho, en esta imagen tiende a mantener o
  aumentar levemente el ruido de sal, ya que la dilatación inicial puede
  "engordar" esos puntos antes de intentar erosionarlos.

**Conclusión:** para este caso particular (ruido de sal sobre fondo oscuro),
la **Apertura fue la operación morfológica más efectiva**, ya que su primer
paso (erosión) está diseñado justamente para eliminar elementos blancos
pequeños y aislados como el ruido generado.
