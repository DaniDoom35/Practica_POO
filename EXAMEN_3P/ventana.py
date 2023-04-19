# Crear una ventana con pestañás

from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador3P import *



#. Crear una objeto de tipo contralador

controlador= controladorMT()

    
#Funcion para insertar material

def ejecutaInsert():
    
    mat=varNom.get()
    can=varCan.get()
    
    controlador.guardarMaterial(mat,can)
    
    
    print(mat,can)



#Ventana
Ventana = Tk()
Ventana.title("Ferreteria")
Ventana.geometry("600x400")

#Notebook

panel = ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

# pestañas

pestana1 = ttk.Frame(panel)

pestana2 = ttk.Frame(panel)

pestana3 = ttk.Frame(panel)


#Pestaña Insertar Material solo cantidad y nombre


titulo = Label(pestana1,text="Registro de Materiales",fg="Blue",font=("Modern",18)).pack()


varNom= tk.StringVar()
lblNom= Label(pestana1,text="Nombre: ").pack()
textNom= Entry(pestana1,textvariable=varNom).pack()

varCan= tk.StringVar()
lblCan= Label(pestana1,text="Cantidad: ").pack()
textCan= Entry(pestana1,textvariable=varCan).pack()


btnGuardar= Button(pestana1,text="Guardar Usuario",command=ejecutaInsert).pack()

#Pestaña Consultar Materiales

titulo = Label(pestana2,text="Consulta de Materiales",fg="Blue",font=("Modern",18)).pack()



#Pestaña Actualizar Materiales

titulo = Label(pestana3,text="Actualizacion de Materiales",fg="Blue",font=("Modern",18)).pack()












#Agregar las pestañas al panel

panel.add(pestana1,text="Insertar Material")
panel.add(pestana2,text="Consultar Materiales")
panel.add(pestana3,text="Actualizar Materiales")


Ventana.mainloop()
