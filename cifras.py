import random, re, os
from getpass import getpass


def jugar():
    inicializar_cifras()
    dificultad = preguntar_dificuldad()
    numeros_pequeños = preguntar_numeros_pequeños()
    objetivo, cifras_disponibles = jugar_cifras(dificultad, numeros_pequeños)
    mostrar_resultados(objetivo, cifras_disponibles)
    getpass(prompt="Presiona Enter para volver...")


def generar_datos_jugador(dificultad=None, numeros_pequeños=None):
    """
    Genera el número a alcanzar.
    
    Argumentos opcionales:
    - Dificultad: Recibe un int entre 1 y 5, que será el número de pasos que el algoritmo hará para generar un objetivo.
    """
    if not dificultad:
        return random.randint(100, 999), generar_cifras_disponibles(numeros_pequeños)

    exito = False

    while not exito:
        # Se genera la lista de números disponibles cada intento
        cifras_disponibles = generar_cifras_disponibles(numeros_pequeños)
        cifras_disponibles_return = cifras_disponibles.copy()
        # Se elige el número del que partir y lo elimina de la cifras_disponibles
        operando1 = random.choice(cifras_disponibles)
        cifras_disponibles.remove(operando1)

        # Se inicia un bucle que se repite tantas veces como dificultad se haya pedido, 1-5
        for _ in range(dificultad):
            # Se elige una operación al azar y un segundo operando
            operacion  = random.choice(OPERACIONES)
            operando2 = random.choice(cifras_disponibles)
            
            if verificar_operacion_generador(operando1, operacion, operando2):
                operando1 = int(operar(operando1, operacion, operando2))
                cifras_disponibles.remove(operando2)
                exito = True
            else:
                exito = False
                break
        if exito == True:
            return operando1, cifras_disponibles_return
        

def verificar_operacion_generador(operando1, operacion, operando2):
    """Verifica si la operación que se desea hacer está dentro de los límites, para uso del algoritmo de generación."""
    if operacion == "/":
        return True if operando1 % operando2 == 0 and 100 <= operar(operando1, operacion, operando2) <= 999 else False
    return 100 <= operar(operando1, operacion, operando2) <= 999


def generar_cifras_disponibles(numeros_pequeños=None):
    """
    Genera una lista aleatoria con los 6 números pertenecientes a la lista de cifras posibles.
    Recoge un parámetro opcional `numeros_pequeños`, que indica la cantidad de números pequeños que habrá en la lista de salida
    """
    if numeros_pequeños or numeros_pequeños == 0:
        return random.choices(CIFRAS_PEQUEÑAS_POSIBLES, k=numeros_pequeños) + random.choices(CIFRAS_GRANDES_POSIBLES, k=6-numeros_pequeños)
    return random.choices(CIFRAS_POSIBLES, k=6)


def verificar_operacion_jugador(entrada):
    """Devuelve True si la operación introducida tiene el formato correcto"""
    return True if re.search(r"^(\d+) ?([+|\-|*|/]) ?(\d+)$", entrada) else False


def extraer_operacion(entrada):
    """Devuelve una lista con el primer número de la operación, el símbolo de operación, y el segundo número de la operación"""
    operacion = [i for i in re.search(r"^(\d+) ?([+|\-|*|/]) ?(\d+)$", entrada).groups()]
    return [int(operacion[0]), operacion[1], int(operacion[2])]


def actualizar_lista(operacion, cifras):
    """
    Actualiza la lista de cifras disponibles.

    Argumentos:
    - `operacion`, un string con la operación que se ha hecho, los dos operandos tienen que estar entre las cifras disponibles
    - `cifras`, una lista que contiene las cifras disponibles para hacer operaciones

    Devuelve la lista actualizada con la operación hecha
    """

    if not verificar_operacion_jugador(operacion):                  # Si la operación no es válida
        print("La operación introducida no es correcta")
        return

    operando1, simbolo, operando2 = extraer_operacion(operacion)
    if not (operando1 in cifras and operando2 in cifras):           # Si cualquiera de los operandos no está en cifras
        print("Las cifras no están entre las cifras disponibles")
        return
    
    if simbolo == "/" and operando1 % operando2 != 0:               # Si la operación es una división y ésta no es entera
        print("La división tiene que ser entera")
        return
    
    if operar(operando1, simbolo, operando2) < 0:
        print("La resta no puede ser negativa")
        return

    cifras.append(operar(operando1, simbolo, operando2))

    cifras.remove(operando1)
    cifras.remove(operando2)

    return cifras


