# IMPORTACIONES - Librerías necesarias para la aplicación
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import heapq  # Para el algoritmo de búsqueda A*
import random  # Para generar terrenos aleatorios

class Mapa:
    def __init__(self):
        self.CAMINO = 0      
        self.EDIFICIO = 1    
        self.AGUA = 2        
        self.BLOQUEADO = 3   
        self.posibles_terrenos = [self.CAMINO, self.EDIFICIO, self.AGUA, self.BLOQUEADO]
        self.COLORES = {
            self.CAMINO: "#FFFFFF",      # Blanco
            self.EDIFICIO: "#424242",    # Gris oscuro
            self.AGUA: "#2196f3",        # Azul
            self.BLOQUEADO: "#FF0000"    # Rojo
        }
        self.COSTOS = { 
            self.CAMINO: 1,              # Costo bajo, fácil de transitar
            self.AGUA: 4,                # Costo alto, difícil de transitar
            self.BLOQUEADO: float("inf"),   # Imposible de transitar
            self.EDIFICIO: float("inf")     # Imposible de transitar
        }
        self.SIMBOLOS = {
            self.CAMINO: ".",        # Punto para camino libre
            self.EDIFICIO: "X",      # X para edificio
            self.AGUA: "~",          # Tilde para agua
            self.BLOQUEADO: "#"      # Numeral para bloqueado
        }
        self.terreno = []
        self.INICIO = None
        self.FIN = None
        self.interfaz = None

    def generar_mundo(self):
        filas = self.interfaz.filas_var.get()
        columnas = self.interfaz.columnas_var.get()
        if filas <= 0 or columnas <= 0:
            messagebox.showerror(
                "Error",
                "Filas y columnas deben ser mayores que 0"
            )
            return
        self.terreno = [
            [random.choice(self.posibles_terrenos) for _ in range(columnas)]
            for _ in range(filas)
        ]
        self.dibujar_mundo()

    def dibujar_mundo(self):
        for widget in self.interfaz.frame_mapa.winfo_children():
            widget.destroy()
        for i, fila in enumerate(self.terreno):
            for j, valor in enumerate(fila):
                if self.INICIO == (i,j):
                    color = "#4cad50"  # Verde para inicio
                    texto = "S"
                elif self.FIN == (i,j):
                    color = "#FFA6A6"  # Rojo para fin
                    texto = "E"
                else:
                    color = self.COLORES.get( valor, "#000000")
                    texto = self.SIMBOLOS.get( valor, "#000000")
                lbl = tk.Label(
                    self.interfaz.frame_mapa,
                    text= texto,
                    bg=color,
                    fg= "black",
                    font=("Consolas", 12, "bold"),
                    width=4,
                    height=2,
                    relief="ridge",
                    borderwidth=1
                )
                lbl.grid(row=i, column=j)
                lbl.bind("<Button-1>", lambda e, x=i, y=j: self.seleccionar_celda(e, x, y))
                lbl.bind("<Button-3>", lambda e, x=i, y=j: self.bloquear_celda(x, y))

    def seleccionar_celda(self, e, i, j):
        if self.INICIO is None:      # Si no hay inicio marcado, la celda actual será el inicio
            self.INICIO = (i, j)
        elif self.FIN is None:       # Si hay inicio pero no fin, la celda actual será el fin
            self.FIN = (i, j)
        elif self.INICIO == (i, j):  # Si ya hay inicio y se hace clic en él, lo deselecciona
            self.INICIO = None
        elif self.FIN == (i, j):     # Si ya hay fin y se hace clic en él, lo deselecciona
            self.FIN = None
        elif self.terreno[i][j] != self.CAMINO: # Si la celda no es transitable, muestra error
            messagebox.showwarning("Invalid", "Solo puedes seleccionar caminos libres")
            return
        else:                   # Si ambos están marcados, reemplaza el fin
            self.FIN = (i, j)
        self.dibujar_mundo()

    def bloquear_celda(self, x, y):
        if self.terreno[x][y] in (self.CAMINO, self.AGUA):
            self.terreno[x][y] = self.EDIFICIO
        elif self.terreno[x][y] in (self.BLOQUEADO, self.EDIFICIO):
            self.terreno[x][y] = self.CAMINO
        self.dibujar_mundo()

