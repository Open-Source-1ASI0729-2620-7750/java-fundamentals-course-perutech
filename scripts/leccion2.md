# Guion Lección 2: Estructuras de Control y Métodos

**Voz en off (Introducción):**
"¡Hola y bienvenidos a la segunda lección de nuestro curso de Java!
En la primera lección conocimos qué es Java, cómo almacenar información en variables como números enteros o textos, y cómo utilizar operadores básicos.
Sin embargo, hasta ese momento nuestros programas solo se ejecutaban en línea recta de arriba hacia abajo, sin poder elegir entre distintos caminos ni repetir tareas por su cuenta.
En esta segunda lección aprenderemos tres herramientas esenciales para darle inteligencia y orden a nuestros programas:
Primero, cómo lograr que el programa tome decisiones utilizando las sentencias condicionales if y else.
Segundo, cómo repetir acciones de forma automática sin duplicar líneas utilizando los bucles for y while.
Y tercero, cómo organizar nuestro programa en bloques reutilizables mediante métodos y parámetros.
Recuerda que en la descripción del video encontrarás el enlace directo a este editor en línea con el código listo para que puedas ejecutarlo desde tu navegador sin instalar nada. ¡Comencemos!"

**Voz en off (Decisiones if - else):**
"Empecemos con las estructuras condicionales if y else, que acabo de activar aquí en el Bloque 1.
En nuestra vida cotidiana tomamos decisiones basadas en condiciones todo el tiempo: si tengo saldo suficiente en mi tarjeta, realizo la compra; si no, debo esperar. En un videojuego ocurre exactamente lo mismo.
En Java representamos estas decisiones con la palabra if, que significa 'si condicional', y la palabra else, que significa 'si no' o 'en caso contrario'.
Observa con atención cómo está construido este Bloque 1 que tenemos en pantalla:
Al inicio tenemos declaradas dos variables enteras: int monedas igual a 120, e int precioEspada igual a 100.
En el primer condicional evaluamos el Caso 1:
Dentro del paréntesis del if tenemos la condición: monedas mayor o igual a precioEspada.
Si esa condición se cumple, el programa ejecuta lo que está dentro de las primeras llaves: muestra el mensaje 'Compra exitosa! Te alcanza para la espada', luego actualiza nuestras monedas restando 120 menos 100, y nos imprime cuántas monedas nos quedan.
En cambio, si no tuviéramos monedas suficientes, el programa saltaría a las llaves del else.
Ahora mira justo debajo el segundo condicional de este mismo bloque, donde evaluamos el Caso 2:
Después de comprar la espada de 100 monedas, solo nos quedaron 20 monedas guardadas en la variable monedas.
Aquí abajo tenemos una nueva variable llamada precioArmadura que vale 80, y un segundo if que pregunta: ¿monedas es mayor o igual a precioArmadura?
Como 20 no es mayor ni igual a 80, en este segundo caso la condición es falsa, por lo que el programa ignorará el bloque if y entrará directamente al bloque else."

**Voz en off (Ejecución if-else):**
"Hagamos clic en el botón Run para comprobar ambos casos en la consola:
En el Caso 1, como empezamos con 120 monedas y la espada costaba 100, se cumplió el if, realizó la compra y nos dejó con 20 monedas restantes.
Y en el Caso 2, como la armadura cuesta 80 y solo nos quedaban 20 monedas, el programa entró automáticamente al camino del else y nos mostró el mensaje: 'No te alcanza para la armadura, solo tienes 20 monedas'. Así vemos ambos caminos funcionando en tiempo real."

**Voz en off (Múltiples condiciones):**
"Ahora pasemos al Bloque 2 que acabo de descomentar en pantalla.
¿Qué sucede cuando en nuestro programa no solo existen dos caminos posibles, sino tres o más alternativas? Por ejemplo, clasificar el rango de un jugador según el nivel que tiene actualmente.
Para evaluar varias condiciones en orden secuencial utilizamos la instrucción else if.
Observa el código de este Bloque 2:
Tenemos la variable entera nivel con el valor de 15.
Primero, el programa revisa la condición del if principal: ¿el nivel es mayor o igual a 20? Si fuera verdadero, mostraría 'Rango actual: Maestro'.
Pero como nuestro nivel es 15, esa primera condición no se cumple y el programa pasa a evaluar la segunda pregunta con else if: ¿el nivel es mayor o igual a 10?
Como 15 sí es mayor o igual a 10, esta condición resulta verdadera y se prepara para mostrar 'Rango actual: Avanzado'.
Finalmente, el último bloque else queda reservado por si el jugador tuviera un nivel menor a 10, asignándole el rango 'Principiante'."

**Voz en off (Ejecución else if):**
"Al darle clic a Run, verificamos en la consola que el programa evaluó las condiciones en orden y seleccionó exactamente la opción del medio: 'Rango actual: Avanzado'."

