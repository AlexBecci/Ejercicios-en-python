# -*- coding: utf-8 -*-

tamanioVector = 10

vectorOriginal=[]
vectorInverso = []

for i in range(tamanioVector):
    valor = int(input(f"Ingrese valor para la posicion {i + 1}: "))
    vectorOriginal.append(valor)


for i in range(tamanioVector -1,-1,-1):
    vectorInverso.append(vectorOriginal[i])

print("Vector original: ",vectorOriginal )

print("Vector Inverso: ",vectorInverso)