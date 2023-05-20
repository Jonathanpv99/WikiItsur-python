# Importar tkinter
import sys

import mysql.connector
from tkinter import *
import tkinter as tk
import PIL
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.ttk import Treeview

def cerrar_proyecto():
    sys.exit()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    )

mycursor = mydb.cursor()
mycursor.execute("USE tareatopicos")
mycursor.execute("SELECT semestre,materia FROM preguntas;")
rows = mycursor.fetchall()


def buscar():
    semestre = lista_semestres.get()
    mycursor.execute("SELECT semestre,materia FROM preguntas where semestre='"+semestre+"';")
    rows = mycursor.fetchall()
    borrarTbl()
    actualizarTbl(rows)

def loging():
    aplicacion.withdraw()
    import Login
    Login.mostrarVentana()


def foro():
    aplicacion.withdraw()
    import Foro
    Foro.mostrarVentana()


# iniciar a tkinter
aplicacion = Tk()
# tamaño de la ventala
aplicacion.geometry('700x500+0+0')
# evitar maximizar la ventana
aplicacion.resizable(0, 0)
# titulo de la ventana
aplicacion.title('WikiItsur')
# color de fondo de la ventana
aplicacion.config(bg='#006633')
# panel superior ------------------------------------------------------------
panel_superior = Frame(aplicacion, bd=1, relief=FLAT,  bg='#052E1A')
panel_superior.pack(side=TOP)
# etiqueta de titulo
etiqueta_titulo = Label(panel_superior, text='Sistemas C. wiki.', fg='azure3',
font=('Arial', 48), bg='#052E1A', width=15)

etiqueta_titulo.grid(row=0, column=1)
# imagen usuario portal
img_usuario_portal = Image.open("logoItsur.jpg")
newSize = (100, 70)
img_usuario_portal = img_usuario_portal.resize(newSize)
img = ImageTk.PhotoImage(img_usuario_portal)
lbl_img_logo = Label(panel_superior, image=img)
lbl_img_logo.grid(row=0, column=0)


# label carrera
label_semestre = Label(panel_superior, text='Selecciona el semestre: ', bg='#006633')
label_semestre.grid(row=1, column=0,sticky=E)
# lista de carreras
lista_semestres = ttk.Combobox(panel_superior,values=["1", "2", "3", "4", "5", "6", "7", "8"])
lista_semestres.grid(row=2, column=0, pady=2, sticky=E)


# boton buscar
boton_buscar = Button(panel_superior, text='Buscar', width=15,
fg='azure3', bg='#006633', font=('Arial', 12), command=buscar)
boton_buscar.grid(row=3, column=1, pady=3)


# panel inferior ------------------------------------------------------------
panel_inferior = Frame(aplicacion, bd=1, relief=FLAT)
panel_inferior.pack(side=BOTTOM)
# boton ingresar
boton_ingresar = Button(panel_inferior, text='Cerrar Sesion', width=26,
fg='azure3', bg='#851818', font=('Arial', 12), command=loging)
boton_ingresar.grid(row=0, column=0, pady=15, padx=55)

# boton ir a foro
boton_foro = Button(panel_inferior, text='Ir a foro', width=26,
fg='azure3', bg='#052E1A', font=('Arial', 12), command=foro)

boton_foro.grid(row=0, column=1, pady=15, padx=50)

#----------------panel izquierdo---------------------------------------
# Crea la tabla
table = Treeview(aplicacion, columns=("columna1"), show="headings")
# Agregar columnas a la tabla
table["columns"] = ("semestre", "materia")
table.column("#0", width=0, stretch=tk.NO)
table.column("semestre", anchor=tk.CENTER, width=75)
table.column("materia", anchor=tk.CENTER, width=125)

# Agregar encabezados de columna a la tabla
table.heading("#0", text="")
table.heading("semestre", text="semestre", anchor=tk.CENTER)
table.heading("materia", text="materia", anchor=tk.CENTER)

# Agregar filas a la tabla
for row in rows:
    table.insert("", tk.END, text="", values=row)

# Agrega la tabla al Frame
table.pack(side=LEFT, padx=5)


# panel derecha -------------------------------------------------------------
panel_derecho = Frame(aplicacion, bd=1, relief=FLAT, bg='#006633')
panel_derecho.pack(side=RIGHT)
# nombre del usuario conectado
usuaroName = 'Jonathan Peña'
lbl_nombre_usuario = Label(panel_derecho, text='Usuario: ' + usuaroName, bg='#006633')
lbl_nombre_usuario.grid(row=0, column=0)
# imagen foro
img_foro = Image.open('foro.png')
newSize = (200, 100)
img_foro = img_foro.resize(newSize)
imgF = ImageTk.PhotoImage(img_foro)
lbl_img_foro = Label(panel_derecho, image=imgF)
lbl_img_foro.grid(row=2, column=0, pady=30)

# mensaje
mensaje = Label(panel_derecho, text='!Ingresa al foro estudiantil del Wikitsur \ny resuelve tus dudas o ayuda a los demas¡',
bg='#006633')
mensaje.grid(row=3, column=0)




def borrarTbl():
    table.delete(*table.get_children())

def actualizarTbl(rows):
  for row in rows:
    table.insert("", tk.END, text="", values=row)

aplicacion.iconify()

# Mostrar ventana
def mostrarVentana():
    aplicacion.deiconify()


# cerrar proyecto
aplicacion.protocol("WM_DELETE_WINDOW", cerrar_proyecto)