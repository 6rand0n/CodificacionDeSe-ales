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

# Fondo
#imagen = PhotoImage (file=R"fondo1.png")
#fondo = Label (tp, image = imagen).pack (padx=5,pady=5)

# Desarrollo

# Boton presionado
opcion = 0

#Lista de botones
botones = []

# Define imagen
imagen = Image.open("btn.png")  
btn = ImageTk.PhotoImage(imagen)    

# Frame para posicionar los botones
frameBotones = tk.Frame(tp, bg="Sky Blue")
frameBotones.place(relx=0.5, rely=0.25, anchor="center")

# Funcion de los botones
def Elegir(i):
    global opcion
    botones[opcion].config(fg="Black")
    botones[i].config(fg="Light Green")
    opcion = i

# Ponemos los botones
for i in range(7):
    boton = Button(frameBotones, text=f"Botón {i+1}", font=TextoF, fg="Black", image=btn, compound="center",
                    borderwidth=0, highlightthickness=0, bg="Sky Blue", activebackground="Sky Blue", command=partial(Elegir, i))
    if i == 0:
        boton.config(fg="Light Green")
    boton.pack(side=LEFT, padx=10)
    botones.append(boton)

textInput = Text(tp, bg = "Light Steel Blue", height="1.4", width="40", borderwidth= "0.6", font = InputF, 
                 relief = "sunken") 
textInput.place(relx = 0.5, rely = 0.35, anchor = "center")

textInput.tag_configure("centrado", justify="center")
textInput.tag_add("centrado", "1.0", "end")

# Lamba permite enviar manualmente los parametros para enviar el evento y el objeto
textInput.bind("<KeyPress>", lambda e: filtrar(e, textInput))
textInput.bind("<KeyRelease>", lambda e: filtrar(e, textInput))

    
tk.mainloop()