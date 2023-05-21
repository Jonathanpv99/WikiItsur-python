import sys

import mysql.connector
from tkinter import *
import tkinter as tk
import PIL
from PIL import Image, ImageTk
from tkinter import ttk

def cerrar_proyecto():
    sys.exit()


def registrar():
    nombre = nombre_entry.get()
    correo = correo_entry.get()
    contraseña = pass_entry.get()
    contraseña2 = pass2_entry.get()
    tipo = cmbTipo.get()
    registro(nombre, correo, contraseña,tipo)





def registro(nomb,email,pass1,tipo):

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
    )

    mycursor = mydb.cursor()
    mycursor.execute("USE tareatopicos")

    sqlComando = "INSERT INTO usuario (nombre, correo, contraseña, tipo) VALUES (%s, %s, %s, %s)"
    record1 = (nomb, email ,pass1,tipo)
    mycursor.execute(sqlComando, record1)
    mydb.commit()
    welcome_label.config(text="¡Registrado con exito "  + "!")


def login():
    window.withdraw()
    import Login
    Login.mostrarVentana()

# Crear ventana
window = Tk()
window.title("Login")
window.geometry("400x530")

# color de fondo
window.config(bg='#006633')

#-------panel superior---------
panel_superior = Frame(window, bd=1, relief=FLAT,  bg='#052E1A')
panel_superior.pack(side=TOP)
#etiqueta bienvenida
label_welcom = Label(panel_superior, text='Registro wikiItsur', fg='azure3',
font=('Arial', 20), bg='#052E1A', width=25)
label_welcom.grid(row=0, column=1)
# imagen usuario portal
img_usuario_portal = Image.open("logoItsur.jpg")
newSize = (80, 60)
img_usuario_portal = img_usuario_portal.resize(newSize)
img = ImageTk.PhotoImage(img_usuario_portal)
#lbl_img_logo = Label(panel_superior, image=img)
#lbl_img_logo.grid(row=0, column=0)


# Crear etiquetas de usuario
nombre_label = Label(window, text="Nombre:", font=("Arial", 12), bg="#006633", fg="#ffffff")
nombre_label.place(x=50, y=100)
nombre_entry = Entry(window, font=("Arial", 12))
nombre_entry.place(x=150, y=100)

correo_label = Label(window, text="Correo:", font=("Arial", 12), bg="#006633", fg="#ffffff")
correo_label.place(x=50, y=150)
correo_entry = Entry(window, font=("Arial", 12),)
correo_entry.place(x=150, y=150)

pass_label = Label(window, text="Contraseña:", font=("Arial", 12), bg="#006633", fg="#ffffff")
pass_label.place(x=50, y=200)
pass_entry = Entry(window, font=("Arial", 12), show="*")
pass_entry.place(x=150, y=200)
pass2_label = Label(window, text="Repite Contraseña:", font=("Arial", 12), bg="#006633", fg="#ffffff")
pass2_label.place(x=50, y=250)
pass2_entry = Entry(window, font=("Arial", 12), show="*")
pass2_entry.place(x=150, y=250)
#Tipo
tipo = Label(window, text="Tipo de Usuario:", font=("Arial", 12), bg="#006633", fg="#ffffff")
tipo.place(x=50, y=300)
#cmb tipo usuario
cmbTipo = ttk.Combobox(window, values=["Estudiante", "Docente"])
cmbTipo.place(x=180, y=300)

# Crear botón de Registro
login_button = Button(window, text="Registrarte", font=("Arial", 12), bg="#052E1A", fg="#ffffff", command=registrar)
login_button.place(x=150, y=350)

# Crear botón de login
login_button = Button(window, text="Login", font=("Arial", 12), bg="#052E1A", fg="#ffffff", command=login )
login_button.place(x=150, y=400)

# Crear etiqueta de mensaje de bienvenida
welcome_label = Label(window, text="", font=("Arial", 12), bg="#006633", fg="#ffffff")
welcome_label.place(x=90, y=430)



window.iconify()

# Mostrar ventana
def mostrarVentana():
    window.deiconify()


# cerrar proyecto
window.protocol("WM_DELETE_WINDOW", cerrar_proyecto)