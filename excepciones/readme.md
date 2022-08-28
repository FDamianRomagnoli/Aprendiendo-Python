* try: Se coloca el codigo donde puede ocurrir una excepción

* except TypeError: En el except se maneja el error, es decir, si ocurre un error dentro del bloque de código del try, se deja de ejecutar el código del try y se ejecuta lo que se haya definido en el Except.

* raise: Cuando sabemos que algo es un error pero para el programa python esta todo bien, elevamos un error, que puede ser de ValueError.
Ejemplo <b>raise ValueError("No se puede ingresar una cadena vacia")</b>
Entonces el except seria asi <b>except ValueError as ve:
    print(ve)
    return false</b>

* finally: se usa al final de un try/except para cerrar conexciones por ejemplo a archivos, bases de datos, etc. con el fin de que estos no se dañen.