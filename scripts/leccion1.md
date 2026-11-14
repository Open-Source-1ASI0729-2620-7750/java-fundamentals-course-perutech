¿Alguna vez te has preguntado cómo sabe un videojuego cuándo debe aumentar tu puntuación, cómo una aplicación recuerda tu nombre o cómo una calculadora obtiene el resultado de una operación? Detrás de todas estas acciones existe algo en común: la programación.

Programar consiste en crear instrucciones que una computadora pueda interpretar y ejecutar para realizar determinadas tareas. Podemos imaginarlo como una receta de cocina: primero necesitamos los ingredientes, después seguimos una serie de pasos y, finalmente, obtenemos un resultado. Las computadoras funcionan de una manera muy parecida; necesitan instrucciones claras, ordenadas y precisas para saber exactamente qué deben hacer.

Ahora bien, existen diferentes lenguajes que nos permiten comunicarnos con ellas. Algunos ejemplos conocidos son Python, C++ y Java. En esta oportunidad vamos a trabajar con Java, un lenguaje de programación sumamente utilizado en el desarrollo de aplicaciones, sistemas empresariales y diferentes tipos de software.

¿Y por qué aprender Java? Principalmente porque permite desarrollar programas de manera estructurada, posee una amplia comunidad de desarrolladores y cuenta con herramientas que facilitan la creación de soluciones para diferentes plataformas. Además, Java nos ayudará a comprender conceptos clave que utilizaremos más adelante, como las clases, los objetos y otros fundamentos esenciales de la programación orientada a objetos. Pero no te preocupes, no necesitamos aprender todo de golpe; comenzaremos con ejemplos pequeños y construiremos nuestros conocimientos paso a paso. Para realizar las prácticas utilizaremos OnlineGDB, un editor gratuito que funciona directamente desde el navegador, lo que nos permite escribir, ejecutar y comprobar nuestro código sin necesidad de descargar ni instalar ningún programa adicional.

Ahora que conocemos un poco más sobre este lenguaje, vamos a comenzar a escribir nuestro primer programa. Cuando abrimos el editor, encontramos una estructura inicial que debemos aprender a reconocer:

public class Main {
public static void main(String[] args) {
}
}

Aunque al principio pueda parecer un poco complejo, cada elemento cumple una función específica. La palabra clave class nos permite definir una clase, que es una estructura fundamental en Java. Por ahora trabajaremos con una clase llamada Main. Dentro de ella encontramos el método main, que funciona como el punto de entrada de nuestro programa, es decir, el lugar exacto desde donde comienza la ejecución. Para comprobarlo, escribiremos una instrucción sencilla:

System.out.println("Hola, estoy aprendiendo Java");

Esta instrucción permite mostrar un mensaje directamente en la consola. Si ejecutamos el programa, veremos nuestro texto reflejado como resultado.

Ahora imaginemos que queremos crear un pequeño registro de estudiantes. Para ello necesitaremos guardar información importante como sus nombres, edades y calificaciones. Para lograrlo utilizamos las variables. Una variable funciona como un espacio identificado por un nombre donde podemos almacenar un dato para utilizarlo posteriormente en el programa. Por ejemplo:

String nombre = "Lucia";
int edad = 16;
double nota = 18.5;
boolean estudianteActivo = true;

Veamos qué significa cada elemento. El tipo String nos permite almacenar textos, los cuales siempre se escriben entre comillas dobles. El tipo int almacena números enteros, como una edad o una cantidad. El tipo double permite guardar números decimales, ideales para calificaciones o estaturas. Finalmente, el tipo boolean representa únicamente dos posibilidades: true o false, es decir, verdadero o falso.

Para construir una variable, escribimos primero el tipo de dato, luego su nombre, colocamos el signo igual, asignamos el valor correspondiente y cerramos la instrucción con un punto y coma. Por ejemplo, en la línea int edad = 16;, estamos indicando que la variable llamada edad almacenará un número entero cuyo valor inicial es dieciséis.

Para mostrar la información que hemos guardado, utilizamos nuevamente la instrucción de salida combinando los textos con nuestras variables mediante el signo más. Algo muy interesante es que podemos modificar estos valores de manera sencilla sin necesidad de cambiar todo el programa, logrando que el sistema sea flexible y trabaje con diferentes datos.

Hasta este punto hemos aprendido a almacenar información. Sin embargo, los programas no solamente guardan datos, sino que también necesitan realizar cálculos, comparar valores y tomar decisiones. Para conseguirlo recurrimos a los operadores. Un operador es un símbolo que permite realizar una operación entre uno o varios valores.

En Java encontramos diferentes categorías. Primero están los operadores aritméticos, que utilizamos para realizar operaciones matemáticas básicas como la suma, la resta, la multiplicación, la división y el cálculo del residuo de una división mediante el porcentaje.

Segundo, tenemos los operadores de comparación, los cuales nos permiten contrastar dos valores y comprobar si se cumple o no una condición utilizando símbolos como el igual, el diferente, el mayor que, el menor que, el mayor o igual, y el menor o igual. Estas comparaciones siempre generan resultados booleanos, es decir, valores de verdadero o falso.

Tercero, los operadores lógicos nos permiten combinar varias condiciones utilizando el operador Y, el operador O, o la negación para invertir el valor lógico.

Finalmente, cuando combinamos variables, valores y operadores dentro de una misma instrucción, obtenemos lo que denominamos una expresión. Por ejemplo, si definimos un precio y una cantidad, podemos multiplicarlos y almacenar el resultado en una nueva variable para obtener el total a pagar. De esta manera, las expresiones nos permiten construir instrucciones mucho más útiles y resolver situaciones de la vida real utilizando Java.