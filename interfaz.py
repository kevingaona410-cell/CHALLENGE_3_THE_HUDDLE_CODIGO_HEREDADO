
# Variable para almacenar el número de filas y columnas del mapa
filas_var = tk.IntVar()
columnas_var = tk.IntVar()


# COLORES de terreno
COLORES = {
    CAMINO: "#FFFFFF",      # Blanco
    EDIFICIO: "#424242",    # Gris oscuro
    AGUA: "#2196f3",        # Azul
    BLOQUEADO: "#FF0000"    # Rojo
}

# símbolo visual para cada terreno
SIMBOLOS = {
    CAMINO: ".",        # Punto para camino libre
    EDIFICIO: "X",      # X para edificio
    AGUA: "~",          # Tilde para agua
    BLOQUEADO: "#"      # Numeral para bloqueado
}

# CONFIGURACIÓN DE ESTILOS 
style = ttk.Style()
style.theme_use("clam")  
style.configure("TButton", font=("Segoe UI", 10), padding=6)
style.configure("TLabel", font=("Segoe UI", 10))

# CONTENEDOR SUPERIOR - Contiene los campos de entrada y botones
# Crea un frame para organizar los controles de entrada
frame_controles = tk.Frame(
    root,
    bg="#B0B0B0",
    padx=10,
    pady=10
)
frame_controles.pack(fill="x", padx=10, pady=10)

# Etiqueta para el campo de filas y columnas
tk.Label(
    frame_controles,
    text="Filas:",
    bg="#DBDBDB",
    fg="black"
).grid(row=0, column=0, padx=5)

tk.Label(
    frame_controles,
    text="Columnas:",
    bg="#DBDBDB",
    fg="black"
).grid(row=0, column=2, padx=5)

# Campo de entrada para el número de filas y columnas
ttk.Entry(
    frame_controles,
    textvariable=filas_var,
    width=5,
    justify="center"
).grid(row=0, column=1, padx=5)

ttk.Entry(
    frame_controles,
    textvariable=columnas_var,
    width=5,
    justify="center"
).grid(row=0, column=3, padx=5)

# Contenedor donde se dibuja la cuadrícula
# Crea un frame que contendrá la visualización del mapa
frame_mapa = tk.Frame(
    root,
    bg="#EDEDED",
    padx=10,
    pady=10
)
frame_mapa.pack(padx=10, pady=10)


# Función para visualizar el mapa en la interfaz gráfica
def dibujar_mundo():
    # Elimina todos los widgets previos del frame del mapa
    for widget in frame_mapa.winfo_children():
        widget.destroy()

    
    for i, fila in enumerate(terreno):
        for j, valor in enumerate(fila):
            # Determina el color y símbolo según si es inicio, fin u otro terreno
            if INICIO == (i,j):
                color = "#4cad50"  # Verde para inicio
                texto = "S"
            elif FIN == (i,j):
                color = "#FFA6A6"  # Rojo para fin
                texto = "E"
            else:
                color = COLORES.get( valor, "#000000")
                texto = SIMBOLOS.get( valor, "#000000")

            # Crea un label (celda) para representar el terreno
            lbl = tk.Label(
                frame_mapa,
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
            lbl.bind("<Button-1>", lambda e, x=i, y=j: seleccionar_celda(e, x, y))
            # Vincula clic derecho para bloquear/desbloquear celdas
            lbl.bind("<Button-3>", lambda e, x=i, y=j: bloquear_celda(x, y))


# BOTONES DE CONTROL - Interfaz para ejecutar las funciones principales
# Botón para generar un mundo aleatorio
ttk.Button(
    frame_controles,
    text="Generar Mundo",
    command=generar_mundo
).grid(row=0, column=4, padx=10)

# Botón para buscar la ruta más corta entre inicio y fin
ttk.Button(
    frame_controles, 
    text="Buscar Ruta",
    command=ruta_existe
).grid(row=0, column=5, padx=10)

# Botón para limpiar el camino y volver a mostrar solo el mapa
ttk.Button(
    frame_controles, 
    text="Limpiar Camino", 
    command=dibujar_mundo
).grid(row=1, column=5, padx=10)

resultado = mapa.seleccionar_celda(x,y)
if resultado == True:
    dibujar_mapa()
else: 
    messagebox.showwarning("Solo puedes seleccionar en los camino libres")