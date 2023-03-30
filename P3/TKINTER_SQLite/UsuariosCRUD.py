

from tkinter import *
from tkinter import ttk
import tkinter as tk
from ControladorDB import *

#. Crear una objeto de tipo contralador

controlador= controladorBD()

#Procedermos a guardar usando el metodo del objeto controlador.

def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())
    

def ejecutaSelectU():
    
    rsUsuario = controlador.consultaUsuario(varBus.get())
    
    for usu in rsUsuario:   
        
        cadena = str(usu[0]) + " " + usu[1] + " " + usu[2] +" " +  str(usu[3])
    
    if(rsUsuario):
        textBus.insert('0.0',cadena)
        print(cadena)
    
    else:
    
        messagebox.showwarning("CUIDADO","No hay usuario")
        

            

       
        
        
   


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


#Pestaña 2 : Buscar ususario

titulo2 = Label(pestana2,text="Buscar Usuario",fg="Blue",font=("Comic Sans",18)).pack()

varBus= tk.StringVar()
lblid= Label(pestana2,text="Identificador Usuario: ").pack()

    

textid= Entry(pestana2,textvariable=varBus).pack()

btnBusqueda= Button(pestana2,text="Buscar Usuario",command=ejecutaSelectU).pack()

subBus= Label(pestana2,text="Registrado:", fg="Blue", font=("Modern,15")).pack()
textBus= tk.Text(pestana2,height=5,width=52)

        







#Crear la funcion para buscar un usuario

    

textBus.pack()


panel.add(pestana1,text="Formulario de Usuarios")
panel.add(pestana2,text="Buscar Usuario")
panel.add(pestana3,text="Consultar Usuarios")
panel.add(pestana4,text="Actualizar Usuario")

Ventana.mainloop()

