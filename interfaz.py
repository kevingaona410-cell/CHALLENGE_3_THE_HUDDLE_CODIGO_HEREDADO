
# CONFIGURACIÓN DE VENTANA PRINCIPAL
# Crea la ventana principal de la aplicación
root = tk.Tk()
root.title("Calculadora de Rutas")
root.geometry("500x500")
root.configure(bg="#DBDBDB")

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

