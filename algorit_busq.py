# Heuristica de Manhattan - Estima la distancia entre dos puntos
def manhattan(a,b):
    h = abs(a[0]-b[0]) + abs(a[1]-b[1])
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# ALGORITMO DE BÚSQUEDA A* 
direcciones = [ # Define los movimientos posibles
    (-1, 0),    # Arriba
    (1, 0),     # Abajo
    (0, -1),    # Izquierda
    (0, 1),     # Derecha
]

# Función principal del algoritmo A* para encontrar el camino más corto
def camino_corto(terreno, INICIO, FIN):
    # Valida que los puntos de inicio y fin estén definidos
    if INICIO is None or FIN is None:
        messagebox.showwarning(
            "Advertencia",
            "Debe seleccionar un punto de inicio y fin"
        )
        return None

    # Obtiene las dimensiones del mapa
    filas = len(terreno)
    columnas = len(terreno[0]) if terreno else 0 

    # Inicializa matrices de control para el algoritmo A*
    visitados = [[False] * columnas for _ in range(filas)]          # Matriz para marcar celdas visitadas
    padre = [[None] * columnas for _ in range(filas)]               # Matriz para para reconstruir el camino
    g_cost = [[float('inf')] * columnas for _ in range(filas)]      # Matriz para el costo acumulado desde el inicio (g_cost)
    h_cost = [[0] * columnas for _ in range(filas)]                 # Matriz para el costo heurístico al fin 
    
    abiertos = []       # Cola de prioridad 
    g_cost[INICIO[0]][INICIO[1]] = 0    # El costo inicial en el inicio es 0
    f_inicio = manhattan(INICIO, FIN)   # Calcula el costo f 
    heapq.heappush(abiertos, (f_inicio, INICIO))    # Añade el nodo inicial a la cola de prioridad

    # Bucle principal del algoritmo 
    while abiertos: 
        f_actual, (x, y) = heapq.heappop(abiertos)
        # Si ya fue visitado, salta al siguiente
        if visitados[x][y]:
            continue
        # Marca el nodo actual como visitado
        visitados[x][y] = True

        if (x, y) == FIN:
            return reconstruir_camino(padre, INICIO, FIN)

        # Explora los vecinos del nodo actual
        for dx, dy in direcciones:
            nuevo_x = x + dx
            nuevo_y = y + dy

            # Verifica si el movimiento es válido y no ha sido visitado
            if movimiento_valido(nuevo_x, nuevo_y, filas, columnas) and not visitados[nuevo_x][nuevo_y]:
                costo = COSTOS[terreno[nuevo_x][nuevo_y]]
                if costo == float("inf"):
                    continue

                # Calcula el nuevo costo g
                nuevo_g = g_cost[x][y] + costo

                # Si encontró un camino más corto, actualiza
                if nuevo_g < g_cost[nuevo_x][nuevo_y]:
                    padre[nuevo_x][nuevo_y] = (x, y)
                    h = manhattan((nuevo_x, nuevo_y), FIN)
                    f = nuevo_g + h
                    g_cost[nuevo_x][nuevo_y] = nuevo_g
                    heapq.heappush(abiertos, (f, (nuevo_x, nuevo_y)))
    
    # Si la cola se vacía sin encontrar el fin, no hay camino
    return None  # No se encontró camino