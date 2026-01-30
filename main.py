
# IMPORTACIONES - Librerías necesarias para la aplicación
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import heapq  # Para el algoritmo de búsqueda A*
import random  # Para generar terrenos aleatorios

# CONSTANTES DE TERRENO
# Define los tipos de terreno que pueden existir en el mapa
CAMINO = 0      
EDIFICIO = 1    
AGUA = 2        
BLOQUEADO = 3   

# Variables para almacenar inicio y fin de ruta
INICIO = None
FIN = None

posibles_terrenos = [CAMINO, EDIFICIO, AGUA, BLOQUEADO]


# el costo de movimiento por tipo de terreno
COSTOS = { 
    CAMINO: 1,              # Costo bajo, fácil de transitar
    AGUA: 4,                # Costo alto, difícil de transitar
    BLOQUEADO: float("inf"),   # Imposible de transitar
    EDIFICIO: float("inf")     # Imposible de transitar
}

# Variable para almacenar el número de filas y columnas del mapa
filas_var = tk.IntVar()
columnas_var = tk.IntVar()

# Función para visualizar el camino encontrado sobre el mapa
def mostrar_camino(camino):
    dibujar_mundo()  # Redibuja el mapa
    # Verifica si se encontró un camino válido
    if camino is None: 
        messagebox.showwarning("Error", "No se encontro un camino 🥲")
        return

    # Marca cada celda del camino (excepto inicio y fin) con un asterisco
    for i, j in camino [1:-1]:
        lbl = tk.Label(
                frame_mapa,
                text= "*",
                fg= "black",
                font=("Consolas", 12, "bold"),
                bg="#ffeb3b",  # Amarillo para resaltar el camino
                width=4,
                height=2,
                relief="ridge",
                borderwidth=1
            )
        lbl.grid(row=i, column=j)
        # Permite hacer clic en las celdas del camino
        lbl.bind("<Button-1>", lambda e, x=i, y=j: seleccionar_celda(e, x, y))



# Función para reconstruir el camino desde el fin hasta el inicio usando la matriz de padres
def reconstruir_camino(padre, INICIO, FIN):
    # Lista para almacenar el camino reconstruido
    camino = []
    actual = FIN

    # Sigue los padres hasta llegar al inicio
    while actual is not None:
        camino.append(actual)
        # Si llegó al inicio, invierte el camino y lo retorna
        if actual == INICIO:
            camino.reverse()
            return camino
        actual = padre[actual[0]][actual[1]]

    # si no se llegó al inicio, retorna None
    return None

# BUCLE PRINCIPAL - Inicia la aplicación
root.mainloop()