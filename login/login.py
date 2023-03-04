
import tkinter 
from validar import *
from tkinter import messagebox

def login():
    val.login_validacion(usuario_entrada.get(),pass_entrada.get())
val = validar() 

ventana = tkinter.Tk()
ventana.title("Login")
ventana.geometry('340x440')
ventana.configure(bg = 'white')

  



frame = tkinter.Frame(bg="#FFFFFF")



inicio_caja = tkinter.Label(frame, text = "Inicio de sesion",bg="#FFFFFF", font="Arial, 30")
usuario_caja = tkinter.Label(frame, text = "Usuario",bg= "#FFFFFF",font="Arial, 16")
usuario_entrada = tkinter.Entry(frame)
pass_entrada = tkinter.Entry(frame, show = '*')
pass_caja = tkinter.Label(frame, text = "Contrasña",bg="#FFFFFF", font="Arial, 16")
inicio_boton = tkinter.Button(frame, text = "Iniciar sesion", bg = 'blue', fg = 'white',command = login)


    
    

inicio_caja.grid(row = 0, column = 0, columnspan = 2, pady = 40)
usuario_caja.grid(row = 1, column = 0)
usuario_entrada.grid(row = 1, column = 1, pady = 20)
pass_caja.grid(row = 2, column = 0)
pass_entrada.grid(row = 2, column = 1, pady = 20)
inicio_boton.grid(row = 3, column = 0, columnspan = 2, pady = 30)




frame.pack()


ventana.mainloop()