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

# Dibujar flechas

def flecha(canvas, x, y, i):
    canvas.create_line(x-10, y+10, x, y, fill='blue', width=2)
    canvas.create_line(x-10, y-10, x, y, fill='blue', width=2)
    canvas.create_text(x-(TAM_CELDA)/2, nivel_1-(TAM_CELDA)/2, text=i, anchor='w', fill='black')

# Señal NRZ-L
def dibujar_nrzl(canvas, bits, tam_celda):
    if not bits:
        return

    # Centrar
    ancho_senal = len(bits) * tam_celda
    x = (ANCHO - ancho_senal) // 2

    # Nivel inicial y primera línea
    nivel_anterior = nivel_0 if bits[0] == '0' else nivel_1

    for i in range(0, len(bits)):
        # Primera linea
        nivel_actual = nivel_0 if bits[i] == '0' else nivel_1

        # Si el nivel cambia, dibujar la línea vertical
        if nivel_actual != nivel_anterior:
            canvas.create_line(x, nivel_anterior, x, nivel_actual, fill='blue', width=2)

        # Dibujar la línea final en X
        canvas.create_line(x, nivel_actual, x + tam_celda, nivel_actual, fill='blue', width=2)
        
        # Dibujar flecha
        flecha(canvas, x + tam_celda, nivel_actual, bits[i])
        
        nivel_anterior = nivel_actual

        # Avanzar a la siguiente celda
        x += tam_celda

# Funciones vacías para implementar luego
def dibujar_nrzi(canvas, bits, tam_celda):
    if not bits:
        return
    
    polaridad = 1

    # Centrar
    ancho_senal = len(bits) * tam_celda
    x = (ANCHO - ancho_senal) // 2

    # Nivel inicial y primera línea
    nivel_anterior = nivel_0 if bits[0] == '0' else nivel_1

    for i in range(0, len(bits)):
        # Primera linea

        if bits[i] == '1':
            if polaridad == 1:
                nivel_actual = nivel_1
            else:
                nivel_actual = nivel_0
            polaridad *= -1
        else:
            nivel_actual = nivel_anterior

        # Si el nivel cambia, dibujar la línea vertical
        if nivel_actual != nivel_anterior:
            canvas.create_line(x, nivel_anterior, x, nivel_actual, fill='blue', width=2)

        # Dibujar la línea final en X
        canvas.create_line(x, nivel_actual, x + tam_celda, nivel_actual, fill='blue', width=2)
        
        # Dibujar flecha
        flecha(canvas, x + tam_celda, nivel_actual, bits[i])
        
        nivel_anterior = nivel_actual

        # Avanzar a la siguiente celda
        x += tam_celda

def dibujar_ami(canvas, bits, tam_celda):
    polaridad = 1

    if not bits:
        return

    # Centrar
    ancho_senal = len(bits) * tam_celda
    x = (ANCHO - ancho_senal) // 2

    # Nivel inicial y primera línea
    nivel_anterior = nivel_0 if bits[0] == '0' else nivel_1

    for i in range(0, len(bits)):
        # Primera linea
        if bits[i] == '1':
            if polaridad == 1:
                nivel_actual = nivel_1
            else:
                nivel_actual = nivel_bajo
            polaridad *= -1
        else:
            nivel_actual = nivel_0

        # Si el nivel cambia, dibujar la línea vertical
        if nivel_actual != nivel_anterior:
            canvas.create_line(x, nivel_anterior, x, nivel_actual, fill='blue', width=2)

        # Dibujar la línea final en X
        canvas.create_line(x, nivel_actual, x + tam_celda, nivel_actual, fill='blue', width=2)
        
        # Dibujar flecha
        flecha(canvas, x + tam_celda, nivel_actual, bits[i])
        
        nivel_anterior = nivel_actual

        # Avanzar a la siguiente celda
        x += tam_celda

