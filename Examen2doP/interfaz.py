
from tkinter import *
from Ex import *

val = Registro()

def mandar ():
    
    val.agregar(miEntry.get(),miEntry2.get(),miEntry3.get(),miEntry4.get(),miEntry5.get())



#ventana

ventana = Tk()

ventana.title("Examen")


#frame

miFrame = Frame(ventana, width=1200, height=600)


#label entry y botones

miLabel = Label(miFrame, text="Nombre")

miLabel.place(x=100, y=100)

miLabel2 = Label(miFrame, text="Apellido Paterno")

miLabel2.place(x=100, y=150)

miLabel3 = Label(miFrame, text="Apellido Materno")

miLabel3.place(x=100, y=200)

miLabel4 = Label(miFrame, text="Año de nacimiento")

miLabel4.place(x=100, y=250)

miLabel5 = Label(miFrame, text="Carrera")

miLabel5.place(x=100, y=300)




#entry

miEntry = Entry(miFrame)

miEntry.place(x=200, y=100)

miEntry2 = Entry(miFrame)

miEntry2.place(x=200, y=150)

miEntry3 = Entry(miFrame)

miEntry3.place(x=200, y=200)

miEntry4 = Entry(miFrame)

miEntry4.place(x=200, y=250)

miEntry5 = Entry(miFrame)

miEntry5.place(x=200, y=300)



#botones

miBoton = Button(miFrame, text="Enviar",command=mandar)

miBoton.place(x=100, y=400)



miFrame.pack()



ventana.mainloop()

