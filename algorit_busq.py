import heapq


class AlgoritmoBusqueda():

    direcciones = [ # Define los movimientos posibles
        (-1, 0),    # Arriba
        (1, 0),     # Abajo
        (0, -1),    # Izquierda
        (0, 1),     # Derecha
    ]

    def __init__(self, mapa):
        self.mapa = mapa

    # Heuristica de Manhattan - Estima la distancia entre dos puntos
    def manhattan(self, a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
         
    # Función principal del algoritmo A* para encontrar el camino más corto
    def a_estrella (self, INICIO, FIN):
        # Valida que los puntos de inicio y fin estén definidos
        self.mapa.validar_estado()
        # Obtiene las dimensiones del mapa
        
        filas = self.mapa.filas
        columnas = self.mapa.columnas
        terreno = self.mapa.terreno
        costos = self.mapa.COSTOS

        # Inicializa matrices de control para el algoritmo A*
        visitados = [[False] * columnas for _ in range(filas)]          # Matriz para marcar celdas visitadas
        padre = [[None] * columnas for _ in range(filas)]               # Matriz para para reconstruir el camino
        g_cost = [[float('inf')] * columnas for _ in range(filas)]      # Matriz para el costo acumulado desde el inicio (g_cost)
        
        abiertos = []       # Cola de prioridad 

        g_cost[INICIO[0]][INICIO[1]] = 0    # El costo inicial en el inicio es 0
        f_inicio = self.manhattan(INICIO, FIN)   # Calcula el costo f 
        heapq.heappush(abiertos, (f_inicio, INICIO))    # Añade el nodo inicial a la cola de prioridad

        # Bucle principal del algoritmo 
        while abiertos: 
            _, (x,y) = heapq.heappop(abiertos)

            # Si ya fue visitado, salta al siguiente
            if visitados[x][y]:
                continue
            # Marca el nodo actual como visitado
            visitados[x][y] = True

            if (x, y) == FIN:
                return padre

            # Explora los vecinos del nodo actual
            for dx, dy in self.direcciones:
                nx = x + dx
                ny = y + dy

                # Verifica si el movimiento es válido y no ha sido visitado
                if not self.mapa.movimiento_valido(nuevo_x, nuevo_y):
                    continue

                if visitados[nx][ny]:
                    continue

                if costo == float("inf")
                continue

                    # Calcula el nuevo costo g
                    nuevo_g = g_cost[x][y] + costo

                    # Si encontró un camino más corto, actualiza
                    if nuevo_g < g_cost[nx][ny]:
                        g_cost[nx][ny] = nuevo_g
                        padre[nx][ny] = (x, y)
                        f = nuevo_g + self.manhattan((nx, ny), fin)
                        heapq.heappush(abiertos, (f, (nx, ny)))

        # Si la cola se vacía sin encontrar el fin, no hay camino
        return None  # No se encontró camino