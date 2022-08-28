Son las funciones anonimas, la estructura es:

* <b>lambda argumentos: expresión</b>

En Python solo pueden tener una sola linea las funciones lambda

palindrome = lambda string: string == string[::-1]

En este caso si le pasamos a palindrome('ana') seria true

En las funciones lambda no hace falta colocar un return

