# Sistema Experto de Recomendación de Vehículos

Sistema experto en Python que recomienda los 3 vehículos más adecuados para un usuario, a partir de un cuestionario guiado y un motor de inferencia basado en reglas ponderadas (forward chaining).

## Índice

- [¿Qué es este sistema?](#qué-es-este-sistema)
- [Arquitectura](#arquitectura)
- [Cómo funciona el motor](#cómo-funciona-el-motor)
- [Base de reglas y pesos](#base-de-reglas-y-pesos)
- [Requisitos e instalación](#requisitos-e-instalación)
- [Cómo ejecutarlo](#cómo-ejecutarlo)
- [Ejemplo de uso](#ejemplo-de-uso)
- [Estructura del código](#estructura-del-código)
- [Base de conocimiento](#base-de-conocimiento)

## ¿Qué es este sistema?

Es un **sistema experto basado en reglas**: en vez de filtrar vehículos con condiciones rígidas (todo o nada), le asigna a **cada** vehículo de la base de conocimiento un puntaje de 0 a 100 según qué tan bien se ajusta a las respuestas del usuario, y recomienda los 3 con mayor puntaje. Un vehículo que cumple 8 de 9 criterios sigue siendo una buena opción, no se descarta por fallar en uno solo — así es como razonaría un asesor con experiencia.

El flujo completo sigue el mapa de nodos del proyecto: preguntas guiadas → activación de reglas → cálculo de puntaje → orden descendente → Top 3 → explicación del resultado.

## Arquitectura

```
Usuario
  │
  ▼
Cuestionario guiado (9 preguntas)
  │
  ▼
Respuestas del usuario ──────┐
                              │
Base de hechos (VEHICULOS) ──┼──▶  Motor de inferencia
  67 vehículos                │     (aplica 9 reglas a cada vehículo)
                              │
                              ▼
                     Puntaje 0-100 por vehículo
                              │
                              ▼
                  Ordenar de mayor a menor
                              │
                              ▼
                   Top 3 + explicación por regla
                              │
                              ▼
              ¿Otra recomendación? ── Sí ──▶ (vuelve al cuestionario)
                              │
                              No
                              ▼
                          Despedida
```

## Cómo funciona el motor

Nada está precalculado. Los vehículos solo tienen **características fijas** (marca, presupuesto, tecnología, terreno, etc.); el puntaje no existe hasta que hay respuestas de un usuario para compararlas contra él:

```
vehículo (características fijas) + respuestas (varían cada corrida) → puntaje (se calcula al vuelo)
```

En cada corrida, el motor:

1. Recorre los 67 vehículos de `VEHICULOS`, uno por uno.
2. Le aplica las 9 reglas SI-ENTONCES a cada uno, comparando sus características contra las respuestas del usuario.
3. Suma lo que ganó en cada regla → puntaje bruto.
4. Normaliza ese puntaje sobre el peso total realmente aplicable (ver nota sobre la marca preferida más abajo) → puntaje final 0-100.
5. Ordena los 67 vehículos de mayor a menor puntaje.
6. Muestra los 3 primeros, cada uno con el detalle de qué reglas le sumaron puntos y por qué.

Cada regla no evalúa solo "coincide / no coincide": varias otorgan **puntaje parcial** cuando el vehículo se acerca a lo pedido sin coincidir exactamente (por ejemplo, un rango de presupuesto vecino, o una tecnología "prima" como Mild Hybrid frente a Híbrido). Esto es lo que le da matices al motor frente a un simple filtro binario.

## Base de reglas y pesos

Los 9 criterios suman 100 puntos en total:

| # | Criterio | Peso máximo | Condición (SI) | Puntaje parcial (si no hay match exacto) |
|---|---|---|---|---|
| R1 | Presupuesto | 20 | Rango del usuario == rango del vehículo | Mitad (10) si el rango es adyacente en la escala |
| R2 | Tipo de vehículo | 15 | Tipo deseado == tipo del vehículo | — (0 si no coincide) |
| R3 | Propósito principal | 15 | Propósito deseado == propósito principal del vehículo | Mitad (7.5) si coincide con el propósito secundario del vehículo |
| R4 | Tecnología | 15 | Tecnología deseada == tecnología del vehículo | Mitad (7.5) si es una tecnología "compatible" (ej. Híbrido ↔ Mild Hybrid) |
| R5 | Terreno | 10 | Terreno deseado == terreno del vehículo | 60% (6) si el vehículo es "Mixto" y cubre lo pedido; 40% (4) si es al revés |
| R6 | Pasajeros | 5 | Capacidad del vehículo ≥ pasajeros requeridos | — (0 si no alcanza) |
| R7 | Transmisión | 5 | Transmisión deseada == transmisión del vehículo | — (0 si no coincide) |
| R8 | Consumo | 10 | Nivel deseado == nivel del vehículo | Mitad (5) si está un escalón de distancia en la escala Muy bajo → Bajo → Medio → Alto |
| R9 | Marca preferida | 5 | Usuario indicó marca Y coincide | Si el usuario no tiene preferencia, la regla **no aplica**: sus 5 puntos se excluyen del total y el puntaje se normaliza sobre 95 en vez de 100, para no penalizar a quien no respondió esa pregunta |



El programa es autocontenido: la base de los 67 vehículos está embebida en el propio código (lista `VEHICULOS`), así que no depende de ningún archivo externo (CSV, Excel, base de datos).

El programa hace preguntas por consola, una a la vez, mostrando las opciones numeradas. Al final de cada recomendación, pregunta si quieres otra (vuelve a empezar el cuestionario) o si prefieres salir.

## Ejemplo de uso

```
¿Cuál es su presupuesto?
  1. 50M-60M
  ...
  6. 100M-120M
Seleccione una opción (número): 6

...(resto de preguntas)...

============================================================
TOP 3 RECOMENDACIONES
============================================================

#1 - Suzuki Vitara Hybrid  |  Puntaje: 89.5/100
    Precio aprox: $132.99M  |  SUV | Híbrido | Automática
    Explicación:
      - Presupuesto en rango cercano (120M-140M)  (+10.0 pts)
      - Tipo de vehículo coincide (SUV)  (+15 pts)
      - Propósito principal coincide (Familiar)  (+15 pts)
      - Tecnología coincide (Híbrido)  (+15 pts)
      - Terreno coincide (Mixto)  (+10 pts)
      - Capacidad suficiente (5 puestos)  (+5 pts)
      - Transmisión coincide (Automática)  (+5 pts)
      - Consumo coincide (Muy bajo)  (+10 pts)

¿Quieres que te recomiende otro vehículo?
  1. Sí
  2. No
Seleccione una opción (número):
```

## Estructura del código

`Motor.py` está organizado en 7 secciones numeradas:

| Sección | Contenido |
|---|---|
| 1 | Base de hechos: lista `VEHICULOS` y `cargar_vehiculos()` |
| 2 | Base de pesos: diccionario `PESOS` y tablas de orden/compatibilidad usadas por las reglas |
| 3 | Las 9 reglas SI-ENTONCES (`regla_presupuesto`, `regla_tipo_vehiculo`, ...) |
| 4 | Motor de inferencia: `calcular_puntaje()` y `motor_inferencia()` |
| 5 | Interfaz de preguntas: `preguntar()` y `recolectar_respuestas()` |
| 6 | Salida: `mostrar_resultado()`, con el Top 3 y su explicación |
| 7 | Punto de entrada: bucle principal con la opción de repetir o salir |

## Base de conocimiento

67 vehículos, cada uno con: marca, modelo, precio, rango de presupuesto, propósito principal y secundario, tecnología, terreno, número de pasajeros, tipo de vehículo, transmisión y nivel de consumo. Cubren rangos de presupuesto desde 50M hasta 160M+ COP, y todas las tecnologías (Combustión, Híbrido, Mild Hybrid, Híbrido Enchufable, Eléctrico).