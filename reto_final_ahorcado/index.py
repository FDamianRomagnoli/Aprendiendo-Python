import random
import os

def main():
    palabra = getWord()
    printMenu(palabra)
    palabra_a_completar = getIncompleted(palabra)
    print(palabra_a_completar)
    juego_terminado = False

    while juego_terminado == False:
        printMenu

def getIncompleted(palabra):
    incompleted = ""
    for l in palabra:
        incompleted = incompleted + "_ "
    return incompleted

def getWord():
    with open('reto_final_ahorcado/data.txt','r', encoding='utf-8') as f:
        palabra = ""
        numero_random = random.randint(1, 171)
        contador = 0

        for line in f:
            contador = contador + 1
            if(contador == numero_random):
                palabra = line

    return palabra
        

def printMenu(text):
    os.system('clear')
    print(f'!Adivine la palabra!\n\t{text}')




if __name__ == '__main__':
    main()
