# Calculadora de Rutas - A* Pathfinding

Una aplicación interactiva en Python que implementa el algoritmo A* para encontrar el camino más corto en un mapa generado aleatoriamente.

## Descripción

Esta aplicación es un desafío de refactorización de código heredado (`CHALLENGE_3_THE_HUDDLE_CODIGO_HEREDADO`) que transforma un código monolítico en una arquitectura orientada a objetos con separación clara de responsabilidades.

## Características

- 🗺️ **Generación de mapas aleatorios** con diferentes tipos de terreno
- 🔍 **Algoritmo A*** optimizado con heurística de Manhattan
- 🎨 **Interfaz gráfica interactiva** con tkinter
- 📊 **Múltiples tipos de terreno**:
  - Camino (transitable, costo 1)
  - Edificio (bloqueado)
  - Agua (transitable, costo 4)
  - Bloqueado (intransitable)
- 🖱️ **Interacción con el ratón**:
  - Clic izquierdo: seleccionar inicio y fin
  - Clic derecho: alternar entre terrenos

## Estructura del Proyecto

```
CHALLENGE_3_THE_HUDDLE_CODIGO_HEREDADO/
├── main.py              # Orquestación principal y constantes
├── mapa.py              # Clase Mapa con lógica del mundo
├── interfaz.py          # Interfaz gráfica con tkinter
├── algorit_busq.py      # Clase Algoritmo_Busqueda con A*
└── README.md            # Este archivo
```

## Clases Principales

### `Mapa`
Gestiona el estado del mapa y las validaciones.
- `__init__()`: Inicializa el mapa con dimensiones y costos
- `movimiento_valido()`: Valida si una posición está dentro de límites
- `validar_estado()`: Verifica que inicio y fin existan
- `seleccionar_celda()`: Marca puntos de inicio/fin
- `bloquear_celda()`: Modifica el tipo de terreno

### `Algoritmo_Busqueda`
Implementa el algoritmo de búsqueda A*.
- `manhattan()`: Heurística de distancia Manhattan
- `camino_corto()`: Encuentra el camino más corto entre dos puntos
- `direcciones`: Define los movimientos posibles (4 direcciones)

## Uso

```bash
python main.py
```

1. Ingresa el número de filas y columnas
2. Haz clic en "Generar" para crear el mapa
3. Haz clic izquierdo en dos celdas para marcar inicio (S) y fin (E)
4. Haz clic en "Buscar Ruta" para encontrar el camino más corto
5. El camino se mostrará en amarillo

## Requisitos

- Python 3.7+
- tkinter (incluido con Python)

## Refactorización

Este proyecto demuestra:
- ✅ Separación de responsabilidades en múltiples módulos
- ✅ Conversión de funciones globales a métodos de clase
- ✅ Uso de herencia y encapsulación
- ✅ Mejora de la mantenibilidad y testabilidad del código

## Algoritmo A*

El algoritmo A* combina las ventajas de Dijkstra y la búsqueda codicioso mediante la función:

```
f(n) = g(n) + h(n)
```

Donde:
- `g(n)` = costo real desde el nodo inicial
- `h(n)` = heurística (Manhattan) estimada hacia el nodo final

## Autor

Kevin Santiago - Challenge 3 The Huddle (Código Heredado)
