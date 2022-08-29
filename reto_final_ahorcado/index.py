from multiprocessing.resource_sharer import stop
import random
import os

def main():
    palabra = list(getWord())
    palabra_a_completar = list(getIncompleted(palabra))
    juego_terminado = False
    printMenu(palabra_a_completar)

    while juego_terminado == False:
        letra = getCharacter()
        palabra_a_completar = compare(palabra,palabra_a_completar,letra)
        printMenu(palabra_a_completar)
        juego_terminado = isWin(palabra,palabra_a_completar)
    
    print("Felicidades, GANASTE")


def isWin(palabra, palabraJugador):
    return ''.join(palabra) == ''.join(palabraJugador)


def getCharacter():
    try:
        letra = input('Ingrese un caracter: ')
        assert len(letra) == 1,'Ingrese un caracter..'
        assert letra.isnumeric() == False, 'Ingrese una letra'
    except ValueError:
        print(ValueError)

    return letra

def compare(palabra_completo,palabra_incompleta,letra):

    palabra_final = ""

    for (i,c) in enumerate(palabra_completo,0):
        if palabra_completo[i] == letra:
            palabra_final = palabra_final + letra
        else:
            palabra_final = palabra_final + palabra_incompleta[i]

    return palabra_final


def getIncompleted(palabra):
    return list(map(lambda a: '_',palabra))

def getWord():
    with open('reto_final_ahorcado/data.txt','r', encoding='utf-8') as f:
        palabra = ""
        numero_random = random.randint(1, 171)
        contador = 0

        for line in f:
            contador = contador + 1
            if(contador == numero_random):
                palabra = line.strip()

    return palabra
        

def printMenu(text):
    os.system('clear')
    print('!Adivine la palabra!\n\t')
    for l in text:
        print(f'{l.upper()}', end=" ")
    print('\n\t')





if __name__ == '__main__':
    main()
