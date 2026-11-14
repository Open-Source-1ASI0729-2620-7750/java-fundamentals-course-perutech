# Fundamentos de Java para Principiantes


## Resumen del Curso


Este curso de 1 hora introduce a estudiantes de secundaria a los fundamentos de la programación con Java, incluyendo programación orientada a objetos.


* **Duración total:** ~60 minutos
* **Público Objetivo:** Estudiantes de 12 a 17 años sin experiencia en programación
* **Prerrequisitos:** Ninguno
* **Herramientas necesarias:** **¡Solo tu navegador web!** (Chrome, Firefox, Safari, Edge)
* **Repositorio de Código Fuente:** [https://github.com/Open-Source-1ASI0729-2620-7750/java-fundamentals-course-perutech](https://github.com/Open-Source-1ASI0729-2620-7750/java-fundamentals-course-perutech)


---


## Secuencia de la Lección


### Lección 1: ¿Qué es Java y la Programación? (10:35 minutos)
* **Descripción:** Aprende qué es la programación, por qué Java es un excelente lenguaje para empezar y cómo declarar tus primeras variables.
* **Enlace:** [Ver la lección](https://youtu.be/O-vM5T0-jkY)
* **Conclusiones clave:** Java se usa para aplicaciones y juegos; los programas son instrucciones para computadoras; uso de `int`, `String` y `boolean`.
* **Empieza a programar:** [Clic para programar](https://www.onlinegdb.com/)


### Lección 2: Operadores y Estructuras de Control (13:10 minutos)
* **Descripción:** Realiza operaciones, toma decisiones con `if-else` y repite tareas con bucles `for` y `while`.
* **Enlace:** [Ver la lección](https://www.youtube.com/watch?v=w2DgzHzalvQ)
* **Conclusiones clave:** `if (monedas >= precio) {}`; `for (int i = 1; i <= 3; i++) {}`; `while (energia > 0) {}`.
* **Práctica:** [Clic para programar](https://onlinegdb.com/-HlatXPEr) **¡No es necesario registrarse!**


### Lección 3: Métodos y Entrada/Salida de Datos (7:26 minutos)
* **Descripción:** Crea código reutilizable con métodos y recibe datos del usuario por consola usando `Scanner`.
* **Enlace:** [Ver la lección 3.1](https://youtu.be/d8fHd0szHwg?si=q3nGAqhbyXpdQYgX)
* **Enlace:** [Ver la lección 3.2](https://youtu.be/uKfFyXdJoYU?si=B9qGhec98OymKk-K)
* **Conclusiones clave:** `public static void greet() {}`; uso de `Scanner`.
* **Práctica:** [Clic para programar](https://jdoodle.com/execute-java-online/your-id) **¡Inicio inmediato!**


### Lección 4: Estudiantes, encapsulación, arrays y cadenas (12 minutos)
* **Descripción:** Crea una clase `Estudiante` con nombre y nota. Después protege sus datos y reúne varios estudiantes en un array para mostrar sus nombres en mayúsculas.
* **Enlace:** [Ver la lección 4](https://youtu.be/ft9aQ1GIczU)
* **Objetivos:** Crear objetos con `new` y un constructor; proteger atributos con `private`; consultar y modificar datos mediante getters y setters; validar notas enteras de 0 a 20, inclusive; recorrer un `Estudiante[]` con `for` y transformar cadenas con `toUpperCase()`.
* **Conclusiones clave:** Una clase es un molde y cada objeto tiene sus propios datos. Los arrays empiezan en la posición 0 y `grupo.length` indica cuántos elementos contienen. `toUpperCase()` devuelve texto en mayúsculas sin cambiar el nombre original.
* **Código inicial:** [starter-files/lesson-04/Main.java](./starter-files/lesson-04/Main.java), ejecutable desde el primer momento.
* **Ejemplo completo:** [completed-examples/lesson-04/Main.java](./completed-examples/lesson-04/Main.java), con encapsulación, validación y recorrido del grupo.
* **Práctica:** [Abrir el compilador Java de OnlineGDB](https://www.onlinegdb.com/online_java_compiler). El enlace compartible con el código precargado mediante **Share** queda pendiente de generación y verificación.

#### Cómo ejecutar la lección 4 en el navegador

1. Abre el código inicial o el ejemplo completo desde los enlaces anteriores y copia **un solo archivo completo**, incluidas las clases `Estudiante` y `Main`.
2. En OnlineGDB, selecciona **Java** y reemplaza todo el contenido de `Main.java` por el código copiado. No combines los dos archivos: cada uno funciona por separado, sin paquetes ni dependencias.
3. Pulsa **Run** y compara la consola con la salida correspondiente. Repite con el otro archivo, reemplazando todo el contenido anterior.

Salida del código inicial:

```text
Ana: 16
```

Salida del ejemplo completo:

```text
Nota invalida: debe estar entre 0 y 20.
ANA -> 18
LUIS -> 10
SOFIA -> 14
```

El constructor utiliza `setNota()` para aplicar la misma validación desde el principio. Una nota fuera del intervalo provoca un error `IllegalArgumentException`: el constructor no crea el estudiante y el setter conserva la nota anterior. En `main`, `try` intenta cambiar la nota a 21 y `catch` captura ese error, muestra el aviso y permite continuar. Las notas 0 y 20 sí son válidas.

#### Ejercicio de la lección 4

Agrega a Diego con nota 9 e inclúyelo en `grupo`. Comprueba que aparezcan los cuatro estudiantes y el nombre `DIEGO` en mayúsculas. Usa `setNombre()` para cambiar su nombre y consulta sus datos con `getNombre()` y `getNota()`. Prueba las notas 0 y 20; después intenta -1 y 21 tanto al construir un estudiante como al usar `setNota()`. Para cada intento inválido, usa un bloque `try/catch` como el del ejemplo: debe aparecer el aviso y, si usaste el setter, conservarse la última nota válida.


### Lección 5: Estructuras de Datos, Proyecto Final y Mejores Prácticas (12 minutos)
* **Descripción:** Combina arrays con objetos para construir una aplicación completa desde cero y aprende a evitar errores comunes de principiante.
* **Enlace:** [Ver la lección]([https://www.youtube.com/watch?v=example-link5](https://www.youtube.com/watch?v=1MZSEopU-hY))
* **Conclusiones clave:** Arreglos de objetos, depuración básica y buenas prácticas en Java.
* **Proyecto final:** [Crea tu aplicación POO](https://replit.com/@your-final-java) **¡Guarda y comparte!**


---


## Recursos adicionales


* **Código fuente completo:** [Repositorio de GitHub](https://github.com/Open-Source-1ASI0729-2620-7750/java-fundamentals-course-perutech)


### Todas las actividades prácticas


| Número de lección | Actividad | Empezar a programar |
| :--- | :--- | :--- |
| 1 | Hola mundo y Variables | [OnlineGDB](https://www.onlinegdb.com/) |
| 2 | Decisiones y Bucles | [OnlineGDB](https://www.onlinegdb.com/) |
| 3 | Métodos y Scanner | [JDoodle](https://jdoodle.com/execute-java-online/your-lesson3) |
| 4 | Estudiantes, encapsulación, arrays y cadenas | [OnlineGDB](https://www.onlinegdb.com/online_java_compiler) · [Código inicial](./starter-files/lesson-04/Main.java) · [Ejemplo completo](./completed-examples/lesson-04/Main.java) |
| 5 | Proyecto Integrador POO | [Replit](https://replit.com/@your-lesson5) |


* **Compartir:** #JavaBeginners


**¡Gracias por completar el curso!**


---


## Elaboración


* **Institución:** Universidad Peruana de Ciencias Aplicadas
* **Carrera:** Ingeniería de Software
* **Período:** 202620
* **Curso:** 1ASI0729 Desarrollo de Aplicaciones Open Source
* **NRC:** 7750
* **Nombre del equipo:** Perutech
* **Líder del equipo:** MCapillo Lema, Mía Valentina
* **Integrantes del equipo:**
  * Capillo Lema, Mía Valentina
  * Pardo Chumpitazi, Kevin Patrick
  * Becerra Durand, Sebastian Uriel
  * Miranda Romero, Sergio Luis
  * Casos Torre, Miguel Andre
* **Fecha de entrega:** 14/11/2026
