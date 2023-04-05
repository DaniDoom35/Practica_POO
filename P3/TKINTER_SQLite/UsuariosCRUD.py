

from tkinter import *
from tkinter import ttk
import tkinter as tk
from ControladorDB import *

#. Crear una objeto de tipo contralador

controlador= controladorBD()

#Procedermos a guardar usando el metodo del objeto controlador.

def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())
    

# Funcion para buscar a un usuario con id y ponerlo en el cuadro de text

def ejecutaSelectU():
    
    
    #borrar texto anterior
    
    textBus.delete('0.0',END)
    
    
    rsUsuario = controlador.consultaUsuario(varBus.get())
    
    
 
    for usu in rsUsuario:   
        
        cadena2 = (" | " + str(usu[0]) + " | " + usu[1] + " | " + usu[2] +" | " +  str(usu[3]))
    
    if(rsUsuario):
        
        textBus.insert('0.0',cadena2)
    else:
    
        messagebox.showwarning("CUIDADO","No hay usuario")


# Funcion para traer todos los usuarios 

def ejecutaSelectT():
    
    #Borrar datos del treeview anterior
    
    tree.delete(*tree.get_children())
    

    
    
        
    # Agregar todos los usuarios a un treeview
    
    rsUsuarios = controlador.consultaUsuarios()
    
    for usu2 in rsUsuarios:
       
        tree.insert(parent='',index='end',values=(usu2[0],usu2[1],usu2[2]))
        
        print(usu2)
    
        

def ejecutaUpdate():
    
    controlador.actualizarUsuario(varId2.get(),varNom2.get(),varCor2.get(),varCon2.get())
    
    varId2.set("")
    varNom2.set("")
    varCor2.set("")
    varCon2.set("")

def ejecutaDelete():
    
    controlador.eliminarusuario(varId.get())
    
    varId.set("")
    varNom.set("")
    varCor.set("")
    varCon.set("")
    


    

#Ventana
Ventana = Tk()
Ventana.title("CRUD Usuarios")
Ventana.geometry("600x400")

#Notebook

panel = ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

# pestañas

pestana1 = ttk.Frame(panel)

pestana2 = ttk.Frame(panel)

pestana3 = ttk.Frame(panel)

pestana4 = ttk.Frame(panel)

pestana5 = ttk.Frame(panel)


#PEstaña1: Formulario Usuarios
titulo = Label(pestana1,text="Registro de usuarios",fg="Blue",font=("Modern",18)).pack()


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

titulo2 = Label(pestana2,text="Buscar Usuario",fg="Blue",font=("Modern",18)).pack()

varBus= tk.StringVar()
lblid= Label(pestana2,text="Identificador Usuario: ").pack()

    

textid= Entry(pestana2,textvariable=varBus).pack()

btnBusqueda= Button(pestana2,text="Buscar Usuario",command=ejecutaSelectU).pack()

subBus= Label(pestana2,text="Registrado:", fg="Blue", font=("Modern,15")).pack()
textBus= tk.Text(pestana2,height=5,width=52)


#3. Pestaña 3 consultar usuarios

titulo3 = Label(pestana3,text="Consultar Usuarios",fg="Blue",font=("Modern",18)).pack()

#1. Agregar un treeview a la pestaña 3

tree = ttk.Treeview(pestana3,columns=(1,2,3),show="headings",height="5")

#2. Agregar las columnas al treeview

tree.heading(1,text="ID")

tree.heading(2,text="Nombre")

tree.heading(3,text="Correo")


tree.pack()



#3. Agregar un boton para consultar usuarios

btnBusqueda= Button(pestana3,text="Buscar Usuario",command=ejecutaSelectT).pack()

textBus.pack()

#4. Pestaña 4 aztulizar usuario ccon metodo actulizar ususario

titulo4 = Label(pestana4,text="Actualizar Usuario",fg="Blue",font=("Modern",18)).pack()

varId2= tk.StringVar()

lblid= Label(pestana4,text="Identificador Usuario: ").pack()

textid= Entry(pestana4,textvariable=varId2).pack()

varNom2= tk.StringVar()

lblNom= Label(pestana4,text="Nombre: ").pack()

textNom= Entry(pestana4,textvariable=varNom2).pack()

varCor2= tk.StringVar()

lblCor= Label(pestana4,text="Correo: ").pack()

textCor= Entry(pestana4,textvariable=varCor2).pack()

varCon2= tk.StringVar()

lblCon= Label(pestana4,text="Contraseña: ").pack()

textCon= Entry(pestana4,textvariable=varCon2).pack()

btnGuardar= Button(pestana4,text="Actualizar Usuario",command=ejecutaUpdate).pack()

#5. Pestaña para eliminar usuario con sqlite3

titulo5 = Label(pestana5,text="Eliminar Usuario",fg="Blue",font=("Modern",18)).pack()

varId= tk.StringVar()

lblid= Label(pestana5,text="Identificador Usuario: ").pack()

textid= Entry(pestana5,textvariable=varId).pack()

btnGuardar= Button(pestana5,text="Eliminar Usuario",command=ejecutaDelete).pack()



#Agregar las pestañas al panel

panel.add(pestana1,text="Formulario de Usuarios")
panel.add(pestana2,text="Buscar Usuario")
panel.add(pestana3,text="Consultar Usuarios")
panel.add(pestana4,text="Actualizar Usuario")
panel.add(pestana5,text="Eliminar usuario")

Ventana.mainloop()

