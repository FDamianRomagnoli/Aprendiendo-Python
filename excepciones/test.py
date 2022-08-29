from multiprocessing.sharedctypes import Value

def es_positivo(num):
    try:
        if num < 0:
            raise ValueError('Ingrese un numero positivo, porfavor')
    except ValueError as ve:
        print(ve)

def main():
    try:
        num = int(input("Ingrese un numero: "))
        es_positivo(num)
    except ValueError:
        print("Debes ingresar un numero")
    


if __name__ == '__main__':
    main()