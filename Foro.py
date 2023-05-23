import sys
from tkinter import *
import tkinter as tk
from tkinter.ttk import Treeview

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

def buscarTbl():
    borrarTbl()
    semestre = lista_semestres.get()
    mycursor.execute("SELECT  p.id, m.nombreMat, p.unidad,p.pregunta FROM preguntas p JOIN materias m ON p.materiaId = m.id  where m.semestre='"+semestre+"';")
    rows = mycursor.fetchall()
    for row in rows:
        table2.insert("", tk.END, text="", values=row)

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
    info = info_area.get("1.0", tk.END)
    sqlComando = "INSERT INTO preguntas(unidad, pregunta, materiaId) VALUES (%s, %s, %s)"
    record1 = (unidad, info, id)
    mycursor.execute(sqlComando, record1)
    mydb.commit()
    ActualizarTabla()

def login():
    window.withdraw()
    import Login
    Login.mostrarVentana()

def wiki():
    window.withdraw()
    import SistemasComputacionales
    SistemasComputacionales.mostrarVentana()


def ActualizarTabla():
    borrarTbl()
    mycursor.execute("SELECT p.id, m.nombreMat, p.unidad,p.pregunta FROM preguntas p JOIN materias m ON p.materiaId = m.id ;")
    rows = mycursor.fetchall()
    for row in rows:
        table2.insert("", tk.END, text="", values=row)


def respuestas():
    window.withdraw()
    seleccion = table2.focus()  # Obtener el índice de la fila seleccionada
    valores = table2.item(seleccion, 'values')  # Obtener los valores de la fila seleccionada
    if valores:
        id = valores[0]  # Obtener el valor de la primera columna (índice 0)
        import VerRespuestas
        VerRespuestas.mostrarVentana(id)

def responder():
    window.withdraw()
    seleccion = table2.focus()  # Obtener el índice de la fila seleccionada
    valores = table2.item(seleccion, 'values')  # Obtener los valores de la fila seleccionada
    if valores:
        id = valores[0]  # Obtener el valor de la primera columna (índice 0)
        import Responder
        Responder.mostrarVentana(id)
# Crear ventana
window = Tk()
window.title("Foro")
window.geometry("800x650")

# color de fondo
window.config(bg='#006633')

#-------panel superior---------
panel_superior = Frame(window, bd=1, relief=FLAT,  bg='#052E1A')
panel_superior.pack(side=TOP)
#etiqueta bienvenida
etiqueta_titulo = Label(panel_superior, text='Foro Estudiantil', fg='azure3',
font=('Arial', 30), bg='#052E1A', width=30)

etiqueta_titulo.grid(row=0, column=1)
#etiqueta accion
etiqueta_accion= Label(panel_superior, text='Escoje una materia y deja tus preguntas', fg='azure3',
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
pass_label.place(x=30, y=180)
cmbMateria = ttk.Combobox(window)
cmbMateria.place(x=110, y=180)

unidad_label = Label(window, text="Unidad:", font=("Arial", 12), bg="#006633", fg="#ffffff")
unidad_label.place(x=30, y=230)
cmbUnidad= ttk.Combobox(window,values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"])
cmbUnidad.place(x=110, y=230)
info_label = Label(window, text="Tu pregunta:", font=("Arial", 12), bg="#006633", fg="#ffffff")
info_label.place(x=350, y=150)
info_area = scrolledtext.ScrolledText(window, width=40, height=5, font=("Arial", 10))
info_area.place(x=350, y=180)

# Crear botón de Registro
login_button = Button(window, text="Registrar", font=("Arial", 12), bg="#052E1A", fg="#ffffff", command=buscarId)
login_button.place(x=620, y=280)



#----------------------------------------tabla y acciones wiki
# label carrera
label_semestre = Label(window, text='Buscar por \n semestre: ',font=("Arial", 12), bg='#006633',fg="#ffffff")
label_semestre.place(x=25, y=285)
# lista de carreras
lista_semestres = ttk.Combobox(window,values=["1", "2", "3", "4", "5", "6", "7", "8"])
lista_semestres.place(x=110, y=300)
# boton buscar
boton_buscar = Button(window, text='Buscar', width=15,
fg='azure3', bg='#052E1A', font=('Arial', 12), command=buscarTbl)
boton_buscar.place(x=260, y=295)

# Crea la tabla
table2 = Treeview(window, columns=("columna1"), show="headings")
# Agregar columnas a la tabla
table2["columns"] = ("id","materia", "Unidad", "pregunta")
table2.column("#0", width=0, stretch=tk.NO)
table2.column("id", anchor=tk.CENTER, width=75)
table2.column("materia", anchor=tk.CENTER, width=125)
table2.column("Unidad", anchor=tk.CENTER, width=75)
table2.column("pregunta", anchor=tk.CENTER, width=125)

# Agregar encabezados de columna a la tabla
table2.heading("#0", text="")
table2.heading("id", text="id", anchor=tk.CENTER)
table2.heading("materia", text="materia", anchor=tk.CENTER)
table2.heading("Unidad", text="Unidad", anchor=tk.CENTER)
table2.heading("pregunta", text="pregunta", anchor=tk.CENTER)

# Agrega la tabla al Frame
table2.place(x=25, y=340)

# Crear botón de VerRespuestas
login_button = Button(window, text="Respuestas", font=("Arial", 12), bg="#052E1A", fg="#ffffff", command=respuestas)
login_button.place(x=460, y=400)

# Crear botón de Responder
login_button = Button(window, text="Responder", font=("Arial", 12), bg="#052E1A", fg="#ffffff", command=responder)
login_button.place(x=600, y=400)

# panel inferior ------------------------------------------------------------
panel_inferior = Frame(window, bd=1, relief=FLAT)
panel_inferior.pack(side=BOTTOM)
# boton ingresar
boton_ingresar = Button(panel_inferior, text='Cerrar Sesion', width=26,
fg='azure3', bg='#851818', font=('Arial', 12), command=login)
boton_ingresar.grid(row=0, column=0, pady=15, padx=55)

# boton ir a foro
boton_foro = Button(panel_inferior, text='Regresar a Wiki', width=26,
fg='azure3', bg='#052E1A', font=('Arial', 12), command=wiki)

boton_foro.grid(row=0, column=1, pady=15, padx=50)


def borrarTbl():
    table2.delete(*table2.get_children())

window.iconify()
# Mostrar ventana
def mostrarVentana():
    window.deiconify()
    ActualizarTabla()

# cerrar proyecto
window.protocol("WM_DELETE_WINDOW", cerrar_proyecto)
