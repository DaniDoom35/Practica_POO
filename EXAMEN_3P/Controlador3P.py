from tkinter import messagebox

import sqlite3

class controladorMT:
    

    def __init__(self):
        pass
    
    #1. Preparamos la conexion 
    def conexionBD(self):
        try:
            
            conexion= sqlite3.connect("C:/Users/iSkye/Documents/GitHub/Practica/EXAMEN_3P/Ferreteria.db")
            print("Conectado con exito")
            return conexion
        
        except sqlite3.OperationalError:
            
            print("Fallo en la conexion")
            
            
   
        
    def guardarMaterial(self,mat,can):
        
   
        conx = self.conexionBD()
        
        
      
        
        if (mat == "" or can == ""):
            
            messagebox.showwarning("CUIDADO","Revisa tus datos")
            conx.close()
            
            
        else:
           
            
            cursor = conx.cursor()
            datos=(mat,can)
            qrInsert="insert into MatConstruccion(Material,Cantidad) values(?,?)"
      
            print(mat,can)
          
            
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("EXITO","Se guardo el material")
        
        
        
      