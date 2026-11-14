¡Hola a todos! Bienvenidos a esta lección de nuestro curso de fundamentos de Java.

En esta clase vamos a aprender tres conceptos importantes de la programación orientada a objetos: las clases y los objetos, la encapsulación y las estructuras de datos.

Para entender estos conceptos, vamos a trabajar con un ejemplo práctico: una pequeña biblioteca donde podremos registrar libros, guardar información sobre ellos y buscar títulos.

No se preocupen si estos conceptos parecen un poco complicados al principio. Vamos a explicarlos paso a paso y utilizaremos un programa sencillo para comprender cómo funcionan.

Primero, vamos a recordar qué es una clase y qué es un objeto.

En Java, una clase funciona como un molde o una plantilla que nos permite definir las características y los comportamientos que tendrán determinados objetos.

Por ejemplo, si queremos representar libros en nuestro programa, podemos crear una clase llamada `Libro`.

Cada libro tiene información propia, como su título, su autor y su número de páginas. Estas características se conocen como atributos.

Vamos a ver cómo se representa esto en Java.

Creamos la clase escribiendo la palabra `class` y luego el nombre `Libro`.

Dentro de ella declaramos tres atributos: `titulo`, de tipo `String`; `autor`, también de tipo `String`; y `paginas`, de tipo `int`.

Ahora vamos a aplicar un concepto muy importante llamado encapsulación.

La encapsulación consiste en proteger la información de un objeto para evitar que pueda modificarse directamente desde cualquier parte del programa.

Para conseguirlo, declaramos los atributos utilizando la palabra `private`.

Esto significa que no podremos acceder directamente a ellos desde fuera de la clase.

Pero entonces, ¿cómo podemos consultar o modificar la información de un libro?

Para eso utilizamos los métodos conocidos como getters y setters.

Los getters nos permiten obtener o consultar el valor de un atributo. Por ejemplo, el método `getTitulo` nos devuelve el título del libro.

Por otro lado, los setters nos permiten modificar el valor de un atributo. Por ejemplo, `setTitulo` recibe un nuevo título y lo guarda dentro del objeto.

También podemos agregar validaciones dentro de los setters.

En nuestro caso, vamos a hacer que el número de páginas siempre sea mayor que cero.

Por eso, dentro de `setPaginas`, utilizamos una condición `if` que comprueba si el número recibido es válido. Si es mayor que cero, se guarda. De lo contrario, mostramos un mensaje indicando que el número de páginas debe ser mayor que cero.

De esta manera, protegemos los datos y evitamos guardar información incorrecta.

Ahora que tenemos nuestra clase `Libro`, vamos a utilizarla para crear objetos.

Un objeto es una instancia de una clase. Es decir, es un elemento creado a partir del molde que definimos anteriormente.

Para crear un objeto en Java utilizamos la palabra `new`, seguida del nombre de la clase y de los paréntesis.

En nuestro programa vamos a crear tres libros diferentes.

Pero, en lugar de declarar una variable independiente para cada libro, vamos a utilizar una estructura de datos llamada arreglo.

Un arreglo nos permite almacenar varios elementos del mismo tipo dentro de una sola variable.

En este caso, escribimos `Libro`, seguido de corchetes, para indicar que será un arreglo de objetos de tipo `Libro`.

Luego le damos el nombre `biblioteca` y establecemos que tendrá espacio para tres elementos.

Después creamos cada uno de los libros utilizando `new Libro()` y los colocamos en las posiciones cero, uno y dos del arreglo.

Es importante recordar que en Java las posiciones de los arreglos comienzan desde cero.

Ahora vamos a utilizar los setters que creamos anteriormente para asignar la información de cada libro.

Al primer libro le asignamos el título "Java desde cero", el autor "Carlos Ruiz" y 180 páginas.

Al segundo libro le asignamos el título "Aprendiendo programación", la autora "Ana Torres" y 220 páginas.

