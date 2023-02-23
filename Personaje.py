class Personaje:
    
    #Definimos el constructor de personaje
    def __init__(self,esp,nom,alt): 
        
        #Atributos
         self.especie = esp   #Inicializacion de atributos 
         self.nombre = nom   #Inicializacion de atributos
         self.altura = alt   #Inicializacion de atributos
         
        
        
    
        
    
    
    
    
    #Metodos del personaje
    
    def correr(self,status):
        if(status):
            print("El personaje " + self.nombre + "Esta corriendo")
            
        else:
            print("El personaje " + self.nombre + "Se detuvo")
            
            
    def lanzarGranadas(self):
        print("El personaje " + self.nombre + "Utilizo una granada")
        
    def recargaArma(self,ammo):
        print("El personaje " + self.nombre + "a recargado " + str(ammo) + " de municion")
        
        
        
        
        
    
    

    
    