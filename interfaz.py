# IMPORTACIONES - Librerías necesarias para la aplicación

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Interfaz:

    
    def __init__(self, root, mapa, main):
        # Variable para almacenar el número de filas y columnas del mapa
        self.main = main
        self.filas_var = tk.IntVar(value= mapa.filas)
        self.columnas_var = tk.IntVar(value = mapa.columnas)
        self.root = root
        self.mapa = mapa
        self.frame_mapa = None
        self.frame_controles = None

        # COLORES de terreno
        self.colores = {
            self.mapa.camino: "#FFFFFF",      # Blanco
            self.mapa.edificio: "#424242",    # Gris oscuro
            self.mapa.agua: "#2196f3",        # Azul
            self.mapa.bloqueado: "#FF0000"    # Rojo
        }

        # símbolo visual para cada terreno
        self.simbolos = {
            self.mapa.camino: ".",        # Punto para camino libre
            self.mapa.edificio: "X",      # X para edificio
            self.mapa.agua: "~",          # Tilde para agua
            self.mapa.bloqueado: "#"      # Numeral para bloqueado
        }
        self.metodo_var = tk.StringVar(value="A*")
    
    def configuracion_principal(self): # CONFIGURACIÓN DE ESTILOS 
        style = ttk.Style()
        style.theme_use("clam")  
        style.configure("TButton", font=("Segoe UI", 10), padding=6)
        style.configure("TLabel", font=("Segoe UI", 10))

        # CONTENEDOR SUPERIOR - Contiene los campos de entrada y botones
        # Crea un frame para organizar los controles de entrada
        self.frame_controles = tk.Frame(
            self.root,
            bg="#B0B0B0",
            padx=10,
            pady=10
        )
        self.frame_controles.pack(fill="x", padx=10, pady=10)

        # Etiqueta para el campo de filas y columnas
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

        # Campo de entrada para el número de filas y columnas
        ttk.Entry(
            self.frame_controles,
            textvariable= self.filas_var,
            width=5,
            justify="center"
        ).grid(row=0, column=1, padx=5)

        ttk.Entry(
            self.frame_controles,
            textvariable=self.columnas_var,
            width=5,
            justify="center"
        ).grid(row=0, column=3, padx=5)

        # Contenedor donde se dibuja la cuadrícula
        # Crea un frame que contendrá la visualización del mapa
        self.frame_mapa = tk.Frame(
            self.root,
            bg="#EDEDED",
            padx=10,
            pady=10
        )
        self.frame_mapa.pack(padx=10, pady=10)

        tk.Label(
        self.frame_controles,
        text="Algoritmo:",
        bg="#DBDBDB"
        ).grid(row=1, column=0, padx=5)

        selector = ttk.OptionMenu(
        self.frame_controles,
        self.metodo_var,
        "A*",      # Opción por defecto
        "A*",      # Lista de opciones...
        "BFS",
        "Dijkstra"
        )
        selector.grid(row=1, column=1, columnspan=2, padx=5, sticky="ew")   

        # BOTONES DE CONTROL - Interfaz para ejecutar las funciones principales
        # Botón para generar un mundo aleatorio
        ttk.Button(
            self.frame_controles,
            text="Generar Mundo",
            command=self.main.generar_mundo
        ).grid(row=0, column=4, padx=10)

        # Botón para buscar la ruta más corta entre inicio y fin
        ttk.Button(
            self.frame_controles, 
            text="Buscar Ruta",
            command=self.main.buscar
        ).grid(row=0, column=5, padx=10)

        # Botón para limpiar el camino y volver a mostrar solo el mapa
        ttk.Button(
            self.frame_controles, 
            text="Limpiar Camino", 
            command=self.dibujar_mundo
        ).grid(row=1, column=5, padx=10)

    # Función para visualizar el mapa en la interfaz gráfica
    def dibujar_mundo(self):
        # Elimina todos los widgets previos del frame del mapa
        for widget in self.frame_mapa.winfo_children():
            widget.destroy()

        
        for i, fila in enumerate(self.mapa.terreno):
            for j, valor in enumerate(fila):
                # Determina el color y símbolo según si es inicio, fin u otro terreno
                if self.mapa.inicio == (i,j):
                    color = "#4cad50"  # Verde para inicio
                    texto = "S"
                elif self.mapa.fin == (i,j):
                    color = "#FFA6A6"  # Rojo para fin
                    texto = "E"
                else:
                    color = self.colores.get( valor, "#000000")
                    texto = self.simbolos.get( valor, "#000000")

                # Crea un label (celda) para representar el terreno
                lbl = tk.Label(
                    self.frame_mapa,
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
                # Vincula clic izquierdo para seleccionar inicio/fin
                lbl.bind("<Button-1>", lambda e, x=i, y=j: self.clic(e, x, y))
                # Vincula clic derecho para bloquear/desbloquear celdas
                # Dentro de dibujar_mundo en interfaz.py
                lbl.bind("<Button-3>", lambda e, x=i, y=j: self.clic_derecho(e, x, y))

    def clic(self, _, x, y):
        resultado = self.mapa.seleccionar_celda(x, y)
        if resultado:
            self.dibujar_mundo()
        else:
            messagebox.showwarning("Aviso", "Solo puedes seleccionar en caminos libres")


    def clic_derecho(self, _, x, y):
        #  pedimos al mapa que cambie el estado de la celda
        self.mapa.bloquear_celda(x, y)

        self.dibujar_mundo()