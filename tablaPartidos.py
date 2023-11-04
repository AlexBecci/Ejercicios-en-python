# -*- coding: utf-8 -*-

#Elaborar un algoritmo que permita ingresar el número de partidos ganados, perdidos y empatados, por ABC club en el torneo apertura, se debe de mostrar su puntaje total, teniendo en cuenta que por cada partido ganado obtendrá 3 puntos, empatado 1 punto y perdido 0 puntos.


nombreEquipo = input("Ingrese nombre de club: ")
 
partidosGanados = int(input("Ingrese el número de partidos ganados: "))
partidosPerdidos = int(input("Ingrese el número de partidos perdidos: "))
partidosEmpatados = int(input("Ingrese el número de partidos empatados: "))

puntosGanados = partidosGanados*3
puntosPerdidos = partidosPerdidos*0
puntosEmpatados = partidosEmpatados*1

puntaje = puntosGanados + puntosEmpatados+ puntosPerdidos

print("Puntaje Total de ", nombreEquipo,": ", puntaje)
