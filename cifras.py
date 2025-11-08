import random
import re


def main():
    cifras_posibles = generar_cifras_posibles()
    objetivo = generar_objetivo()
    cifras_disponibles = generar_cifras_disponibles(cifras_posibles)

    print(f"Cifras posibles: {cifras_posibles}")

    while len(cifras_disponibles) != 1 and not objetivo in cifras_disponibles:
        try:
            print(f"Objetivo: {objetivo}")
            print(f"Cifras disponibles:{cifras_disponibles}")
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


def generar_objetivo():
    """Genera el número a alcanzar"""
    return random.randint(100, 999)


def generar_cifras_disponibles(cifras):
    """Genera una lista con los 6 números con los que llegar al objetivo"""
    return random.choices(cifras, k=6)


def verificar_operacion(entrada):
    """Devuelve True si la operación introducida tiene el formato correcto ("... + ...", "... / ...", etc.)"""
    return True if re.search(r"^(\d+) ?([+|\-|*|/]) ?(\d+)$", entrada) else False


def extraer_operacion(entrada):
    """Devuelve una lista con el primer número de la operación, el símbolo de operación, y el segundo número de la operación"""
    operacion = [i for i in re.search(r"^(\d+) ?([+|\-|*|/]) ?(\d+)$", entrada).groups()]
    operacion[0], operacion[2] = int(operacion[0]), int(operacion[2])
    return operacion


def actualizar_lista(operacion, cifras):
    """
    Actualiza la lista de cifras disponibles.

    Argumentos:
    - `operacion`, un string con la operación que se ha hecho, los dos operandos tienen que estar entre las cifras disponibles
    - `cifras`, una lista que contiene las cifras disponibles para hacer operaciones

    Devuelve la lista actualizada con la operación hecha
    """

    if not verificar_operacion(operacion):
        print("La operación introducida no es correcta")
        return

    operando1, simbolo, operando2 = extraer_operacion(operacion)
    if not (operando1 in cifras and operando2 in cifras):
        print("Las cifras no están entre las cifras disponibles")
        return

    match simbolo:
        case "+":
            cifras.append(operando1 + operando2)
        case "-":
            cifras.append(operando1 - operando2)
        case "*":
            cifras.append(operando1 * operando2)
        case "/":
            if operando1 % operando2 != 0:
                print("La división tiene que ser entera")
                return
            cifras.append(operando1 / operando2)

    cifras.remove(operando1)
    cifras.remove(operando2)

    return cifras


def calcular_distancia(cifras_disponibles, objetivo):
    distancia = objetivo - cifras_disponibles[0]
    for cifra in cifras_disponibles:
        if abs(objetivo - cifra) < distancia:
            distancia = abs(objetivo - cifra)
    return distancia


if __name__ == "__main__":
    main()
