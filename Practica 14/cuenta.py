from tkinter import *



class Cuenta :
    
    def __init__(self,numero,titular,edad,saldo):
        
        self.__numero = numero
        self.__titular = titular
        self.__eded = edad
        self.__saldo = saldo
        
    
    def depositar (self,cantidad) :
        
        self.__saldo += cantidad
        
        
        print("Hola")
        print(cantidad)
        
    def retirar (self,cantidad):
        
        self.__saldo -= cantidad
        
        
    def tranferir (self,cantidad,otra):
        
        self.retirar(cantidad)
        otra.depositar(cantidad)
        