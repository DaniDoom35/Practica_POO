
from tkinter import *
import tkinter
from cuenta import *

cu = Cuenta(numero="",titular="",edad="",saldo="",)   



def mandar ():
    
    cu.depositar(cantidad.get())
    








ventana = tkinter.Tk()
ventana.title("CAJA POPULAR")
ventana.geometry('340x440')
ventana.configure(bg = 'white')



ingresar = tkinter.Label(ventana,text="Ingresar",bg="#FFFFFF", font="Arial, 30")
ingresar.grid(row = 0, column = 0, columnspan = 2, pady = 40)
cantidad = tkinter.Entry(ventana)
cantidad.grid(row= 1,column =0, columns=2,pady=40)

depositarboton = tkinter.Button(ventana, text="Ingresar Varo", bg="white",command=mandar)
depositarboton.grid(row = 2, column = 0, columnspan = 2, pady = 30)












ventana.mainloop()