class InterfazTkinter:
    def __init__(self, mapa, algoritmo):
        self.mapa = mapa
        self.algoritmo = algoritmo
        self.root = tk.Tk()
        self.root.title("Calculadora de Rutas")
        self.root.geometry("500x500")
        self.root.configure(bg="#DBDBDB")
        self.style = ttk.Style()
        self.style.theme_use("clam")  
        self.style.configure("TButton", font=("Segoe UI", 10), padding=6)
        self.style.configure("TLabel", font=("Segoe UI", 10))
        self.filas_var = tk.IntVar()
        self.columnas_var = tk.IntVar()
        self.frame_controles = tk.Frame(
            self.root,
            bg="#B0B0B0",
            padx=10,
            pady=10
        )
        self.frame_controles.pack(fill="x", padx=10, pady=10)
        tk.Label(
            self.frame_controles,
            text="Filas:",
            bg="#DBDBDB",
            fg="black"
        ).grid(row=0, column=0, padx=5)
        tk.Label(
            self.frame_controles,
            text="Columnas:",
            bg="#DBDBDB",
            fg="black"
        ).grid(row=0, column=2, padx=5)
        ttk.Entry(
            self.frame_controles,
            textvariable=self.filas_var,
            width=5,
            justify="center"
        ).grid(row=0, column=1, padx=5)
        ttk.Entry(
            self.frame_controles,
            textvariable=self.columnas_var,
            width=5,
            justify="center"
        ).grid(row=0, column=3, padx=5)
        self.frame_mapa = tk.Frame(
            self.root,
            bg="#EDEDED",
            padx=10,
            pady=10
        )
        self.frame_mapa.pack(padx=10, pady=10)
        ttk.Button(
            self.frame_controles,
            text="Generar Mundo",
            command=self.mapa.generar_mundo
        ).grid(row=0, column=4, padx=10)
        ttk.Button(
            self.frame_controles, 
            text="Buscar Ruta",
            command=self.ruta_existe
        ).grid(row=0, column=5, padx=10)
        ttk.Button(
            self.frame_controles, 
            text="Limpiar Camino", 
            command=self.mapa.dibujar_mundo
        ).grid(row=1, column=5, padx=10)

    def ruta_existe(self):
        if not self.mapa.terreno:
            messagebox.showwarning("Error", "Primero genera el mundo")
            return
        if self.mapa.INICIO is None or self.mapa.FIN is None:
            messagebox.showwarning("Advertencia", "Selecciona inicio y fin primero")
            return
        camino = self.algoritmo.camino_corto(self.mapa.terreno, self.mapa.INICIO, self.mapa.FIN, self.mapa.COSTOS)
        self.mostrar_camino(camino)

    def mostrar_camino(self, camino):
        self.mapa.dibujar_mundo()
        if camino is None: 
            messagebox.showwarning("Error", "No se encontro un camino ")
            return
        for i, j in camino [1:-1]:
            lbl = tk.Label(
                self.frame_mapa,
                text= "*",
                fg= "black",
                font=("Consolas", 12, "bold"),
                bg="#ffeb3b",
                width=4,
                height=2,
                relief="ridge",
                borderwidth=1
            )
            lbl.grid(row=i, column=j)
            lbl.bind("<Button-1>", lambda e, x=i, y=j: self.mapa.seleccionar_celda(e, x, y))

    def iniciar(self):
        self.root.mainloop()

class AlgoritmoBusqueda:
    def __init__(self):
        self.direcciones = [
            (-1, 0),    # Arriba
            (1, 0),     # Abajo
            (0, -1),    # Izquierda
            (0, 1),     # Derecha
        ]

    def manhattan(self, a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    def movimiento_valido(self, x, y, filas, columnas):
        if x < 0 or x >= filas:     # Verifica si está fuera de límites en el eje X
            return False
        if y < 0 or y >= columnas:  # Verifica si está fuera de límites en el eje Y 
            return False 
        return True

    def camino_corto(self, terreno, INICIO, FIN, COSTOS):
        if INICIO is None or FIN is None:
            messagebox.showwarning(
                "Advertencia",
                "Debe seleccionar un punto de inicio y fin"
            )
            return None
        filas = len(terreno)
        columnas = len(terreno[0]) if terreno else 0 
        visitados = [[False] * columnas for _ in range(filas)]
        padre = [[None] * columnas for _ in range(filas)]
        g_cost = [[float('inf')] * columnas for _ in range(filas)]
        abiertos = []
        g_cost[INICIO[0]][INICIO[1]] = 0
        f_inicio = self.manhattan(INICIO, FIN)
        heapq.heappush(abiertos, (f_inicio, INICIO))
        while abiertos:
            f_actual, (x, y) = heapq.heappop(abiertos)
            if visitados[x][y]:
                continue
            visitados[x][y] = True
            if (x, y) == FIN:
                return self.reconstruir_camino(padre, INICIO, FIN)
            for dx, dy in self.direcciones:
                nuevo_x = x + dx
                nuevo_y = y + dy
                if self.movimiento_valido(nuevo_x, nuevo_y, filas, columnas) and not visitados[nuevo_x][nuevo_y]:
                    costo = COSTOS[terreno[nuevo_x][nuevo_y]]
                    if costo == float("inf"):
                        continue
                    nuevo_g = g_cost[x][y] + costo
                    if nuevo_g < g_cost[nuevo_x][nuevo_y]:
                        padre[nuevo_x][nuevo_y] = (x, y)
                        h = self.manhattan((nuevo_x, nuevo_y), FIN)
                        f = nuevo_g + h
                        g_cost[nuevo_x][nuevo_y] = nuevo_g
                        heapq.heappush(abiertos, (f, (nuevo_x, nuevo_y)))
        return None

    def reconstruir_camino(self, padre, INICIO, FIN):
        camino = []
        actual = FIN
        while actual is not None:
            camino.append(actual)
            if actual == INICIO:
                camino.reverse()
                return camino
            actual = padre[actual[0]][actual[1]]
        return None

# MAIN
mapa = Mapa()
algoritmo = AlgoritmoBusqueda()
interfaz = InterfazTkinter(mapa, algoritmo)
mapa.interfaz = interfaz
interfaz.iniciar()
