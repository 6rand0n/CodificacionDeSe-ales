# Info del Canvas 

MARGEN_SUPERIOR = 40

ANCHO = 1200
ALTO = 320
TAM_CELDA = 40

# Filtrado de entrada

def filtrar(event, text_widget):
    texto = text_widget.get("1.0", "end-1c")

    # Permitir teclas de edición
    if event.keysym in ("BackSpace", "Delete", "Left", "Right", "Up", "Down"):
        return

    # Limitar longitud a 20 caracteres
    if len(texto) >= 25:
        return "break"

    # Permitir solo 0 y 1
    if event.char not in ("0", "1"):
        return "break"
    
    # Centrado
    text_widget.tag_add("centrado", "1.0", "end")

# Funcion general para graficar

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

# Funciones de graficado auxiliares

def dibujar_cuadricula(canvas, tam_celda):

    nivel_1 = MARGEN_SUPERIOR
    nivel_0 = MARGEN_SUPERIOR + tam_celda * 3
    nivel_bajo = MARGEN_SUPERIOR + tam_celda * 6  # Nivel -1
    nivel_medio = (nivel_1 + nivel_0) // 2
    nivel_medioN = (nivel_bajo + nivel_0) // 2

    for x in range(0, ANCHO + 1, tam_celda):
        canvas.create_line(x, 0, x, ALTO, fill='lightgray')

    for y in range(0, ALTO + 1, tam_celda):
        canvas.create_line(0, y, ANCHO, y, fill='lightgray')

    canvas.create_line(0, nivel_medio, ANCHO, nivel_medio, fill='black', dash=(4, 2))

    canvas.create_text(15, nivel_1 - 10, text='1', anchor='w', fill='black')
    canvas.create_text(15, nivel_medio - 10, text='0.5', anchor='w', fill='black')
    canvas.create_text(15, nivel_0 - 10, text='0', anchor='w', fill='black')
    canvas.create_text(15, nivel_bajo - 10, text='-1', anchor='w', fill='black')
    canvas.create_text(15, nivel_medioN - 10, text='-0.5', anchor='w', fill='black')

def dibujar_nrzl(canvas, bits, tam_celda):
    # Codificación NRZ-L: ejemplo base
    nivel_1 = MARGEN_SUPERIOR
    nivel_0 = MARGEN_SUPERIOR + tam_celda * 3
    x = (ANCHO - len(bits) * tam_celda) // 2
    y_anterior = nivel_0 if bits[0] == '0' else nivel_1
    canvas.create_line(x, y_anterior, x + tam_celda, y_anterior, fill='blue', width=2)
    x += tam_celda

    for i in range(1, len(bits)):
        y_actual = nivel_0 if bits[i] == '0' else nivel_1
        if y_actual != y_anterior:
            canvas.create_line(x, y_anterior, x, y_actual, fill='blue', width=2)
        canvas.create_line(x, y_actual, x + tam_celda, y_actual, fill='blue', width=2)
        y_anterior = y_actual
        x += tam_celda

def dibujar_nrzi(canvas, bits, tam_celda):
    pass  # Implementación futura

def dibujar_ami(canvas, bits, tam_celda):
    pass  # Implementación futura

def dibujar_pseudoternario(canvas, bits, tam_celda):
    pass  # Implementación futura

def dibujar_manchester(canvas, bits, tam_celda):
    pass  # Implementación futura

def dibujar_diferencial(canvas, bits, tam_celda):
    pass  # Implementación futura