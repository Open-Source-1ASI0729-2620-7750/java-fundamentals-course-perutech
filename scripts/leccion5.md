# Lección 5: Estructuras de Datos, Proyecto Final y Mejores Prácticas

Hola, bienvenidos a la quinta y última lección de nuestro curso de Fundamentos
de Java.

Durante las lecciones anteriores hemos aprendido conceptos como variables,
operadores, condicionales, bucles, métodos y programación orientada a objetos.

En esta última lección vamos a combinar varios de esos conocimientos para
construir nuestro pequeño proyecto final.

Aprenderemos qué son los arrays, cómo podemos recorrerlos y cómo almacenar
objetos dentro de ellos. Finalmente, construiremos un pequeño Gestor de
Mascotas.

Para realizar nuestra práctica utilizaremos OneCompiler, una herramienta que
nos permite escribir y ejecutar código Java directamente desde nuestro
navegador.

## Arrays

Comencemos con los arrays, también conocidos como arreglos.

Imaginemos que queremos almacenar los nombres de varias mascotas.

Podríamos crear una variable diferente para cada nombre. Sin embargo, si
tuviéramos diez, veinte o cien mascotas, tendríamos que crear demasiadas
variables.

Para solucionar este problema podemos utilizar un array.

Un array nos permite almacenar varios elementos del mismo tipo dentro de una
sola estructura.

Por ejemplo:

String[] petNames = {"Luna", "Michi", "Rocky"};

En este caso utilizamos String porque vamos a almacenar textos.

Los corchetes indican que no estamos trabajando con un solo String, sino con
un conjunto de ellos.

También debemos recordar que Java comienza a contar las posiciones desde cero.

Por eso Luna se encuentra en la posición cero, Michi en la posición uno y
Rocky en la posición dos.

Si queremos recorrer todos los elementos podemos utilizar un bucle for-each.

for (String petName : petNames) {
System.out.println(petName);
}

Podemos leer esta instrucción como: por cada nombre que exista dentro del
arreglo petNames, muestra ese nombre.

## Arrays de objetos

Hasta este momento hemos almacenado textos, pero una mascota tiene más
información.

Por ejemplo, queremos almacenar su nombre, edad y tipo.

Para representar esta información podemos utilizar programación orientada a
objetos.

Creamos una clase llamada Pet que tendrá tres atributos privados: name, age
y type.

También utilizamos un constructor para recibir estos datos cuando creamos
cada mascota.

Luego podemos crear métodos como getName y getAge para consultar la
información almacenada.

Finalmente, el método showInfo permite mostrar todos los datos de una
mascota en la consola.

Ahora podemos combinar los arrays con los objetos.

En lugar de crear un array de String, podemos crear un array de tipo Pet.

Pet[] pets = {
new Pet("Luna", 3, "Perro"),
new Pet("Michi", 2, "Gato"),
new Pet("Rocky", 5, "Perro"),
new Pet("Nala", 1, "Gato")
};

Cada posición del arreglo contiene ahora un objeto completo.

Podemos recorrerlo utilizando nuevamente un for-each.

for (Pet pet : pets) {
pet.showInfo();
}

Por cada objeto Pet que se encuentre dentro del arreglo, ejecutamos su método
showInfo.

De esta manera podemos mostrar automáticamente todas las mascotas
registradas.

## Cantidad de elementos

Los arrays también tienen una propiedad llamada length.

Esta propiedad permite conocer la cantidad de elementos existentes.

Por ejemplo:

pets.length

Como nuestro array contiene cuatro mascotas, el resultado será cuatro.

Una ventaja es que si agregamos otra mascota, no necesitamos cambiar
manualmente este número.

## Proyecto final

Para completar nuestro proyecto vamos a crear una función que permita
identificar cuál de nuestras mascotas tiene mayor edad.

El método se llama findOldestPet.

Primero suponemos que la primera mascota del arreglo es la de mayor edad.

Después recorremos todo el arreglo mediante un for-each.

En cada recorrido utilizamos una condición if para comparar la edad de la
mascota actual con la edad de la mascota que actualmente consideramos mayor.

Si encontramos una edad superior, actualizamos nuestra variable.

Cuando terminamos de recorrer el arreglo devolvemos la mascota encontrada.

Al ejecutar el programa podemos comprobar que Rocky es identificado como la
mascota de mayor edad con cinco años.

En este pequeño proyecto estamos combinando varios conceptos que vimos
durante el curso.

Utilizamos clases, objetos, encapsulación, métodos, arrays, bucles y
condicionales.

## Depuración básica

Ahora veremos un concepto importante: la depuración.

Mientras programamos es completamente normal cometer errores.

Por ejemplo, nuestro arreglo contiene cuatro mascotas.

Java comienza a contar desde cero, por lo que las posiciones disponibles son
cero, uno, dos y tres.

Si intentamos utilizar pets[10], Java mostrará un
ArrayIndexOutOfBoundsException.

Este mensaje significa que estamos intentando acceder a una posición que no
existe dentro del arreglo.

Cuando ocurra un error no debemos modificar el programa al azar.

Primero debemos leer el mensaje que Java nos proporciona e identificar la
línea donde ocurrió el problema.

El proceso de localizar, analizar y corregir errores en nuestro programa se
conoce como depuración.

## Buenas prácticas

Antes de terminar, recordemos algunas buenas prácticas que podemos aplicar
desde nuestros primeros programas.

Primero, debemos utilizar nombres descriptivos para nuestras variables y
métodos.

Por ejemplo, un nombre como oldestPet permite comprender fácilmente qué
información almacena una variable.

También debemos mantener una correcta indentación para facilitar la lectura
del código.

Otra buena práctica consiste en utilizar métodos para separar las diferentes
responsabilidades de nuestro programa.

Además, debemos evitar repetir código cuando podemos resolver una tarea
utilizando estructuras como métodos o bucles.

Finalmente, cuando aparezca un error debemos acostumbrarnos a leer el mensaje
antes de comenzar a modificar nuestro código.

## Cierre

Y con esto llegamos al final de nuestra quinta lección y también al final del
curso de Fundamentos de Java.

En esta lección aprendimos qué es un array, cómo recorrerlo y cómo almacenar
objetos dentro de él.

Después combinamos estos conocimientos para construir nuestro Gestor de
Mascotas.

También aprendimos cómo identificar un error sencillo y revisamos algunas
buenas prácticas para mantener nuestro código organizado.

Como reto final pueden modificar el proyecto agregando nuevas mascotas,
nuevos atributos o creando un método que permita buscar una mascota por su
nombre.

Lo más importante ahora es continuar practicando, experimentar con el código
y crear nuevos proyectos.

¡Felicitaciones por completar el curso de Fundamentos de Java!