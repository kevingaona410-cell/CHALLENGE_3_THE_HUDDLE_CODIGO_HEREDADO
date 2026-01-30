
# IMPORTACIONES - Librerías necesarias para la aplicación
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import heapq  # Para el algoritmo de búsqueda A*
import random  # Para generar terrenos aleatorios

# CONFIGURACIÓN DE VENTANA PRINCIPAL
# Crea la ventana principal de la aplicación
root = tk.Tk()
root.title("Calculadora de Rutas")
root.geometry("500x500")
root.configure(bg="#DBDBDB")

# Función para generar un mapa aleatorio 
def generar_mundo():
    global terreno

    # Obtiene las dimensiones del mapa desde los campos de entrada
    filas = filas_var.get()
    columnas = columnas_var.get()

    # Valida las dimensiones 
    if filas <= 0 or columnas <= 0:
        messagebox.showerror(
            "Error",
            "Filas y columnas deben ser mayores que 0"
        )
        return

    # Genera una matriz con terrenos aleatorios
    terreno = [
        [random.choice(posibles_terrenos) for _ in range(columnas)]
        for _ in range(filas)
    ]
    dibujar_mundo()

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

if Mapa.validar_estado():
    # Calcula el camino más corto usando el algoritmo A*
    camino = buscador.camino_corto(mapa)
    interfaz.mostrar_camino(camino)
# BUCLE PRINCIPAL - Inicia la aplicación
root.mainloop()