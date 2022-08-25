Python guarda todos los paquetes de terceros en un solo directorio, esto tiene el problema que al tener varios proyectos con las mismas dependencias, si un modulo tiene una actualización puede que afecte a uno de los proyectos en cuestion.

Ahi aparecen los entornos virtuales, donde podremos asignar a cada proyecto sus determinadas dependencias con las actualiazaciones correspondientes para que no haya problemas.

Como crear un entorno virtual?

- Una vez dentro de un repositorio, abrimos la consola iterativa con python3 -m venv "Nombre del entorno".

- Por convención el nombre del entorno suele ser venv o env

- Una vez creado tendremos la carpeta del entorno virtual segun el nombre que le hallamos dado, en este caso venv.

- Tendremos que activar el entorno virtual, en la carpeta Scripts del venv utilizaremos "source venb/bin/activate", Con este comando activamos el entorno virtual. Para salir del entorno se usa deactivate

- Por ultimo, una buena practica es crear el fichero .gitignore para ocultar el entorno virtual:
    Dentro de .gitignore hay que colocar un / + el nombre de la carpeta, por ejemplo /venv