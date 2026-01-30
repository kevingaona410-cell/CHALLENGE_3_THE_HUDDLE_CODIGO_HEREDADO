class Mapa:
    # CONSTANTES DE TERRENO
    CAMINO, EDIFICIO, AGUA, BLOQUEADO = 0,1,2,3 
    # Define los tipos de terreno que pueden existir en el mapa
    posibles_terrenos = [CAMINO, EDIFICIO, AGUA, BLOQUEADO]

    def __init__(self, terreno, filas, columnas, INICIO, FIN, COSTOS=None):
        # Matriz que representa el terreno/mapa de la aplicación
        self.terreno = terreno
        self.filas = filas
        self.columnas = columnas
        # Variables para almacenar inicio y fin de ruta
        self.INICIO = INICIO
        self.FIN = FIN

        if COSTOS:
            self.COSTOS = COSTOS
        else:
            # el costo de movimiento por tipo de terreno
            self.COSTOS = { 
                self.CAMINO: 1,              # Costo bajo, fácil de transitar
                self.AGUA: 4,                # Costo alto, difícil de transitar
                self.BLOQUEADO: float("inf"),   # Imposible de transitar
                self.EDIFICIO: float("inf")     # Imposible de transitar
            }

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
            raise ValueError(f"Error logico: El mapa, no existe.")
            # Verifica que se hayan seleccionado puntos de inicio y fin
        if self.INICIO is None or self.FIN is None:
            raise ValueError(f"Error logico: Inicio o Fin no existe.")
        return True
        
    # Función para seleccionar/deseleccionar puntos de inicio y fin
    def seleccionar_celda(self,x,y):
        
        if not self.INICIO:      # Si no hay inicio marcado, la celda actual será el inicio
            self.INICIO = (x, y)
        elif not self.FIN:       # Si hay inicio pero no fin, la celda actual será el fin
            self.FIN = (x, y)
        elif self.INICIO == (x, y):  # Si ya hay inicio y se hace clic en él, lo deselecciona
            self.INICIO = None
        elif self.FIN == (x, y):     # Si ya hay fin y se hace clic en él, lo deselecciona
            self.FIN = None
        elif self.terreno[x][y] != self.CAMINO: # Si la celda no es transitable, muestra error
            raise ValueError("Invalido", "Solo puedes seleccionar caminos libres")
        else:                   # Si ambos están marcados, reemplaza el fin
            self.FIN = (x, y)
        return True
    # Función para alternar entre bloqueado y desbloqueado con clic derecho
    def bloquear_celda(self, x, y):
        # Si es camino o agua, lo convierte a edificio 
        if self.terreno[x][y] in (self.CAMINO, self.AGUA):
            self.terreno[x][y] = self.EDIFICIO
        # Si es bloqueado o edificio, lo convierte a camino
        elif self.terreno[x][y] in (self.BLOQUEADO, self.EDIFICIO):
            self.terreno[x][y] = self.CAMINO