**Voz en off (Bucles for y while):**
"Continuemos ahora con el Bloque 3 para conocer nuestro segundo tema principal: los bucles for y while.
En programación, muchas veces necesitamos repetir una misma tarea varias veces, como registrar 3 misiones diarias o descontar puntos de energía en un entrenamiento. En lugar de copiar y pegar la misma línea muchas veces, utilizamos los bucles para que el programa repita las instrucciones automáticamente.
En la primera parte de este Bloque 3 tenemos el bucle for.
Utilizamos el bucle for cuando sabemos exactamente cuántas veces queremos repetir una acción.
Observa las tres instrucciones que están dentro del paréntesis del for, separadas por punto y coma:
La primera es el punto de partida: int mision = 1; donde empieza nuestra cuenta.
La segunda es la condición límite: mision menor o igual a 3; el bucle seguirá dando vueltas mientras mision sea 1, 2 o 3.
Y la tercera es el incremento: mision++; esos dos signos de suma aumentan el número de misión de uno en uno al terminar cada vuelta.
Justo debajo, en este mismo bloque, tenemos el bucle while, que en español significa 'mientras'.
Usamos el bucle while cuando queremos repetir una acción mientras una condición se mantenga verdadera.
Aquí vemos la variable entera energia inicializada en 3, seguida de la instrucción while con la condición: energia mayor que 0.
Dentro de sus llaves, el programa muestra el mensaje de entrenamiento y en la línea siguiente tiene la instrucción energia--; con dos signos de resta, la cual descuenta 1 punto de energía en cada vuelta.
Esta línea donde restamos energía es fundamental: si no estuviera ahí, la energía siempre sería 3 y el bucle se repetiría sin parar creando un bucle infinito."

**Voz en off (Ejecución bucles):**
"Vamos a presionar Run para observar el resultado en la consola:
Primero vemos cómo el bucle for ejecutó las tres vueltas mostrando las misiones diarias número 1, 2 y 3.
Y debajo vemos cómo el bucle while entrenó al personaje con energía 3, luego con energía 2, luego con energía 1, y cuando la energía bajó a cero, el bucle terminó limpiamente mostrando el mensaje 'Personaje sin energia, hora de descansar!'."

**Voz en off (Métodos):**
"Finalmente, acabo de activar el Bloque 4 para aprender el tercer tema de nuestra clase: los métodos —también conocidos como funciones— y los parámetros.
Cuando construimos programas más grandes, poner todas las instrucciones juntas dentro del método main hace que el código sea difícil de mantener.
Un método es un bloque de código independiente con nombre propio que creamos para realizar una tarea específica cada vez que lo llamemos. Y los parámetros son los datos que colocamos entre paréntesis para que ese método trabaje con ellos.
Observa aquí en la parte superior de nuestro archivo los dos métodos que tenemos definidos fuera del main:
El primero se llama saludarJugador. Tiene la palabra void porque su única tarea es mostrar un mensaje en pantalla sin devolver ningún cálculo matemático, y entre paréntesis recibe un parámetro de tipo texto llamado nombreJugador.
El segundo método se llama calcularPuntajeTotal. En lugar de void, tiene la palabra int porque este método sí nos devolverá un número entero como resultado. Recibe dos parámetros entre paréntesis: int puntosMision e int puntosExtra. Dentro suma ambos números en la variable resultado y usa la palabra return para devolver ese total."

**Voz en off (Ejecución Métodos):**
"Al bajar nuevamente al Bloque 4 y presionar Run, mira qué limpio queda nuestro programa principal:
Llamamos a saludarJugador pasándole el parámetro 'Alex', y en la siguiente línea lo reutilizamos pasándole el parámetro 'Sofia'.
Luego llamamos a calcularPuntajeTotal enviándole los parámetros 250 y 50, guardamos el valor devuelto en la variable puntajeFinal, y en la consola inferior comprobamos cómo aparecen ambos saludos personalizados y el puntaje total de 300."

**Voz en off (Pausa Interactiva y Cierre):**
"¡Muy bien! Ahora que has visto cómo funcionan las estructuras de control y los métodos en acción, es momento de que hagas una prueba rápida por tu cuenta.
Haz clic en el enlace del editor en línea que está en la descripción del video y pausa esta lección durante un par de minutos para experimentar con el código:
Prueba cambiar en el Bloque 2 el valor de la variable nivel de 15 a 25 o a 5, o cambia en el Bloque 4 los números a tu libertad, y presiona el botón Run para observar cómo responde el programa ante tus propios datos.
Hagamos una breve pausa de unos segundos para que puedas intentarlo...
(Pausa)
¡Excelente trabajo! Repasemos las tres ideas clave que aprendimos en esta Lección 2:
Primero: Con if, else if y else logramos que nuestro programa evalúe condiciones y elija el camino correcto.
Segundo: Con los bucles for y while automatizamos tareas repetitivas ahorrando muchas líneas de código.
Y tercero: Con los métodos y parámetros organizamos nuestras instrucciones en bloques claros que podemos reutilizar cuantas veces queramos.
En la Lección 3 aprenderás a leer datos escritos directamente por el usuario en la consola usando Scanner y comenzarás a crear tus propias clases y objetos en Programación Orientada a Objetos. ¡Muchas gracias por tu atención y nos vemos en el siguiente video!"