
from tkinter import messagebox


class validar :
    
    
    def __init__(self):
        
        self.__correo = "halo@outlook.com"
        self.__contra = "1234"
        

    
    def login_validacion (self,usuario_entrada,pass_entrada):
        
        if self.__correo == usuario_entrada and self.__contra == pass_entrada:
            
            messagebox.showinfo("Exito","Bienvenido")
            
        else:
             
            messagebox.showerror("ACCESO DENEGADO","Verifica tus datos")
        
        
        
        
