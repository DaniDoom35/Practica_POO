from tkinter import messagebox
import random



class Registro ():
    
    
    def __init__(self):
        
        pass

        
        
        
    def agregar (self,miEntry,miEntry2,miEntry3,miEntry4,miEntry5):
        
        
     a = miEntry[:1]   #nombre 
     b = miEntry2[:3]   #apellido paterno
     c = miEntry3[:3]   #apellido materno
     d = miEntry4[-2:]  #Año
     e = miEntry5[:3]   #Carrera
     
     n = 23
     
     r = "0,1,2,3,4,5,6,7,8,9" #Ramdom
        
     r = list(r)
        
     
     r = random.choice(r)
     

        

     messagebox.showinfo("Exito",e+str(n)+d+a+b+c+r)
     
     

     




    

        