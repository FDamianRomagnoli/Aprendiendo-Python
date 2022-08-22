def conversor(tipo_pesos,valor_dolar):
    pesos = input(f'¿Cuantos pesos {tipo_pesos} tienes? -> ')
    pesos = float(pesos)
    dolares = pesos/valor_dolar
    dolares = str(round(dolares,2))
    print(f'Tienes ${dolares} dolares')


menu = """
Bienvenido al conversor de monedas 

1- Pesos argentinos
2- Pesos colombianos
3- Pesos mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor('argentinos', 295)
elif opcion == 2:
    conversor('colombianos', 4400)
elif opcion == 3:
    conversor('mexicanos', 20)
else:
    print('Ingresa una opcion correcta')