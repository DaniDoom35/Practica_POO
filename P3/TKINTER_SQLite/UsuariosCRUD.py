

from tkinter import *
from tkinter import ttk
import tkinter as tk
from ControladorDB import *

#. Crear una objeto de tipo contralador

controlador= controladorBD()

#Procedermos a guardar usando el metodo del objeto controlador.

def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())
    



#Ventana
Ventana = Tk()
Ventana.title("CRUD Usuarios")
Ventana.geometry("500x300")

#Notebook

panel = ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

#pestañas

pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)

#PEstaña1: Formulario Usuarios
titulo = Label(pestana1,text="Registro de usuarios",fg="Blue",font=("Comic Sans",18)).pack()

varNom= tk.StringVar()
lblNom= Label(pestana1,text="Nombre: ").pack()
textNom= Entry(pestana1,textvariable=varNom).pack()

varCor= tk.StringVar()
lblCor= Label(pestana1,text="Correo: ").pack()
textCor= Entry(pestana1,textvariable=varCor).pack()

varCon= tk.StringVar()
lblCon= Label(pestana1,text="Contraseña: ").pack()
textCon= Entry(pestana1,textvariable=varCon).pack()

btnGuardar= Button(pestana1,text="Guardar Usuario",command=ejecutaInsert).pack()


panel.add(pestana1,text="Formulario de Usuarios")
panel.add(pestana2,text="Buscar Usuario")
panel.add(pestana3,text="Consultar Usuarios")
panel.add(pestana4,text="Actualizar Usuario")

Ventana.mainloop()

