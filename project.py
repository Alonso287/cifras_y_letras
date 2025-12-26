import cifras, letras, os, sys
from getpass import getpass

def main():
    inicializar_datos()
    while True:
        respuesta = home()
        match respuesta:
            case "1":
                print(respuesta)
            case "2":
                print(respuesta)
            case "3":
                como_jugar()
            case "4":
                sys.exit()

def home():
    os.system("cls")
    print(HOME)
    try:
        respuesta = input()
    except EOFError:
        sys.exit()
    return respuesta

def como_jugar():
    os.system("cls")
    print(COMO_JUGAR)
    getpass(prompt="")

def negrita(texto):
    return f"\033[1m{texto}\033[0m"

def azul(texto):
    return f"\033[36m{texto}\033[0m"

def subrayar(texto):
    return f"\033[4m{texto}\033[0m"

def inicializar_datos():
    global ANCHO
    ANCHO = os.get_terminal_size()[0]
    global HOME
    HOME = (azul(negrita("CIFRAS Y LETRAS".center(ANCHO))) 
    + "Creado por Alonso Navarro".center(ANCHO) + "\n"
    + "\n"
    + negrita("Opciones".center(ANCHO) + "\n")
    + "\n"
    + "1. Jugar a Cifras".center(ANCHO) + "\n"
    + "2. Jugar a Letras".center(ANCHO) + "\n"
    + "3. Cómo Jugar".center(ANCHO) + "\n"
    + "4. Salir".center(ANCHO) + "\n")

    global COMO_JUGAR
    COMO_JUGAR = (azul(negrita("CIFRAS Y LETRAS".center(ANCHO))) 
    + "Creado por Alonso Navarro".center(ANCHO) + "\n"
    + "\n"
    + negrita("Cómo jugar".center(ANCHO) + "\n")
    + """
Cifras y letras es un programa de televisión español de preguntas y respuestas, basado en el programa francés Des chiffres et des lettres creado por Armand Jammot.
Existen dos modos de juego: Cifras y Letras.
    - En el modo de juego \"Cifras\" se muestran 6 números aleatorios entre el 1 y el 10 o también 25, 50, 75 o 100; y otro número entre 100 y 999 que hay que alcanzar usando las operaciones matemáticas básicas (suma, resta, multiplicación y división). Podrás elegir la cantidad de números pequeños (Es decir, entre 1 y 10) que quieres antes de comenzar la ronda.
    - En el modo de juego \"Letras\" elegirás al principio de la prueba cuántas vocales quieres de un grupo de 10 letras, entre un mínimo de 3 y un máximo de 6, y tu objetivo será encontrar la palabra más larga
    
Presiona Enter para volver""")

if __name__ == "__main__":
    main()