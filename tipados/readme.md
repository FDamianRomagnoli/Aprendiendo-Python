* Los lenguajes de tipado estatico levantan los errores de type en tiempo de compilación.

* Los lenguajes de tipado dinamico lo levantan en tiempo de ejecución, python detecta un error cuando el programa llega al punto donde esta el error, en cambio java lo detecta en tiempo de compilación antes de que ejecute.

* Los lenguajes de tipado debil tratan de manera menos estricta a las variables de distintos tipos, permitiendo hacer operaciones entre variables de distintos tipos.

* Los lenguajes de tipado fuerte no permiten operaciones entre variables de distintos tipos.

<h2>Tipado estatico en python > 3.6</h2>

<b>a: int = 5</b><br>
<b>b: str = "hola"</b><br>
<b>c: bool = True</b><br>

<b>def suma(a: int, b: int) -> int: (Aca anunciamos que tipo va a retornar nuestra funcion con -> int)</b><br>

De igual forma esta es una nueva función de python por lo que contiene algunos huecos.