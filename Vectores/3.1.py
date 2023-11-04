#Realizar un programa que cargue un vector de 15 posiciones.
# -*- coding: utf-8 -*-

import array as arr




def main():
    vector = arr.array('d',[])
    for i in range(0,15,1):
        valor = int(input("Ingresa un valor para el vector "))
        vector.append(valor)
        print(vector)


main()