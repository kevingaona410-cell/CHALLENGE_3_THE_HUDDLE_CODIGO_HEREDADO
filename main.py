from mapa import Mapa
from interfaz import Interfaz
from algorit_busq import AlgoritmoBusqueda
import tkinter as tk
from tkinter import messagebox

class Main:

    # CONFIGURACIÓN DE VENTANA PRINCIPAL
    # Crea la ventana principal de la aplicación
    def __init__(self):
        self.root = tk.Tk()
        self.mapa = Mapa()
        self.busqueda = AlgoritmoBusqueda(mapa= self.mapa)
        self.interfaz = Interfaz(root= self.root, mapa= self.mapa, main= self)
        self.root.title("Calculadora de Rutas")
        self.root.geometry("500x500")
        self.root.configure(bg="#DBDBDB")

    # Función para generar un mapa aleatorio
    def generar_mundo(self):
        # Obtenemos los valores de las variables de la interfaz
        f = self.interfaz.filas_var.get()
        c = self.interfaz.columnas_var.get()

        if f <= 0 or c <= 0:
            messagebox.showerror("Error", "Filas y columnas deben ser mayores que 0")
            return
        self.mapa.generar_mundo(f, c)

        # Le decimos a la interfaz que se actualice
        self.interfaz.dibujar_mundo()

    # Función para visualizar el camino encontrado sobre el mapa
    def mostrar_camino(self, camino):
        self.interfaz.dibujar_mundo()  # Redibuja el mapa
        # Verifica si se encontró un camino válido
        if camino is None:
            messagebox.showwarning("Error", "No se encontro un camino 🥲")
            return

        # Marca cada celda del camino (excepto inicio y fin) con un asterisco
        for i, j in camino [1:-1]:
            lbl = tk.Label(
                    self.interfaz.frame_mapa,
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

    # Función para reconstruir el camino desde el fin hasta el inicio usando la matriz de padres
    def reconstruir_camino(self, padre):
        # Lista para almacenar el camino reconstruido
        camino = []
        actual = self.mapa.fin

        # Sigue los padres hasta llegar al inicio
        while actual is not None:
            camino.append(actual)
            # Si llegó al inicio, invierte el camino y lo retorna
            if actual == self.mapa.inicio:
                camino.reverse()
                return camino
            actual = padre[actual[0]][actual[1]]
        return  None

    def buscar(self):
        if self.mapa.validar_estado():
            # Obtenemos la opción del selector
            algoritmo = self.interfaz.metodo_var.get()
            
            padre_map = None # Variable para guardar el resultado
            
            if algoritmo == "A*":
                padre_map = self.busqueda.a_estrella()
            elif algoritmo == "Dijkstra":
                padre_map = self.busqueda.dijkstra()
            elif algoritmo == "BFS":
                padre_map = self.busqueda.bfs()

            # Si el algoritmo devolvió la matriz de padres, reconstruimos
            if padre_map:
                camino = self.reconstruir_camino(padre_map)
                self.mostrar_camino(camino)
            else:
                messagebox.showwarning("Sin ruta", "No se encontró un camino posible.") 
    
    # --- AQUÍ TERMINA LA CLASE ---
# BUCLE PRINCIPAL - Inicia la aplicación
if __name__ == "__main__":
    app = Main()
    app.interfaz.configuracion_principal()  # Esto construye los botones
    app.interfaz.dibujar_mundo()  # Dibuja el mapa inicial si lo hay
    app.root.mainloop()  # Llama al mainloop