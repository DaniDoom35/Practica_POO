from tkinter import Tk,Button,Frame,messagebox


#5. Declaramos funciones
def mostrarmensajes():
    messagebox.showinfo("Aviso", "Presionaste el boton")
    messagebox.showerror("Error: ", "Todo Fallo con exito")
    print(messagebox.askyesno("Una Question", "¿Le vas al America?"))
    
#6.  Creamos una funcion para agregar botones para los mensajes
def agregarbton():
    botonnaranja.config(text ="+",bg="green",fg="white")
    botonNuevo = Button(seccion3, text="Nuevo")
    botonNuevo.pack()


#1. Instaciamos el objeto llamado "Ventana"

ventana = Tk()
ventana.title("Ejemplo de 3 Frames ")
ventana.geometry("600x400")


#2. Agregamos los Frames

seccion1 = Frame(ventana,bg = "blue")
seccion1.pack(expand = True, fill = 'both')

seccion2 = Frame(ventana,bg = "yellow")
seccion2.pack(expand = True, fill = 'both')

seccion3 = Frame(ventana,bg = "purple")
seccion3.pack(expand = True, fill = 'both')

#3. Agregamos botones

botonazul = Button(seccion1, text = "HOLA", fg = "blue", command = mostrarmensajes)
botonazul.place(x = 60, y = 60)

botonrojo = Button(seccion2, text = "HOLA ROJO", fg = "white", bg = "#FF2A00")
botonrojo.grid(row = 0, column = 0 )

botonverde = Button(seccion2, text = "HOLA ROJO", fg = "white", bg = "#56FF20")
botonverde.grid(row = 1, column = 1 )

botonnaranja = Button(seccion3, text = "HOLA NARANJA", fg = "white", bg = "#FF7000", command=agregarbton)
botonnaranja.configure(height = 2,width=10)
botonnaranja.pack()

#4. Posicionamiento de elementos 

#Final. Llamamos a su main (Tiene que ir al final del codigo)

ventana.mainloop()
