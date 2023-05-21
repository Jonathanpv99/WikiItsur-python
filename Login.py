import sys
import mysql.connector
from tkinter import *
import tkinter as tk
import PIL
import SistemasComputacionales
from PIL import Image, ImageTk
import Registro
import WikiDocente


def cerrar_proyecto():
    sys.exit()

def login():
    user = user_entry.get()
    password = pass_entry.get()
    comparar(user,password)


def comparar(usuario,contraseña):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
    )

    mycursor = mydb.cursor()
    mycursor.execute("USE tareatopicos")
#RECUPERAR DATOS DE UNA TABLA
    mycursor.execute("SELECT * FROM usuario where correo='"+usuario+"' and contraseña='"+contraseña+"';")
    resultado = mycursor.fetchall()
    for renglon in resultado:
        if renglon[4] == 'Estudiante':
         ventanaSistemas()
        else:
         ventanaDocente()



def ventanaSistemas():
    window.withdraw() # Oculta la ventana actual
    SistemasComputacionales.mostrarVentana()


def registro():
    window.withdraw()
    Registro.mostrarVentana()


def ventanaDocente():
    window.withdraw()
    WikiDocente.mostrarVentana()


# Crear ventana
window = Tk()
window.title("Login")
window.geometry("400x400")

# color de fondo
window.config(bg='#006633')

#-------panel superior---------
panel_superior = Frame(window, bd=1, relief=FLAT,  bg='#052E1A')
panel_superior.pack(side=TOP)
#etiqueta bienvenida
label_welcom = Label(panel_superior, text='Bienvenidos a wikiItsur', fg='azure3',
font=('Arial', 20), bg='#052E1A', width=25)
label_welcom.grid(row=0, column=1)
# imagen usuario portal
img_usuario_portal = Image.open("logoItsur.jpg")
newSize = (80, 60)
img_usuario_portal = img_usuario_portal.resize(newSize)
img = ImageTk.PhotoImage(img_usuario_portal)
#lbl_img_logo = Label(panel_superior, image=img)
#lbl_img_logo.grid(row=0, column=0)


# Crear etiquetas de usuario y contraseña
user_label = Label(window, text="Usuario:", font=("Arial", 12), bg="#006633", fg="#ffffff")
user_label.place(x=50, y=100)
user_entry = Entry(window, font=("Arial", 12))
user_entry.place(x=150, y=100)

pass_label = Label(window, text="Contraseña:", font=("Arial", 12), bg="#006633", fg="#ffffff")
pass_label.place(x=50, y=150)
pass_entry = Entry(window, font=("Arial", 12), show="*")
pass_entry.place(x=150, y=150)

# Crear botón de inicio de sesión
login_button = Button(window, text="Iniciar sesión", font=("Arial", 12), bg="#052E1A", fg="#ffffff", command=login)
login_button.place(x=150, y=200)

# Crear botón de registro
registro_button = Button(window, text="Registrate", font=("Arial", 12), bg="#052E1A", fg="#ffffff", command=registro)
registro_button.place(x=150, y=250)

# Crear etiqueta de mensaje de bienvenida
welcome_label = Label(window, text="", font=("Arial", 12), bg="#006633", fg="#ffffff")
welcome_label.place(x=150, y=330)

# Mostrar ventana
def mostrarVentana():
    window.deiconify()


# cerrar proyecto
window.protocol("WM_DELETE_WINDOW", cerrar_proyecto)


window.mainloop()