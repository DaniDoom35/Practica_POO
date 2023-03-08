import tkinter
from tkinter import ttk,messagebox,Tk
from passclass import *

 




def show_selection():
   
    selection = combo.get()
    messagebox.showinfo(
        message=f"La opción seleccionada es: {selection}",
        title="Selección"
    )
ventana = tkinter.Tk()
ventana.geometry('340x440')




pass_label = tkinter.Label(ventana, text = "Contraseña",bg= "#FFFFFF",font="Arial, 16")
pass_entrada = tkinter.Entry(ventana)
pass_label.grid (row = 1, column = 0)
pass_entrada.grid(row = 1, column = 1, pady = 20)



ventana.title("Combobox")
combo = ttk.Combobox(
    state="readonly",
    values=["1", "2", "3", "4", "5", "6","7","8"]
)
combo.place(x=50, y=50)
button = ttk.Button(text="Mostrar selección", command=show_selection)
button.place(x=50, y=100)






ventana.mainloop()
















ventana.mainloop()


