import sys

import mysql.connector
from tkinter import *
import tkinter as tk
import PIL
from PIL import Image, ImageTk
from tkinter import ttk, scrolledtext

def cerrar_proyecto():
    sys.exit()
# cerrar proyecto
def cerrar():
    window.withdraw()
    import Foro
    Foro.mostrarVentana()


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    )

mycursor = mydb.cursor()
mycursor.execute("USE tareatopicos")

def ActualizarResp(id):
    mycursor.execute("SELECT respuesta FROM respuestas where preguntaId=" + str(id) + ";")
    texto = mycursor.fetchall()
    for tex in texto:
        resp_area.insert(tk.END, tex[0] + '\n')

def ActualizarPre(id):
    mycursor.execute("SELECT pregunta FROM preguntas where id=" + str(id) + ";")
    texto = mycursor.fetchall()
    for tex in texto:
        pre_area.insert(tk.END, tex[0] )

# Crear ventana
window = Tk()
window.title("Respuestas")
window.geometry("500x630")

# color de fondo
window.config(bg='#006633')

#-------panel superior---------
panel_superior = Frame(window, bd=1, relief=FLAT,  bg='#052E1A')
panel_superior.pack(side=TOP)
#etiqueta bienvenida
label_welcom = Label(panel_superior, text='Respuestas', fg='azure3',
font=('Arial', 20), bg='#052E1A', width=25)
label_welcom.grid(row=0, column=1)

# Crear botón de cerrar
login_button = Button(window, text="Cerrar Respuestas", font=("Arial", 12), bg="#851818", fg="#ffffff", command=cerrar)
login_button.place(x=320, y=50)

#label pregunta
semestre_label = Label(window, text="Pregunta:", font=("Arial", 12), bg="#006633", fg="#ffffff")
semestre_label.place(x=25, y=70)

# Crear TexArea Pregunta
pre_area = scrolledtext.ScrolledText(window, width=60, height=5, font=("Arial", 10))
pre_area.place(x=25, y=100)

#label Respuestas
semestre_label = Label(window, text="Respuestas:", font=("Arial", 12), bg="#006633", fg="#ffffff")
semestre_label.place(x=25, y=210)

# Crear TexArea Respuestas
resp_area = scrolledtext.ScrolledText(window, width=60, height=20, font=("Arial", 10))
resp_area.place(x=25, y=240)



window.iconify()

# Mostrar ventana
def mostrarVentana(id):
    window.deiconify()
    pre_area.delete("1.0", tk.END)
    resp_area.delete("1.0", tk.END)
    ActualizarResp(id)
    ActualizarPre(id)

# cerrar proyecto
window.protocol("WM_DELETE_WINDOW", cerrar_proyecto)