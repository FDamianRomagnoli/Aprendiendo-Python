Tenemos errores de sintaxis y las excepciones:

* Un error de sintaxis es un error en el orden, reglas, o nombres de identificadores, haciendo que el programa ni siquiera se ejecute.

* Las excepciones suceden en un punto de ejecución que hace que quiebre toda la logica del programa, hay mas de 50 excepciones en python pero las 6 mas vistas son:

- KeyboardInterrupt: CTRL + C
- KeyError: Intentamos acceder a una key de un diccionario que no existe
- IndexError: Intentamos acceder a un indice de la lista que no existe
- FileNotFoundError: Si intentamos abrir un archivo que no existe se produce una excepción
- ZeroDivisionError: División por cero
- ImportError: Si importamos un modulo donde halla un error se produce esta excepción.

* El mensaje que vemos es el Traceback que es el objeto de excepción, lo ideal es leer la ultima linea del mensaje del traceback que dice que tipo de excepción se produjo.