import random
import re


def main(): ...


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
    return True if re.search(r"^\d+ [+|-|*|/] \d+$", entrada) else False


def actualizar_lista(operacion, cifras):
    if not verificar_operacion(operacion):
        raise ValueError("La operación introducida no es correcta")

    operando1, simbolo, operando2 = operacion.split(" ")
    if not (operando1 in cifras and operando2 in cifras):
        raise ValueError("Las cifras no están entre las cifras disponibles")

    cifras.pop(operando1).pop(operando2)

    match simbolo:
        case "+":
            cifras.append(operando1 + operando2)
        case "-":
            cifras.append(operando1 - operando2)
        case "*":
            cifras.append(operando1 * operando2)
        case "/":
            cifras.append(operando1 / operando2)

    return cifras


if __name__ == "__main__":
    main()