Finalmente, al tercer libro le asignamos el título "Introducción a Java", el autor "Luis Pérez" y 150 páginas.

Como pueden observar, cada objeto tiene sus propios datos, aunque todos fueron creados utilizando la misma clase.

Ahora que tenemos nuestros tres libros guardados en el arreglo, vamos a mostrar su información en pantalla.

Para hacerlo, utilizaremos un ciclo `for`.

Un ciclo nos permite repetir una serie de instrucciones varias veces sin tener que escribirlas manualmente para cada elemento.

En nuestro caso, el ciclo comienza con una variable llamada `i`, que representa la posición actual del arreglo.

La condición indica que el ciclo continuará mientras `i` sea menor que la cantidad de elementos de la biblioteca.

Para obtener esa cantidad utilizamos `biblioteca.length`.

Después de cada repetición, aumentamos el valor de `i` en uno.

Dentro del ciclo mostramos el número del libro, su título, su autor y su cantidad de páginas.

Para consultar estos datos utilizamos los getters que definimos en nuestra clase `Libro`.

Por ejemplo, escribimos `biblioteca[i].getTitulo()` para obtener el título del libro que se encuentra en la posición actual.

Lo mismo hacemos con el autor y el número de páginas.

De esta manera, el programa puede recorrer todos los libros y mostrar su información automáticamente.

Esto es muy útil cuando trabajamos con varios objetos, porque no necesitamos escribir instrucciones diferentes para cada uno.

Ahora vamos a agregar una funcionalidad más a nuestra biblioteca: buscar libros por una palabra que aparezca en su título.

Primero creamos una variable de tipo `String` llamada `palabraBuscada`.

En este ejemplo vamos a guardar la palabra "java".

También creamos una variable booleana llamada `encontrado`, que inicialmente tendrá el valor `false`.

Esta variable nos servirá para saber si encontramos algún libro que coincida con nuestra búsqueda.

Después utilizamos otro ciclo `for` para recorrer nuevamente el arreglo de libros.

En cada repetición obtenemos el título del libro actual utilizando el método `getTitulo()` y lo guardamos en una variable llamada `titulo`.

Ahora viene una parte importante.

Utilizamos el método `toLowerCase()` para convertir el texto a letras minúsculas.

Esto nos permite realizar una búsqueda sin importar si algunas letras están escritas en mayúsculas o minúsculas.

Luego utilizamos el método `contains()`, que permite comprobar si un texto contiene una palabra o fragmento determinado.

Por ejemplo, si el título es "Java desde cero", el método puede comprobar que contiene la palabra "java".

Si encontramos una coincidencia, mostramos el título del libro en pantalla y cambiamos la variable `encontrado` a `true`.

Finalmente, después de recorrer todos los libros, comprobamos si la variable `encontrado` continúa siendo `false`.

Si es así, significa que no encontramos ningún libro que coincida con la palabra buscada, por lo que mostramos un mensaje indicando que no hubo resultados.

Así conseguimos implementar una búsqueda sencilla utilizando arreglos y métodos de la clase `String`.

Ahora que hemos visto cómo funciona nuestro programa, les propongo un pequeño ejercicio para practicar.

Primero, intenten agregar un cuarto libro a la biblioteca.

Recuerden que, para hacerlo, tendrán que modificar el tamaño del arreglo y crear el nuevo objeto.

Después, asignen un título, un autor y una cantidad válida de páginas utilizando los setters.

Como segundo reto, cambien la palabra que utilizamos para realizar la búsqueda.

Por ejemplo, pueden buscar la palabra "programación" o cualquier otra palabra que aparezca en alguno de los títulos.

Finalmente, prueben qué sucede cuando buscan una palabra que no existe en ningún libro.

De esta manera podrán comprobar cómo funcionan los arreglos, los objetos, los métodos y las condiciones dentro de un mismo programa.