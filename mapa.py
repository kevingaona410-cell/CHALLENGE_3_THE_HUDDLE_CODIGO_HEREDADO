class Mapa:
    # CONSTANTES DE TERRENO
    camino, edificio, agua, bloqueado = 0,1,2,3
    # Define los tipos de terreno que pueden existir en el mapa
    posibles_terrenos = [camino, edificio, agua, bloqueado]

    # el costo de movimiento por tipo de terreno
    costos = {
        camino: 1,              # Costo bajo, fácil de transitar
        agua: 4,                # Costo alto, difícil de transitar
        bloqueado: float("inf"),   # Imposible de transitar
        edificio: float("inf")     # Imposible de transitar
        }

    def __init__(self):
        # Matriz que representa el terreno/mapa de la aplicación
        self.filas = 0
        self.columnas = 0
        self.terreno = []
        # Variables para almacenar inicio y fin de ruta
        self.inicio = None
        self.fin = None

    #metodo de polimorfismo
    def generar_mundo(self, f, c):
        self.filas = f
        self.columnas = c
        self.inicio = None
        self.fin = None
        import random
        self.terreno = [
            [random.choice(self.posibles_terrenos) for _ in range(c)]
            for _ in range(f)
        ]


    # Función para validar si una posición está dentro de los límites del mapa
    def movimiento_valido(self, x, y):
        if x < 0 or x >= self.filas:     # Verifica si está fuera de límites en el eje X
            return False
        if y < 0 or y >= self.columnas:  # Verifica si está fuera de límites en el eje Y 
            return False 
        else:
            return True

    # Función para validar si existe una ruta entre inicio y fin
    def validar_estado(self):
        # Verifica que se haya generado un mapa
        if not self.terreno:
            return False
            # Verifica que se hayan seleccionado puntos de inicio y fin
        if self.inicio is None or self.fin is None:
            raise ValueError(f"Error logico: Inicio o Fin no existe.")
        return True
        
    # Función para seleccionar/deseleccionar puntos de inicio y fin
    def seleccionar_celda(self,x,y):
        
        if not self.inicio:      # Si no hay inicio marcado, la celda actual será el inicio
            self.inicio = (x, y)
        elif not self.fin:       # Si hay inicio pero no fin, la celda actual será el fin
            self.fin = (x, y)
        elif self.inicio == (x, y):  # Si ya hay inicio y se hace clic en él, lo deselecciona
            self.inicio = None
        elif self.fin == (x, y):     # Si ya hay fin y se hace clic en él, lo deselecciona
            self.fin = None
        elif self.terreno[x][y] != self.camino: # Si la celda no es transitable, muestra error
            return False
        else:                   # Si ambos están marcados, reemplaza el fin
            self.fin = (x, y)
        return True
    # Función para alternar entre bloqueado y desbloqueado con clic derecho
    def bloquear_celda(self, x, y):
        # Si es camino o agua, lo convierte a edificio 
        if self.terreno[x][y] in (self.camino, self.agua):
            self.terreno[x][y] = self.edificio
        # Si es bloqueado o edificio, lo convierte a camino
        elif self.terreno[x][y] in (self.bloqueado, self.edificio):
            self.terreno[x][y] = self.camino
        return True
