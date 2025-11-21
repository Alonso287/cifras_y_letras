import requests
import random

def main():
    inicializar_variables()
    while True:
        try:
            vocales_jugador = int(input("Cuántas vocales quieres? (3-6)\n"))
            if not (3 <= vocales_jugador <= 6):
                print("El número debe estar entre 3 y 6")
                continue
            break
        except Exception:
            print("Entrada inválida")

    modo = input("Quieres jugar en modo anagrama? Esto garantizará que exista una respuesta (s/n)").strip().lower() == "s"
    letras_disponibles = generar_letras_disponibles(vocales_jugador, modo)

    while True:
        print(f"Letras disponibles: {letras_disponibles}")
        palabra = input("Introduce tu palabra:\n").strip().lower()
        if not verificar_palabra(quitar_tildes(palabra), letras_disponibles):
            print("Todas las letras de tus palabras deben estar entre las letras disponibles")
            continue
        elif len(palabra) < 5:
            print("Las palabras deben tener 5 letras o más")
            continue
        break

    if buscar_palabra(palabra):
        print(f"¡Enhorabuena! Has encontrado una palabra con {len(palabra)} letras!\n")
        origen, acepciones = significados(palabra)
        print(palabra)
        print(f"Origen: {origen}")
        print("Acepciones:")
        for i in range(len(acepciones)):
            print(f"{i+1}. {acepciones[i]}")
    else:
        print(f"¡Mala suerte! La palabra {palabra} no está en el Diccionario de la Real Academia Española")

def inicializar_variables():
    global consonantes
    global vocales
    global letras
    global url
    consonantes = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z")
    vocales = ("a", "e", "i", "o", "u")
    letras = consonantes + vocales
    url = "https://rae-api.com/api/words/"


def generar_letras_disponibles(vocales_jugador=None, modo_anagrama= False):
    if vocales_jugador == None:
        vocales_jugador = random.randint(3,6)
    if not modo_anagrama:
        return random.choices(vocales, k=vocales_jugador) + random.choices(consonantes, k=10 - vocales_jugador)
    palabra = list(quitar_tildes(requests.get("https://rae-api.com/api/random?max_length=10").json()["data"]["word"]))
    random.shuffle(palabra)
    return palabra


def buscar_palabra(palabra):
    return requests.get(url + palabra).json()["ok"]


def significados(palabra):
    respuesta = requests.get(url + palabra).json()
    try:
        origen = respuesta["data"]["meanings"][0]["origin"]["raw"]
    except:
        origen = "N/A"
    try:
        acepciones =  [acepcion["description"] for acepcion in respuesta["data"]["meanings"][0]["senses"]]
    except:
        acepciones = "N/A"
    return origen, acepciones


def verificar_palabra(palabra, letras_disponibles):
    frecuencia_palabra = {letra:palabra.count(letra) for letra in palabra}
    frecuencia_letras = {letra:letras_disponibles.count(letra) for letra in palabra}

    return all([frecuencia_letras[letra] - frecuencia_palabra[letra] >= 0 for letra in palabra])
    

def quitar_tildes(palabra):
    return palabra.strip().replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")


if __name__ == "__main__":
    palabra = requests.get("https://rae-api.com/api/random?max_length=10").json()
    print(palabra)
    palabra = palabra["data"]["word"]
    print(palabra)
    palabra = quitar_tildes(palabra)
    print(palabra)