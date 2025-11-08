import random
import re


def main():
    cifras_posibles = generar_cifras_posibles()
    while True:
        try:
            dificultad = int(input("Selecciona dificultad (1-5). Ctrl-D para usar el algoritmo antiguo.\n"))
            if not (1 <= dificultad <= 5):
                raise Exception
            break
        except EOFError:
            dificultad = None
            break
        except Exception:
            continue
    while not (objetivo := generar_objetivo(dificultad, cifras_disponibles :=generar_cifras_disponibles(cifras_posibles))):
        objetivo = generar_objetivo(dificultad, cifras_disponibles)
        cifras_disponibles = generar_cifras_disponibles(cifras_posibles)

    print(f"Cifras posibles: {cifras_posibles}")

    while len(cifras_disponibles) != 1 and not objetivo in cifras_disponibles:
        try:
            print(f"Objetivo: {objetivo}")
            print(f"Cifras disponibles:{cifras_disponibles}")
            print("Ctrl-D para terminar.")
            actualizar_lista(input(), cifras_disponibles)
        except EOFError:
            break

    if objetivo in cifras_disponibles:
        print("Enhorabuena! Has llegado al objetivo")
    else:
        print("Mala suerte! No has llegado al objetivo")
        print(f"Distancia: {calcular_distancia(cifras_disponibles, objetivo)}")


def generar_cifras_posibles():
    """Devuelve una lista con los números del 1-10 y 35, 50, 75 y 100"""
    return list(range(1, 11)) + [25, 50, 75, 100]


def generar_objetivo(dificultad=None, cifras_disponibles=None):
    """
    Genera el número a alcanzar
    
    Argumentos opcionales:
    - Dificultad: Recibe un int, y es el número de pasos que el algoritmo hará para generar un objetivo a partir de la lista de números disponibles obtenida. Tiene que estar entre 0 y 5.
    """
    cifras_disponibles = cifras_disponibles.copy()
    if dificultad == None or cifras_disponibles == None:
        return random.randint(100, 999)
    
    operaciones = ["+", "-", "/", "*"]
    cifras_disponibles.remove(objetivo := random.choice(cifras_disponibles))    # Elige el primer objetivo y lo elimina de los números disponibles
    for _ in range(dificultad):
        operando2 = random.choice(cifras_disponibles)                           # Elige el segundo objetivo

        operacion = random.choice(operaciones)                                  # Elige una operación aleatoria

        # Si la operación elegida es una división y el resultado no es entero, se elige otra operación
        # También se elige otra operación si el resultado de la operación es menor que 1

        # Edge case: El resultado no está entre el rango permitido de 100-999 con dificultades altas, y el bucle se queda atascado.
        # Para esos casos se irá contando y si se hacen todas las combinaciones posibles se interrumpirá el bucle y se usará el objetivo anterior.
        count = 0
        while operacion == "/" and objetivo % operando2 != 0 or not 100 <= operar([objetivo, operacion, operando2]) <= 999:
            count+=1
            operacion = random.choice(operaciones)
            operando2 = random.choice(cifras_disponibles)

            if count == 24:
                return

        cifras_disponibles.remove(operando2)                        # Elimina el segundo operando
        objetivo = int(operar([objetivo, operacion, operando2]))    # Actualiza el objetivo
    return objetivo



def generar_cifras_disponibles(cifras):
    """Genera una lista con los 6 números con los que llegar al objetivo"""
    return random.choices(cifras, k=6)


def verificar_operacion(entrada):
    """Devuelve True si la operación introducida tiene el formato correcto ("... + ...", "... / ...", etc.)"""
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

    if not verificar_operacion(operacion):                          # Si la operación no es válida
        print("La operación introducida no es correcta")
        return

    operando1, simbolo, operando2 = extraer_operacion(operacion)
    if not (operando1 in cifras and operando2 in cifras):           # Si cualquiera de los operandos no está en cifras
        print("Las cifras no están entre las cifras disponibles")
        return
    
    if simbolo == "/" and operando1 % operando2 != 0:               # Si la operación es una división y ésta no es entera
        print("La división tiene que ser entera")
        return

    cifras.append(operar([operando1, simbolo, operando2]))

    cifras.remove(operando1)
    cifras.remove(operando2)

    return cifras


def calcular_distancia(cifras_disponibles, objetivo):
    distancia = objetivo - cifras_disponibles[0]
    for cifra in cifras_disponibles:
        if abs(objetivo - cifra) < distancia:
            distancia = abs(objetivo - cifra)
    return distancia


def operar(operacion):
    """Devuelve el resultado de una operación, el argumento tiene que ser una lista en formato [operando1, símbolo, operando2]"""
    match operacion[1]:
        case "+":
            return operacion[0] + operacion[2]
        case "-":
            return operacion[0] - operacion[2]
        case "*":
            return operacion[0] * operacion[2]
        case "/":
            return operacion[0] / operacion[2]


if __name__ == "__main__":
    main()
