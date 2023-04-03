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
    
    # Metodo consulta usuario
    
    def consultaUsuario(self,id):
        
        #1. Prepara la conexion
        
        conx = self.conexionBD()
        

        #2. Verificar que el ID no este vacio
        
        if( id == ""):
            messagebox.showwarning("CUIDADO","Revisa tus datos")
            conx.close()
        else:
            
            #3. Proceder a buscar
            
            try:
                #4. Prepara lo necesario para el select
                
                cursor = conx.cursor()
                sqlSelect="select * from TBRegistrados where id = "+id
               
                
                #5. Ejecucion y guardado de la consulta

                
                cursor.execute(sqlSelect)
                RSusuario= cursor.fetchall()
                conx.close()
                
                
                return RSusuario
                
            
            except sqlite3.OperationalError:
                print("Fallo en la consulta") 
    
    
    # Metodo para consultar ususario
    
    def consultaUsuario2(self):
        
        conx = self.conexionBD()
        
        try:
        
            cursor = conx.cursor()
            sqlSelect1="select * from TBRegistrados"

            cursor.execute(sqlSelect1)
            aUsuario= cursor.fetchall()
            conx.close()
            
            
        except sqlite3.OperationalError:
            print("Fallo en la consulta")
            
            
    # Metodo Para actualizar usuario
    
    def actualizarUsuario(self,id,nom,cor,con):
        
        #1. Prepara la conexion
        
        conx = self.conexionBD()
        
        #2. Verificar que los parametros no esten vacios
        
        if (id == "" or nom == "" or cor == "" or con == ""):
            messagebox.showwarning("CUIDADO","Revisa tus datos")
            conx.close()
        else:
            
            #3. Prepara los datos y los query SQL
            
            cursor = conx.cursor()
            datos=(nom,cor,con,id)
            qrUpdate="update TBRegistrados set nombre = ?,correo = ?,contra = ? where id = ?"
            
            #4. Proceder a actualizar
            
            cursor.execute(qrUpdate,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("EXITO","Se actualizo el usuario")
            
    
                
        
        