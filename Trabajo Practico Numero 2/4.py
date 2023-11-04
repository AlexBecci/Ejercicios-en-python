import random
#palabras para jugar al ahorcado
palabras = [
    "computadora", "programación", "desarrollo", "inteligencia", "python", "algoritmo", "software", "hardware", "lenguaje", "base",
    "datos", "depuración", "pantalla", "internet", "navegador", "servidor", "encriptación", "seguridad", "documento", "gráficos",
    "código", "variable", "función", "memoria", "ejecución", "compilador", "depurador", "programador", "instrucción", "implementación",
    "matriz", "bucle", "condición", "depuración", "programable", "estructura", "comunicación", "sistema", "aplicación", "interfaz",
    "archivo", "protocolo", "rendimiento", "rendimiento", "error", "optimización", "administración", "rendimiento", "resolución",
    "depuración"
]
categoria="Tecnología de la Información"
palabra_secreta = random.choice(palabras)

# Inicializar variables
intentos_restantes = 6
letras_adivinadas = []


# Función para mostrar la palabra oculta con letras adivinadas
def mostrar_palabra(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

# Función para dibujar el ahorcado
def dibujar_ahorcado(intentos_restantes):
    ahorcado = [
        "  +---+",
        "  |   |",
        "      |",
        "      |",
        "      |",
        "      |",
        "========="
    ]
    if intentos_restantes < 6:
        ahorcado[2] = "  |   O"
    if intentos_restantes < 5:
        ahorcado[3] = "  |   |"
    if intentos_restantes < 4:
        ahorcado[4] = "  |  /|\\"
    if intentos_restantes < 3:
        ahorcado[5] = "  |  / \\"
    for linea in ahorcado:
        print(linea)

# Comienza el juego
print("Bienvenido al juego del Ahorcado!")
while True:
    print("\nPalabra: " + mostrar_palabra(palabra_secreta, letras_adivinadas))
    dibujar_ahorcado(intentos_restantes)
    letra = input("Adivina una letra: ").lower()
    
    if letra in letras_adivinadas:
        print("Ya adivinaste esa letra.",)
        
    else:
        letras_adivinadas.append(letra)
        if letra in palabra_secreta:
            print("¡Adivinaste una letra!")
        else:
            print("Letra incorrecta.")
            intentos_restantes -= 1

    if intentos_restantes == 0:
        print("\n¡Has perdido! La palabra era: " + palabra_secreta)
        break

    if set(letras_adivinadas) == set(palabra_secreta):
        print("\n¡Felicidades! ¡Has ganado! La palabra era: " + palabra_secreta)
        break