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



def buscar():
    semestre = lista_semestres.get()
    mycursor.execute("SELECT semestre,nombreMat FROM materias where semestre='"+semestre+"';")
    rows = mycursor.fetchall()
    borrarTbl()
    actualizarTbl(rows)

def loging():
    mydb.close()
    aplicacion.withdraw()
    import Login
    Login.mostrarVentana()


def foro():
    aplicacion.withdraw()
    import Foro
    Foro.mostrarVentana()

#Dinamismo de tabla
def on_select():
    item = table.focus()
    materia= table.item(item, 'values')[1]
    mycursor.execute("select id from materias where nombreMat='" + materia + "';")
    resultado = mycursor.fetchall()
    for res in resultado:
        cargartbl2(res[0])


def cargartbl2(id):
    mycursor.execute("SELECT id,Unidad,Tema FROM informacion where materiaId=" + str(id) + ";")
    rows = mycursor.fetchall()
    borrarTbl2()
    actualizarTbl2(rows)


def on_select2():
    aplicacion.withdraw()
    item = table2.focus()
    id= table2.item(item, 'values')[0]
    import Informacion
    Informacion.mostrarVentana(id)
    table2.selection_remove(table2.focus())

# iniciar a tkinter
aplicacion = Tk()
# tamaño de la ventala
aplicacion.geometry('750x500')
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
font=('Arial', 48), bg='#052E1A', width=20)

etiqueta_titulo.grid(row=0, column=1)


# label carrera
label_semestre = Label(panel_superior, text='Selecciona el semestre: ', bg='#006633')
label_semestre.place(x=10, y=80)
# lista de carreras
lista_semestres = ttk.Combobox(panel_superior,values=["1", "2", "3", "4", "5", "6", "7", "8"])
lista_semestres.place(x=150, y=80)


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


# Agrega la tabla al Frame
table.pack(side=LEFT, padx=5)

# Crear botón de VerRespuestas
login_button = Button(aplicacion, text="Ir", font=("Arial", 12), bg="#052E1A", fg="#ffffff", command=on_select)
login_button.place(x=220, y=170)



# panel derecha -------------------------------------------------------------
# Crea la tabla
table2 = Treeview(aplicacion, columns=("columna1"), show="headings")
# Agregar columnas a la tabla
table2["columns"] = ("id", "Unidad", "Tema")
table2.column("#0", width=0, stretch=tk.NO)
table2.column("id", anchor=tk.CENTER, width=75)
table2.column("Unidad", anchor=tk.CENTER, width=75)
table2.column("Tema", anchor=tk.CENTER, width=125)

# Agregar encabezados de columna a la tabla
table2.heading("#0", text="")
table2.heading("id", text="id", anchor=tk.CENTER)
table2.heading("Unidad", text="Unidad", anchor=tk.CENTER)
table2.heading("Tema", text="Tema", anchor=tk.CENTER)


# Agrega la tabla al Frame
table2.place(x=300, y=165)

# Crear botón de Responder
login_button = Button(aplicacion, text="Leer", font=("Arial", 12), bg="#052E1A", fg="#ffffff", command=on_select2)
login_button.place(x=590, y=165)

def borrarTbl():
    table.delete(*table.get_children())


def borrarTbl2():
    table2.delete(*table2.get_children())

def actualizarTbl(rows):
  for row in rows:
    table.insert("", tk.END, text="", values=row)



def actualizarTbl2(rows):
  for row in rows:
    table2.insert("", tk.END, text="", values=row)


def ActualizacionIni():
    mycursor.execute("SELECT semestre,nombreMat FROM materias ;")
    rows = mycursor.fetchall()
    for row in rows:
        table.insert("", tk.END, text="", values=row)


aplicacion.iconify()

# Mostrar ventana
def mostrarVentana():
    aplicacion.deiconify()
    borrarTbl()
    ActualizacionIni()

# cerrar proyecto
aplicacion.protocol("WM_DELETE_WINDOW", cerrar_proyecto)