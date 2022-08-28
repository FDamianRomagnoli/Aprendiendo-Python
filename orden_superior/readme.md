Son funciones que reciben como parametro otra función

<li>
    <ul>
        <h2>Filter</h2>
        <p>Su forma es list(filter(funcion_lambda, my_list)) y filter retorna un iterador, que usando la funcion list() convertimos este iterador en una lista</p>
    </ul>
    <ul>
        <h2>Map</h2>
        <p>Modifica los valores de la lista, su forma es list(map(lambda, my_list)) donde la funcion lambda tiene que estar el cambio que haremos en cada elemento, ejemplo: lambda x: x**2.</p>
    </ul>
    <ul>
        <h2>Reduce</h2>
        <p>Reduce los valores de todo la lista en un solo valor, por ejemplo si quisieramos multiplicar todos los valores de una lista y tener un resultado, primero tenemos que importar el modulo reduce de esta forma: <b>from functools import reduce</b><br><br>Luego su forma seria valor = reduce(lambda a,b: a*b, my_list)</p>
    </ul>
</li>