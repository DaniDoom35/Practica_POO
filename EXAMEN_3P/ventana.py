
from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador3P import *



#contralador

controlador= controladorMT()

    
#Funcion para insertar material

def ejecutaInsert():
    
    mat=varNom.get()
    can=varCan.get()
    
    controlador.guardarMaterial(mat,can)
    
    
    print(mat,can)
    
#Funcion Para consultar todos los materiales

def ejecutaSelectT():
    
    
    
    tree.delete(*tree.get_children())
    
        
   
    
    rsMateriales = controlador.consultaMateriales()
    
    for mat in rsMateriales:
       
        tree.insert(parent='',index='end',values=(mat[0],mat[1],mat[2]))
        
        
#Funcion para Actualizar material

def ejecutaUpdate():
    
    id=varId.get()
    mat=varNom2.get()
    can=varCan2.get()
    
    
    controlador.actualizarMaterial(id,mat,can)
    
    print(id,mat,can)



Ventana = Tk()
Ventana.title("Ferreteria")
Ventana.geometry("600x400")



panel = ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)



titulo = Label(pestana1,text="Registro de Materiales",fg="Blue",font=(20)).pack()


varNom= tk.StringVar()
lblNom= Label(pestana1,text="Nombre: ").pack()
textNom= Entry(pestana1,textvariable=varNom).pack()

varCan= tk.StringVar()
lblCan= Label(pestana1,text="Cantidad: ").pack()
textCan= Entry(pestana1,textvariable=varCan).pack()


btnGuardar= Button(pestana1,text="Guardar Usuario",command=ejecutaInsert).pack()



titulo3 = Label(pestana2,text="Mostrar Materiales",fg="Blue",font=(20)).pack()

tree = ttk.Treeview(pestana2,columns=(1,2,3),show="headings",height="5")



tree.heading(1,text="ID")

tree.heading(2,text="Nombre")

tree.heading(3,text="Cantidad")


tree.pack()


btnMostrar= Button(pestana2,text="Mostrar Materiales",command=ejecutaSelectT).pack()



titulo3 = Label(pestana3,text="Actualizar Materiales",fg="Blue",font=(20)).pack()

varId= tk.StringVar()

lblId= Label(pestana3,text="ID: ").pack()

textId= Entry(pestana3,textvariable=varId).pack()

varNom2= tk.StringVar()

lblNom2= Label(pestana3,text="Nombre: ").pack()

textNom2= Entry(pestana3,textvariable=varNom2).pack()

varCan2= tk.StringVar()

lblCan2= Label(pestana3,text="Cantidad: ").pack()

textCan2= Entry(pestana3,textvariable=varCan2).pack()

btnActualizar= Button(pestana3,text="Actualizar Material",command=ejecutaUpdate).pack()





panel.add(pestana1,text="Insertar Material")
panel.add(pestana2,text="Consultar Materiales")
panel.add(pestana3,text="Actualizar Materiales")


Ventana.mainloop()
