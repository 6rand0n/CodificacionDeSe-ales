from tkinter import*
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
from functools import partial
from funciones import *

# Configuraciones generales
tp = Tk()

tp.title("Codificacion")
tp.geometry ("1600x900")
tp.configure(background="Sky Blue")
TituloF = tkFont.Font (family = "Century Gothic", size = 24, weight = "bold")
TextoF = tkFont.Font (family = "Century Gothic", size = 12, weight = "bold")
InputF = tkFont.Font (family = "Century Gothic", size = 16, weight = "bold")

# Etiqueta de titulo
T = tk.Label (tp, text="Codificacion de señales",font = TituloF, fg = "Steel Blue")
T.pack (padx=20,pady=10,fill=tk.X)

# Desarrollo

# Boton presionado
opcion = 0

#Lista de botones
botones = []
botonNombre = ["NRZ-L", "NRZ-I", "Bipolar AMI", "Pseudoternario", "Manchester", "Código diferencial"]

# Define imagen
imagen = Image.open("btn.png")     
ancho, alto = imagen.size
imgBtn = imagen.resize((int(ancho * 1.2), int(alto)), Image.Resampling.LANCZOS)
btn = ImageTk.PhotoImage(imgBtn)

# Frame para posicionar los botones

frameBotones = tk.Frame(tp, bg="Sky Blue")
frameBotones.place(relx=0.5, rely=0.25, anchor="center")

# Funcion de los botones

def Elegir(i):
    global opcion
    botones[opcion].config(fg="Black")
    botones[i].config(fg="Light Green")
    opcion = i

    if i in (2, 3):  # Bipolar AMI o Pseudoternario
        canvas.config(height=320)
    else:
        canvas.config(height=200)

    graficar(canvas, textInput.get("1.0", "end-1c"), opcion)

# Ponemos los botones

for i in range(6):
    boton = Button(frameBotones, text=botonNombre[i], font=TextoF, fg="Black", image=btn, compound="center",
                    borderwidth=0, highlightthickness=0, bg="Sky Blue", activebackground="Sky Blue", command=partial(Elegir, i))
    if i == 0:
        boton.config(fg="Light Green")
    boton.pack(side=LEFT, padx=10)
    botones.append(boton)

# Configuracion del TextInput

textInput = Text(tp, bg = "Light Steel Blue", height="1.4", width="40", borderwidth= "0.6", font = InputF, 
                 relief = "sunken") 
textInput.place(relx = 0.5, rely = 0.35, anchor = "center")

textInput.tag_configure("centrado", justify="center")
textInput.tag_add("centrado", "1.0", "end")

# Lamba permite enviar manualmente los parametros para enviar el evento y el objeto

def manejar_input(e):
    filtrar(e, textInput)
    graficar(canvas, textInput.get("1.0", "end-1c"), opcion)

textInput.bind("<KeyPress>", lambda e: filtrar(e, textInput))
textInput.bind("<KeyRelease>", manejar_input)

# Canvas

canvas = tk.Canvas(tp, width=1200, height=200, bg='white')
canvas.place(relx = 0.5, rely = 0.6, anchor = "center")

graficar(canvas, "", opcion)

# Etiqueta de Autores

T = tk.Label (tp, text="Brandon Javier Becerra Davila  415730",font = TituloF, fg = "Steel Blue")
T.place (relx = 0.6, rely = 0.9, anchor = "sw")
T = tk.Label (tp, text="Bruno Gonzalez Castillo             301249",font = TituloF, fg = "Steel Blue")
T.place (relx = 0.6, rely = 0.95, anchor = "sw")

tk.mainloop()