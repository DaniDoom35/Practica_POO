class Personaje:
    
    #Definimos el constructor de personaje
    def __init__(self,esp,nom,alt): 
        
        #Atributos
         self.__especie = esp   #Inicializacion de atributos 
         self.__nombre = nom   #Inicializacion de atributos
         self.__altura = alt   #Inicializacion de atributos
         
        
    
    #Metodos del personaje
    
    def correr(self,status):
        if(status):
            print("El personaje " + self.__nombre + " Esta corriendo")
            
        else:
            print("El personaje " + self.__nombre + " Se detuvo")
            
            
    def lanzarGranadas(self):
        print("El personaje " + self.__nombre + " Utilizo una granada")
        
    def recargaArma(self,ammo):
        print("El personaje " + self.__nombre + " a recargado " + str(ammo) + " de municion")
        
        
        
    def __pensar(self):
        print(" Hello There ")
        
        #Declarar GETTERS y SETTS
        
    def getnombre(self):
        return self.__nombre
    
    def setnombre(self,nom):
        self.__nombre = nom
        
        
           
    def getespecie(self):
        return self.__especie
    
    def setespecie(self,esp):
        self.__especie = esp
        
        
          
    def getaltura(self):
        return self.__nombre
    
    def setaltura(self,alt):
        self.__altura = alt
        
        
        
           
        
        
    
    

    
    