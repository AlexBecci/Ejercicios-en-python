# -*- coding: utf-8 -*-

#Se necesita elaborar un algoritmo que solicite el
#número de respuestas correctas, incorrectas y en blanco,
#correspondientes a postulantes, y muestre su puntaje final
#considerando que por cada respuesta correcta tendrá
#3 puntos, respuestas incorrectas tendrá -1 y respuestas en
#blanco tendrá 0.

correctResponse = int(input("Ingrese respuestas correctas: "))
incorrectResponse = int(input("Ingrese respuestas incorrectas: "))

notFoundResponse = int(input("Ingrese respuestas en blanco: "))

correctPoint= correctResponse*3
incorrectPoint= incorrectResponse*-1
notFoundPoint = notFoundResponse*0

print("puntaje final: ",(correctPoint + incorrectPoint + notFoundPoint))