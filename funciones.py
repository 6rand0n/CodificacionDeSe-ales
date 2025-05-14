# Info del Canvas 
MARGEN_SUPERIOR = 40
ANCHO = 1200
ALTO = 320
TAM_CELDA = 40

# Niveles lógicos en píxeles
nivel_1 = MARGEN_SUPERIOR                          # Lógico 1
nivel_0 = MARGEN_SUPERIOR + TAM_CELDA * 3          # Lógico 0
nivel_bajo = MARGEN_SUPERIOR + TAM_CELDA * 6       # Lógico -1
nivel_medio = (nivel_1 + nivel_0) // 2             # Lógico 0.5
nivel_medioN = (nivel_0 + nivel_bajo) // 2         # Lógico -0.5

# Filtrado de entrada
def filtrar(event, text_widget):
    texto = text_widget.get("1.0", "end-1c")

    if event.keysym in ("BackSpace", "Delete", "Left", "Right", "Up", "Down"):
        return
    if len(texto) >= 25:
        return "break"
    if event.char not in ("0", "1"):
        return "break"
    
    text_widget.tag_add("centrado", "1.0", "end")

# Función general para graficar
def graficar(canvas, InputText, opcion):
    canvas.delete("all")
    bits = InputText.strip()

    if not bits:
        dibujar_cuadricula(canvas, TAM_CELDA)
        return

    dibujar_cuadricula(canvas, TAM_CELDA)

    if not all(c in '01' for c in bits):
        return

    match opcion:
        case 0:
            dibujar_nrzl(canvas, bits, TAM_CELDA)
        case 1:
            dibujar_nrzi(canvas, bits, TAM_CELDA)
        case 2:
            dibujar_ami(canvas, bits, TAM_CELDA)
        case 3:
            dibujar_pseudoternario(canvas, bits, TAM_CELDA)
        case 4:
            dibujar_manchester(canvas, bits, TAM_CELDA)
        case 5:
            dibujar_diferencial(canvas, bits, TAM_CELDA)

# Función para dibujar la cuadrícula
def dibujar_cuadricula(canvas, tam_celda):

    #Cuadricula
    for x in range(0, ANCHO + 1, tam_celda):
        canvas.create_line(x, 0, x, ALTO, fill='lightgray')
    for y in range(0, ALTO + 1, tam_celda):
        canvas.create_line(0, y, ANCHO, y, fill='lightgray')

    # Etiquetas de niveles
    canvas.create_text(15, nivel_1 - 10, text='1', anchor='w', fill='black')
    canvas.create_text(15, nivel_medio - 10, text='0.5', anchor='w', fill='black')
    canvas.create_text(15, nivel_0 - 10, text='0', anchor='w', fill='black')
    canvas.create_text(15, nivel_medioN - 10, text='-0.5', anchor='w', fill='black')
    canvas.create_text(15, nivel_bajo - 10, text='-1', anchor='w', fill='black')

# Señal NRZ-L
def dibujar_nrzl(canvas, bits, tam_celda):
    if not bits:
        return

    # Centrar
    ancho_senal = len(bits) * tam_celda
    x = (ANCHO - ancho_senal) // 2

    # Nivel inicial y primera línea
    nivel_anterior = nivel_0 if bits[0] == '0' else nivel_1
    canvas.create_line(x, nivel_anterior, x + tam_celda, nivel_anterior, fill='blue', width=2)

    x += tam_celda

    for i in range(1, len(bits)):
        # Primera linea
        nivel_actual = nivel_0 if bits[i] == '0' else nivel_1

        # Si el nivel cambia, dibujar la línea vertical
        if nivel_actual != nivel_anterior:
            canvas.create_line(x, nivel_anterior, x, nivel_actual, fill='blue', width=2)

        # Dibujar la línea final en X
        canvas.create_line(x, nivel_actual, x + tam_celda, nivel_actual, fill='blue', width=2)
        nivel_anterior = nivel_actual

        # Avanzar a la siguiente celda
        x += tam_celda

# Funciones vacías para implementar luego
def dibujar_nrzi(canvas, bits, tam_celda):
    pass

def dibujar_ami(canvas, bits, tam_celda):
    pass

def dibujar_pseudoternario(canvas, bits, tam_celda):
    pass

def dibujar_manchester(canvas, bits, tam_celda):
    pass

def dibujar_diferencial(canvas, bits, tam_celda):
    pass
