import sys
from tkinter import *
import tkinter as tk
import PIL
import mysql.connector
from PIL import Image, ImageTk
from tkinter import ttk, scrolledtext


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
    semestre = cmbSemestre.get()
    mycursor.execute("SELECT nombreMat FROM materias where semestre='"+semestre+"';")
    rows = mycursor.fetchall()

    # Borrar los elementos del ComboBox
    cmbMateria['values'] = ()
    #llenar cmb
    for row in rows:
        cmbMateria['values'] = (*cmbMateria['values'], row[0])


def buscarId():
    materia = cmbMateria.get()
    mycursor.execute("select id from materias where nombreMat='" + materia + "';")
    resultado = mycursor.fetchall()
    for res in resultado:
        registrar(res[0])


def registrar(id):
    unidad = cmbUnidad.get()
    tema = tema_entry.get()
    info = info_area.get("1.0", tk.END)
    sqlComando = "INSERT INTO informacion (unidad, tema, info, materiaId) VALUES (%s, %s, %s, %s)"
    record1 = (unidad, tema, info, id)
    mycursor.execute(sqlComando, record1)
    mydb.commit()
    welcome_label.config(text="¡Registrado con exito " + "!")

def login():
    window.withdraw()
    import Login
    Login.mostrarVentana()


# Crear ventana
window = Tk()
window.title("WikiDicente")
window.geometry("800x500")

# color de fondo
window.config(bg='#006633')

#-------panel superior---------
panel_superior = Frame(window, bd=1, relief=FLAT,  bg='#052E1A')
panel_superior.pack(side=TOP)
#etiqueta bienvenida
etiqueta_titulo = Label(panel_superior, text='Wiki Docente', fg='azure3',
font=('Arial', 30), bg='#052E1A', width=30)

etiqueta_titulo.grid(row=0, column=1)
#etiqueta accion
etiqueta_accion= Label(panel_superior, text='Registra informacion en la wiki', fg='azure3',
font=('Arial', 18), bg='#018243', width=60)

etiqueta_accion.grid(row=1, column=1)




# Crear etiquetas de wiki
semestre_label = Label(window, text="semestre:", font=("Arial", 12), bg="#006633", fg="#ffffff")
semestre_label.place(x=305, y=100)
cmbSemestre = ttk.Combobox(window,values=["1", "2", "3", "4", "5", "6", "7", "8"])
cmbSemestre.place(x=395, y=100)
# Crear botón de busqueda
busc_button = Button(window, text="Buscar materias", font=("Arial", 11), bg="#052E1A", fg="#ffffff", command=buscar)
busc_button.place(x=570, y=90)

pass_label = Label(window, text="Materia:", font=("Arial", 12), bg="#006633", fg="#ffffff")
pass_label.place(x=30, y=150)
cmbMateria = ttk.Combobox(window)
cmbMateria.place(x=110, y=150)

unidad_label = Label(window, text="Unidad:", font=("Arial", 12), bg="#006633", fg="#ffffff")
unidad_label.place(x=30, y=200)
cmbUnidad= ttk.Combobox(window,values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"])
cmbUnidad.place(x=110, y=200)
tema_label = Label(window, text="Tema:", font=("Arial", 12), bg="#006633", fg="#ffffff")
tema_label.place(x=30, y=250)
tema_entry = Entry(window, font=("Arial", 12))
tema_entry.place(x=110, y=250)
info_label = Label(window, text="Informacion:", font=("Arial", 12), bg="#006633", fg="#ffffff")
info_label.place(x=350, y=150)
info_area = scrolledtext.ScrolledText(window, width=40, height=10, font=("Arial", 10))
info_area.place(x=350, y=180)

# Crear botón de Registro
login_button = Button(window, text="Registrar", font=("Arial", 12), bg="#052E1A", fg="#ffffff", command=buscarId)
login_button.place(x=620, y=380)


# Crear etiqueta de mensaje de registro
welcome_label = Label(window, text="", font=("Arial", 12), bg="#006633", fg="#ffffff")
welcome_label.place(x=400, y=385)

# panel inferior ------------------------------------------------------------
panel_inferior = Frame(window, bd=1, relief=FLAT)
panel_inferior.pack(side=BOTTOM)
# boton ingresar
boton_ingresar = Button(panel_inferior, text='Cerrar Sesion', width=16,
fg='azure3', bg='#851818', font=('Arial', 12), command=login)
boton_ingresar.grid(row=0, column=0, pady=10, padx=325)


window.iconify()
# Mostrar ventana
def mostrarVentana():
    window.deiconify()

# cerrar proyecto
window.protocol("WM_DELETE_WINDOW", cerrar_proyecto)