#Dado un arreglo de 4 elementos enteros determinar si es un palíndromo  (se lee igual de adelante hacia atrás / capicua).

def es_palindromo(arreglo):
    if len(arreglo) != 4:
        print('# El arreglo no tiene 4 elementos, no puede ser un palíndromo')
        return False  
    
    # Comparar los elementos
    if arreglo[0] == arreglo[3] and arreglo[1] == arreglo[2]:
        print("# Es un palíndromo")
        return True  # Es un palíndromo
    else:
        print("No es palíndromo")
        return False  # No es un palíndromo

arreglo = []


def main():
    for i in range(1,5,1):
        valor = int(input(f"Ingrese el elemento {i}, entero para el arreglo: "))
        arreglo.append(valor)
    
    print(arreglo)
    es_palindromo(arreglo)
main()