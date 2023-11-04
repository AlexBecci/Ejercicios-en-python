#Modificar el algoritmo anterior para que el programa maneje un menú de opciones que permite solo la carga de números comprendidos entre 1 y 50. Debe validar y para la carga manual en caso de escribir un número fuera de rango debe volver a pedirlo. 

#1 - Carga Manual
#2 - Carga aleatoria 
#3 - Invertir Vector 
#4 - Salir 


# -*- coding: utf-8 -*-
import random

tamanioVector = 10

vectorOriginal=[]
vectorInverso = []

menu = True

def menuOptions(option):
    if(option == 1):
        vectorOriginal.clear()
        for i in range(tamanioVector):
            valor = int(input(f"Ingrese valor, comprendido entre 1 y 50 para la posicion {i + 1}: "))
            if(valor >= 1 and valor <=50):
                vectorOriginal.append(valor)
            else:
                print("Valor erroneo, el valor que debe ingresar tiene que estar comprendido entre 1 y 50. El numero ingresado que fue ingresado era: ", valor)
                tamanioVector -1
        print("Vector original: ",vectorOriginal )

    elif(option ==2):
        vectorOriginal.clear()
        for i in range(tamanioVector):
            valor = random.randint(1, 50)
            vectorOriginal.append(valor)
        print("Vector original: ",vectorOriginal )

    elif(option ==3):
        vectorInverso.clear()
        if(vectorOriginal==[]):
            print("El vector esta vacio, primero tienes que llenarlo")
        else:
            for i in range(tamanioVector -1,-1,-1):
                vectorInverso.append(vectorOriginal[i])
                
            print("Vector original: ",vectorOriginal )
            print("Vector invertido: ", vectorInverso)
    
    elif(option ==4):
        print("Saliendo del programa.")
        
        

    else:
        print("Option invalida, por favor coloque una opcion valida entr 1 y 4")


def main():
    while menu ==True:

        print("# 1 - Carga Manual")
        print("#2 - Carga aleatoria ")
        print("#3 - Invertir Vector ")
        print("#4 - Salir ")

        option = int(input("Ingrese la opcion deseada: "))
        menuOptions(option)
        if(option == 4):
            break

    


#print("Vector Inverso: ",vectorInverso)        





main()