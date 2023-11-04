#Un punto en el plano tiene dos coordenadas (X ,Y), entonces el
#punto A tendrá sus coordenadas (AX, AY) y el punto B de
#manera similar (BX, BY), luego se tiene los siguientes datos:
#Entrada Identificador
#Coordenada X de A AX
##Coordenada Y de A AY
#Coordenada X de B BX
#Coordenada Y de B BY

#Salida
#Distancia entre el punto A y B D
#Para determinar la distancia entre dos puntos, empleamos la
# matemática siguiente:
#D = √(AX − BX)2 + (AY − BY)2

print('Ingrese cordenadas de A: ')
ax = float(input("AX: "))
ay = float(input("AY: "))

print('Ingrese cordenadas de B: ')
bx = float(input("BX: "))
by = float(input("BY: "))

distance = ((ax-bx)**2 + (ay-by)**2)**0.5

print("La distancia desde el punto A a el punto B es: ", distance)
