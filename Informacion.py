import sys

import mysql.connector
from tkinter import *
import tkinter as tk
import PIL
from PIL import Image, ImageTk
from tkinter import ttk, scrolledtext


# cerrar proyecto
def cerrar():
    window.iconify()


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    )

mycursor = mydb.cursor()
mycursor.execute("USE tareatopicos")

def ActualizarInfo(id):
    mycursor.execute("SELECT info FROM informacion where id=" + str(id) + ";")
    texto = mycursor.fetchall()
    for tex in texto:
        info_area.insert(tk.END, tex[0])



# Crear ventana
window = Tk()
window.title("Login")
window.geometry("500x630")

# color de fondo
window.config(bg='#006633')

#-------panel superior---------
panel_superior = Frame(window, bd=1, relief=FLAT,  bg='#052E1A')
panel_superior.pack(side=TOP)
#etiqueta bienvenida
label_welcom = Label(panel_superior, text='Pagina de Lectura', fg='azure3',
font=('Arial', 20), bg='#052E1A', width=25)
label_welcom.grid(row=0, column=1)


# Crear TexArea lectura
info_area = scrolledtext.ScrolledText(window, width=60, height=30, font=("Arial", 10))
info_area.place(x=25, y=100)


# Crear botón de cerrar
login_button = Button(window, text="Cerrar lectura", font=("Arial", 12), bg="#851818", fg="#ffffff", command=cerrar)
login_button.place(x=350, y=50)




window.iconify()

# Mostrar ventana
def mostrarVentana(id):
    window.deiconify()
    info_area.delete("1.0", tk.END)
    ActualizarInfo(id)