def calcular_distancia(cifras_disponibles, objetivo):
    """Devuelve la diferencia entre el objetivo y el número más cercano a éste"""
    distancia = objetivo - cifras_disponibles[0]
    for cifra in cifras_disponibles:
        if abs(objetivo - cifra) < distancia:
            distancia = abs(objetivo - cifra)
    return distancia


def operar(operando1, operacion, operando2):
    """Devuelve el resultado de una operación, siendo `operando1` y `operando2` números y `operacion` la operación que se desea hacer"""
    match operacion:
        case "+":
            return operando1 + operando2
        case "-":
            return operando1 - operando2
        case "*":
            return operando1 * operando2
        case "/":
            return operando1 / operando2


def inicializar_cifras():
    """Inicializa las reglas que usarán las demás funciones: `cifras_pequeñas`, `cifras_grandes`, `cifras_posibles` y `operaciones`"""
    global CIFRAS_PEQUEÑAS_POSIBLES
    global CIFRAS_GRANDES_POSIBLES
    global CIFRAS_POSIBLES
    global OPERACIONES
    CIFRAS_PEQUEÑAS_POSIBLES = (tuple(range(1,11)))
    CIFRAS_GRANDES_POSIBLES = (25, 50, 75, 100)
    CIFRAS_POSIBLES = CIFRAS_PEQUEÑAS_POSIBLES + CIFRAS_GRANDES_POSIBLES
    OPERACIONES = ("+", "-", "/", "*")



def preguntar_dificuldad():
    while True:
        try:
            dificultad = int(input("Selecciona dificultad (1-5).\nCtrl-Z + Enter para usar el algoritmo antiguo.\n" 
                                   if os.name == "nt" else
                                   "Selecciona dificultad (1-5).\nCtrl-C para usar el algoritmo antiguo.\n"))
            if not (1 <= dificultad <= 5):
                raise Exception
            break
        except EOFError:
            dificultad = None
            break
        except Exception:
            continue
    return dificultad


def preguntar_numeros_pequeños():
    while True:
        try:
            numeros_pequeños = int(input("Elige la cantidad de números pequeños (Entre 1 y 10) que quieras\nCtrl-Z + Enter para una selección aleatoria\n"
                                         if os.name == "nt" else
                                         "Elige la cantidad de números pequeños (Entre 1 y 10) que quieras\nCtrl-C para una selección aleatoria\n"))
            if 0 <= numeros_pequeños <= 6:
                break
        except EOFError:
            numeros_pequeños = None
            break
        except Exception:
            print("La cantidad debe estar entre 0 y 6")
            continue
    return numeros_pequeños


def jugar_cifras(dificultad, numeros_pequeños):
    objetivo, cifras_disponibles = generar_datos_jugador(dificultad, numeros_pequeños)

    while len(cifras_disponibles) != 1 and not objetivo in cifras_disponibles:
        try:
            print(f"Objetivo: {objetivo}")
            print(f"Cifras disponibles:{cifras_disponibles}")
            print("Introduce tu palabra. Ctrl-Z + Enter para terminar." 
                  if os.name == "nt" else
                  "Introduce tu palabra. Ctrl-C para terminar.")
            actualizar_lista(input(), cifras_disponibles)
        except EOFError:
            break
    return objetivo, cifras_disponibles


def mostrar_resultados(objetivo, cifras_disponibles):
    if objetivo in cifras_disponibles:
        print("¡Enhorabuena! Has llegado al objetivo")
    else:
        print("¡Mala suerte! No has llegado al objetivo")
        print(f"Distancia: {calcular_distancia(cifras_disponibles, objetivo)}")


if __name__ == "__main__":
    jugar()