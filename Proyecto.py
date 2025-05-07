from tkinter import*
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
from functools import partial

# Configuraciones generales
tp = Tk()

tp.title("Codificacion")
tp.geometry ("1600x900")
tp.configure(background="Sky Blue")
TituloF = tkFont.Font (family = "Century Gothic", size = 24, weight = "bold")
TextoF = tkFont.Font (family = "Century Gothic", size = 12, weight = "bold")

# Etiqueta de titulo
T = tk.Label (tp, text="Codificacion de señales",font = TituloF, fg = "Steel Blue")
T.pack (padx=20,pady=20,fill=tk.X)

# Fondo
#imagen = PhotoImage (file=R"fondo1.png")
#fondo = Label (tp, image = imagen).pack (padx=5,pady=5)

# Desarrollo

# Boton presionado
opcion = 0

#Lista de botones
botones = []

def Opc1(i):
    global opcion
    botones[opcion].config(fg="Black")
    botones[i].config(fg="Light Green")
    opcion = i

# Define imagen
imagen = Image.open("btn.png")  
btn = ImageTk.PhotoImage(imagen)    

frame_centrado = tk.Frame(tp, bg="Sky Blue")
frame_centrado.pack(expand=True) 

# el comando es una funcion
# Cuida la indentacion, es importante aqui  

for i in range(7):
    boton = Button(frame_centrado, text=f"Botón {i+1}", font=TextoF, fg="Black", image=btn, compound="center",
                    borderwidth=0, highlightthickness=0, bg="Sky Blue", activebackground="Sky Blue", command=partial(Opc1, i))
    if i == 0:
        boton.config(fg="Light Green")
    boton.pack(side=LEFT, padx=10)
    botones.append(boton)
    
tk.mainloop()