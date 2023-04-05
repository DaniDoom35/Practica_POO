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
      
            print(nom,cor,con)
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
    
    def consultaUsuarios(self):
        
        conx = self.conexionBD()
        
        try:
        
            cursor = conx.cursor()
            sqlSelect1="select * from TBRegistrados"

            cursor.execute(sqlSelect1)
            rsUsuario= cursor.fetchall()
            conx.close()
            
            return rsUsuario
            
        except sqlite3.OperationalError:
            
            print("Fallo en la consulta")    

            
            


            
            
    # Metodo Para actualizar usuario
    
    def actualizarUsuario(self,id,nom2,cor2,con2):
        
        
        conx = self.conexionBD()
        
        if (id == "" or nom2 == "" or cor2 == "" or con2 == ""):
            messagebox.showwarning("CUIDADO","Revisa tus datos")
            conx.close()
        else:
            
            cursor = conx.cursor()
            sqlUpdate="update TBRegistrados set nombre = '"+nom2+"', correo = '"+cor2+"', contra = '"+con2+"' where id = "+id
            cursor.execute(sqlUpdate)
            conx.commit()
            messagebox.showinfo("EXITO","Se actualizo el usuario")
            conx.close()
    
    
    
            
    # confirmación antes de Eliminar un registro
    
    def eliminarusuario(self,id):
        
        conx = self.conexionBD()
        
        if (id == ""):
            messagebox.showwarning("CUIDADO","Revisa tus datos")
            conx.close()
        else:
            
            respuesta = messagebox.askquestion("Eliminar","¿Deseas eliminar el registro?")
            
            if(respuesta == "yes"):
                
               
                cursor = conx.cursor()
                sqlDelete="delete from TBRegistrados where id = "+id
                cursor.execute(sqlDelete)
                conx.commit()
              
                messagebox.showinfo("EXITO","Se elimino el usuario")
        
        
                conx.close()
             
                
            else:
                
                # Messagebox no se elimino el registro
                
                messagebox.showinfo("INFO","No se elimino el usuario")
                conx.close()
                