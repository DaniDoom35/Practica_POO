from Personaje import *

#1. Solicitar Datos Heroe

print("")
print("####### Datos Heroe ####")
especieH = input("Escribe la especie del Heroe: ")
nombreH = input("Escribe el nombre del Heroe: ")
alturaH = float(input("Escribe la altura del Heroe: "))
recargarH = int(input("Cuantas Balas recargas al Heroe: "))

#1.2. Solicitar Datos Villano

print("")
print("####### Datos Villano ####")
especieV = input("Escribe la especie del Villano: ")
nombreV = input("Escribe el nombre del Villano: ")
alturaV = float(input("Escribe la altura del Villano: "))
recargarV = int(input("Cuantas Balas recargas al Villano: "))


#2. Crar objeto de clase Personaje

heroe = Personaje(especieH,nombreH,alturaH)
villano = Personaje(especieV,nombreV,alturaV)



#3. usar atributos


print("")
print("####### Objeto Heroe ####")
print("El personaje se llama: " + heroe.nombre)
print("Pertenece a la especie: " + heroe.especie)
print("Y tiene una altura de: " + str(heroe.altura))


print("")
print("####### Objeto Villano ####")
print("El personaje se llama: " + villano.nombre)
print("Pertenece a la especie:asd " + villano.especie)
print("Y tiene una altura de: " + str(villano.altura))


#3. Usar metodos

heroe.correr(True)
heroe.lanzarGranadas()
heroe.recargaArma(recargarH)

villano.correr(False)
villano.lanzarGranadas()
villano.recargaArma(recargarV)