def dibujar_pseudoternario(canvas, bits, tam_celda):
    polaridad = 1

    if not bits:
        return

    # Centrar
    ancho_senal = len(bits) * tam_celda
    x = (ANCHO - ancho_senal) // 2

    # Nivel inicial
    nivel_anterior = nivel_1 if bits[0] == '0' else nivel_0

    for i in range(0, len(bits)):
        # Primera linea
        if bits[i] == '0':
            if polaridad == 1:
                nivel_actual = nivel_1
            else:
                nivel_actual = nivel_bajo
            polaridad *= -1
        else:
            nivel_actual = nivel_0

        # Si el nivel cambia, dibujar la línea vertical
        if nivel_actual != nivel_anterior:
            canvas.create_line(x, nivel_anterior, x, nivel_actual, fill='blue', width=2)

        # Dibujar la línea final en X
        canvas.create_line(x, nivel_actual, x + tam_celda, nivel_actual, fill='blue', width=2)
        
        # Dibujar flecha
        flecha(canvas, x + tam_celda, nivel_actual, bits[i])
        
        nivel_anterior = nivel_actual

        # Avanzar a la siguiente celda
        x += tam_celda

def dibujar_manchester(canvas, bits, tam_celda):
    if not bits:
        return

    # Centrar
    ancho_senal = len(bits) * tam_celda
    x = (ANCHO - ancho_senal) // 2

    # Nivel inicial 
    nivel_anterior = nivel_0 if bits[0] == '1' else nivel_1
    nivel_actual = nivel_0 if bits[0] == '0' else nivel_1

    for i in range(0, len(bits)):
        nivel_actual = nivel_0 if bits[i] == '0' else nivel_1

        # Si el nivel cambia, dibujar la línea vertical
        if nivel_actual == nivel_anterior:
            nivel_anterior = nivel_1 if nivel_anterior == nivel_0 else nivel_0
            canvas.create_line(x, nivel_actual, x, nivel_anterior, fill="blue", width=2)

        canvas.create_line(x, nivel_anterior, x + tam_celda/2, nivel_anterior, fill='blue', width=2)
        canvas.create_line(x+tam_celda/2, nivel_anterior, x + tam_celda/2, nivel_actual, fill='blue', width=2)
        canvas.create_line(x+tam_celda/2, nivel_actual, x + tam_celda, nivel_actual, fill='blue', width=2)
        
        # Dibujar flecha
        flecha(canvas, x + tam_celda, nivel_actual, bits[i])
        
        nivel_anterior = nivel_actual

        # Avanzar a la siguiente celda
        x += tam_celda

def dibujar_diferencial(canvas, bits, tam_celda):
    if not bits:
        return

    polaridad = 1

    # Centrar
    ancho_senal = len(bits) * tam_celda
    x = (ANCHO - ancho_senal) // 2

    # Inicializado 
    nivel_anterior = nivel_0
    nivel_actual = nivel_1 # Para hacerla "global" en caso de 1

    for i in range(0, len(bits)):

        # Si el bit es 0, dibujar la línea vertical
        if bits[i] == '0':
            if i == 0:
                nivel_actual = nivel_1 # Solo para el primer bit
            # Crea la linea vertical si es un 0 el bit
            canvas.create_line(x, nivel_actual, x, nivel_anterior, fill="blue", width=2)
        else:
            # Actualiza los niveles si es un 1 el bit y la polaridad cambia
            nivel_anterior = nivel_actual
            nivel_actual = nivel_0 if polaridad == 1 else nivel_1
            polaridad *= -1

        # Dibuja la grafica con los niveles dados
        canvas.create_line(x, nivel_anterior, x + tam_celda/2, nivel_anterior, fill='blue', width=2)
        canvas.create_line(x+tam_celda/2, nivel_anterior, x + tam_celda/2, nivel_actual, fill='blue', width=2)
        canvas.create_line(x+tam_celda/2, nivel_actual, x + tam_celda, nivel_actual, fill='blue', width=2)
        
        # Dibujar flecha
        flecha(canvas, x + tam_celda, nivel_actual, bits[i])

        # Avanzar a la siguiente celda
        x += tam_celda