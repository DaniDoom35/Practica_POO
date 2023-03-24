from tkinter import messagebox

import sqlite3

import bcrypt 

class controladorBD:
    
    def __init__(self):
        pass
    
    #1. Preparamos la conexion para usarla cuando sea necesario.
    def conexionBD(self):
        try:
            
            conexion= sqlite3.connect("C:/Users/iSkye/Documents/GitHub/Practica/P3/TKINTER_SQLite/DBRegistrados.db")
            print("Conectado con exito")
            return conexion
            
        except sqlite3.OperationalError:
            
            print("Fallo en la conexion")
            
            
     #.Metodo  para insertar       
    def guardarUsuario(self,nom,cor,con):
        
        #1. Primer paso para insertar es llamar a la conexion.
        conx = self.conexionBD()
        
        #2. Revisar que los parametros no esten vacios
        
        if (nom == "" or cor == "" or con == ""):
            messagebox.showwarning("CUIDADO","Revisa tus datos")
            conx.close()
        else:
            #3. Preparamos los datos y los query SQL
            
            cursor = conx.cursor()
            conH= self.encriptarCon(con)
            datos=(nom,cor,conH)
            qrInsert="insert into TBRegistrados(correo,contra,nombre) values(?,?,?)"
            
            
            
            #4. Proceder a insertar
            
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("EXITO","Se guardo el usuario")
            
            
    def encriptarCon(self,con):
        
        conPlana= con
        conPlana = conPlana.encode() #Convertir contraseña a Bytes
        sal= bcrypt.gensalt()
        conHa= bcrypt.hashpw(conPlana,sal)
        print(conHa)
              
        return conHa
            
    