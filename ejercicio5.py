#Elaborar un algoritmo que permita calcular el número de micro discos 3 .5 necesarios para hacer una copia de seguridad, de la información almacenada en un disco cuya capacidad se conoce.Hay que considerar que el disco duro está lleno de información,además expresado en gigabyte. Un micro disco tiene 1.4 megabyte y un gigabyte es igual a 1,024 megabyte.(Vinuesa,

# -*- coding: utf-8 -*-
import math 
#librería necesaria para usar funciones Matemáticas
#en este caso math.ceil(), que redondea un numero al Entero superior
#Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("Ejercicio5: NÚMERO DE MICRO DISCOS 3.5 NECESARIOS")
print("-------------------------------------------------------")
#Entradas
print("Ingrese GB: ")
GB = float( input())
#Proceso
MG = GB*1024
MD = MG/1.44
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print(MD)
#En caso de Decimal Aproximar al siguiente entero
#Ya que la parte decimal debe ser almacenada en otro DISCO 3.5
print("Numero de Discos necesarios: ", math.ceil(MD))