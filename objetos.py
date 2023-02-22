from Personaje import *

#!.Crear objeto de la clase Personaje

heroe = Personaje()

#2. usar atributos

print("El personaje se llama: " + heroe.nombre)
print("Pertenece a la especie: " + heroe.especie)
print("Y tiene una altura de: " + heroe.altura)

#3. Usar metodos

heroe.correr(true)
heroe.lanzarGranadas()
heroe.recargaArmaI(87)

