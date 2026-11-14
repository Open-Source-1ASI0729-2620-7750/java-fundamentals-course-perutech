# Fundamentos de Java para Principiantes


## Resumen del Curso


Este curso introductorio, con una duración audiovisual de 52 minutos y 41 segundos según los metadatos consultados, introduce a estudiantes de secundaria a los fundamentos de la programación con Java, incluyendo programación orientada a objetos.


* **Duración total de videos:** 52:41 según metadatos de YouTube consultados el 14/11/2026. Reserva unos 60 minutos de visualización y pausas; el tiempo de práctica adicional depende de cada estudiante.
* **Público Objetivo:** Estudiantes de 12 a 17 años sin experiencia en programación
* **Prerrequisitos:** Ningún conocimiento previo de programación. Sigue las lecciones en orden; necesitas un navegador y conexión a Internet.
* **Herramientas necesarias:** **¡Solo tu navegador web!** (Chrome, Firefox, Safari, Edge). Se utilizan las modalidades gratuitas de OnlineGDB, JDoodle y OneCompiler. Replit es una alternativa; revisa sus condiciones y requisitos de cuenta antes de elegirlo.
* **Repositorio de Código Fuente:** [https://github.com/Open-Source-1ASI0729-2620-7750/java-fundamentals-course-perutech](https://github.com/Open-Source-1ASI0729-2620-7750/java-fundamentals-course-perutech)


---


## Secuencia de las lecciones


### Lección 1: ¿Qué es Java y la programación? (10:38 minutos)
* **Descripción:** Aprende qué es la programación, por qué Java es un excelente lenguaje para empezar y cómo declarar tus primeras variables.
* **Enlace:** [Ver la lección](https://youtu.be/O-vM5T0-jkY)
* **Conclusiones clave:** Java se usa para aplicaciones y juegos; los programas son instrucciones para computadoras; uso de `int`, `String` y `boolean`.
* **Objetivos:** Mostrar mensajes con `System.out.println`, declarar variables `String`, `int`, `double` y `boolean`, y calcular un total con multiplicación.
* **Empieza a programar:** [OnlineGDB, carga manual](https://www.onlinegdb.com/online_java_compiler). Enlace con código precargado: **pendiente**.
* **Código:** [Inicial](./starter-files/leccion1.java) · [Completo](./completed-examples/leccion1.java) · [Guion](./scripts/leccion1.md).
* **Ejercicio:** Cambia el nombre y la edad; modifica el precio y la cantidad y comprueba el total.
* **Continuidad:** Usarás estas variables para tomar decisiones y repetir acciones en la lección 2.


### Lección 2: Operadores y estructuras de control (13:11 minutos)
* **Descripción:** Realiza operaciones, toma decisiones con `if-else` y repite tareas con bucles `for` y `while`.
* **Enlace:** [Ver la lección](https://www.youtube.com/watch?v=w2DgzHzalvQ)
* **Conclusiones clave:** `if (monedas >= precio) {}`; `for (int i = 1; i <= 3; i++) {}`; `while (energia > 0) {}`.
* **Objetivos:** Comparar valores con operadores, elegir entre ramas `if/else`, repetir tareas con `for` y `while`, y llamar métodos con parámetros y retorno. Los métodos se presentan aquí y se reutilizan en la lección 3.
* **Práctica:** [Proyecto compartido por el equipo en OnlineGDB](https://onlinegdb.com/-HlatXPEr). El enlace responde HTTP 200; la carga del código, su ejecución y el acceso sin cuenta requieren comprobación manual.
* **Código:** [Inicial](./starter-files/leccion2.java) · [Completo](./completed-examples/leccion2.java) · [Guion](./scripts/leccion2.md).
* **Ejercicio:** Completa `verificarRecord(int puntaje)` en el inicial. Muestra un aviso distinto para puntajes menores que 500 y para 500 o más; llama al método con ambos casos. Es un reto adicional: ese método no aparece en el ejemplo completo.
* **Continuidad:** En la lección 3 recibirás los datos del usuario, en lugar de escribir siempre valores fijos.


### Lección 3: Métodos, entrada/salida y primeros objetos (7:28 minutos en dos partes)
* **Descripción:** Reutiliza los métodos y parámetros presentados en la lección 2, recibe datos por consola con `Scanner` (parte 3.1) y representa mascotas con clases, constructores y métodos (parte 3.2).
* **Enlace (3:14):** [Ver la lección 3.1](https://youtu.be/d8fHd0szHwg?si=q3nGAqhbyXpdQYgX)
* **Enlace (4:14):** [Ver la lección 3.2](https://youtu.be/uKfFyXdJoYU?si=B9qGhec98OymKk-K)
* **Conclusiones clave:** `Scanner.nextLine()` y `nextInt()`; parámetros de constructor; clase `Mascota`, objetos creados con `new` y método `comer()`. Cada objeto mantiene su propia energía.
* **Objetivos:** Leer nombre y edad, mostrar una respuesta, reconocer atributos y constructores, e invocar un método en dos objetos distintos.
* **Práctica:** [JDoodle, carga manual](https://www.jdoodle.com/online-java-compiler). Los enlaces anteriores con `your-id` y `your-lesson3` devolvieron HTTP 404 y se retiraron. Faltan enlaces compartibles para ambas partes.
* **Código 3.1:** [Inicial](./starter-files/lesson3.1.java) · [Completo](./completed-examples/lesson3.1.java) · [Guion](./scripts/lesson3.1.md).
* **Código 3.2:** [Inicial](./starter-files/lesson3.2.java) · [Completo](./completed-examples/lesson3.2.java) · [Guion](./scripts/leccion3.2.md).
* **Ejercicio:** Ejecuta la parte 3.1 con `Ana` y `15` en líneas separadas. En la parte 3.2, agrega una tercera mascota y llama a `comer()` dos veces en ella; su energía debe llegar a 140.
* **Continuidad:** La lección 4 cambia el ejemplo a `Estudiante` para aprender a proteger los atributos. No es necesario que ambas clases tengan el mismo nombre.


### Lección 4: Estudiantes, encapsulación, arrays y cadenas (11:01 minutos)
* **Descripción:** Crea una clase `Estudiante` con nombre y nota. Después protege sus datos y reúne varios estudiantes en un array para mostrar sus nombres en mayúsculas.
* **Enlace:** [Ver la lección 4](https://youtu.be/ft9aQ1GIczU)
* **Objetivos:** Crear objetos con `new` y un constructor; proteger atributos con `private`; consultar y modificar datos mediante getters y setters; validar notas enteras de 0 a 20, inclusive; recorrer un `Estudiante[]` con `for` y transformar cadenas con `toUpperCase()`.
* **Conclusiones clave:** Una clase es un molde y cada objeto tiene sus propios datos. Los arrays empiezan en la posición 0 y `grupo.length` indica cuántos elementos contienen. `toUpperCase()` devuelve texto en mayúsculas sin cambiar el nombre original.
* **Código inicial:** [starter-files/lesson-04/Main.java](./starter-files/lesson-04/Main.java), ejecutable desde el primer momento.
* **Ejemplo completo:** [completed-examples/lesson-04/Main.java](./completed-examples/lesson-04/Main.java), con encapsulación, validación y recorrido del grupo.
* **Práctica:** [Abrir el compilador Java de OnlineGDB](https://www.onlinegdb.com/online_java_compiler). Enlace compartible con código precargado: **pendiente**; la carga manual permite realizar la práctica mientras el equipo lo prepara.

* **Guion recomendado:** [Secuencia de estudiantes](./scripts/lesson-04.md). El [guion anterior de libros](./scripts/leccion4.md) y los archivos `leccion4.java` se conservan como material alternativo, no como el punto de partida recomendado para este video.
* **Continuidad:** En la lección 5 reutilizarás encapsulación, métodos y arrays en un gestor de mascotas. Cambia el dominio del ejemplo, pero se conservan los conceptos.

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


### Lección 5: Estructuras de datos, proyecto final y mejores prácticas (10:23 minutos)

* **Responsable:** Becerra Durand, Sebastian Uriel
* **Descripción:** Aprende a utilizar arrays en Java y a combinarlos con objetos mediante el desarrollo de un proyecto integrador basado en un Gestor de Mascotas.
* **Enlace:** [Ver la lección](https://youtu.be/1MZSEopU-hY)
* **Conclusiones clave:** Uso de arrays, recorrido de arreglos con `for-each`, arreglos de objetos, métodos, depuración básica mediante `ArrayIndexOutOfBoundsException` y buenas prácticas de programación.
* **Proyecto final:** Desarrollo de un **Gestor de Mascotas** que almacena objetos de tipo `Pet`, muestra su información, contabiliza las mascotas registradas e identifica la mascota de mayor edad.
* **Objetivos:** Recorrer arrays con `for-each`, almacenar objetos `Pet`, consultar `pets.length`, encontrar la mayor edad y reconocer un acceso fuera de límites.
* **Práctica:** [OneCompiler, carga manual](https://onecompiler.com/java). Enlace con código precargado: **pendiente**. No requiere instalación.
* **Código:** [Inicial](./starter-files/leccion5.java) · [Completo](./completed-examples/leccion5.java) · [Guion](./scripts/leccion5.md).
* **Ejercicio:** Agrega una mascota mayor de cinco años. Deben aparecer cinco mascotas y el nuevo nombre como el de mayor edad. Mantén el array con al menos un elemento: `findOldestPet()` parte de `pets[0]` y no admite un array vacío.
* **Cierre y continuidad:** Explica qué hace cada método y practica cambios pequeños, ejecutando después de cada uno. Puedes continuar con la búsqueda de mascotas por nombre.


---


## Duraciones y comprobaciones audiovisuales

Las duraciones anteriores proceden del campo `videoDetails.lengthSeconds` de las páginas de YouTube, consultado el 14/11/2026. Los seis enlaces respondieron HTTP 200 y el reproductor informó estado `OK`; esto no equivale a haber visto los videos ni a verificar su visibilidad en YouTube Studio.

| Lección o parte | Duración según metadatos | Comprobación pendiente |
| :--- | :--- | :--- |
| 1 | 10:38 | Reproducción, contenido, subtítulos y visibilidad No listado |
| 2 | 13:11 | Reproducción, contenido, subtítulos y visibilidad No listado |
| 3.1 | 3:14 | Menos de 5 minutos por video; validar con docente |
| 3.2 | 4:14 | Menos de 5 minutos; su título en YouTube dice Lección 4; confirmar correspondencia |
| 4 | 11:01 | Correspondencia del código y validación de notas con lo grabado |
| 5 | 10:23 | Reproducción, contenido, subtítulos y visibilidad No listado |
| **Total** | **52:41** | Confirmar aceptación como aproximadamente una hora |

No se modificaron los videos. La progresión se revisó a partir de guiones y código, no mediante una revisión audiovisual completa. La validación de privacidad de todos los videos y la calidad de narración y pantalla corresponden al equipo.

## Cómo practicar sin instalar programas

1. Abre un enlace de código inicial y copia su contenido completo.
2. Abre el editor indicado, selecciona Java y pega un solo ejemplo en `Main.java`. Los archivos históricos `leccion1.java`, `lesson3.1.java`, etc. contienen `public class Main`: en el editor el nombre debe ser `Main.java`.
3. Pulsa **Run**. Los iniciales con instrucciones `TODO` pueden terminar sin salida hasta que completes el reto; esto es esperado.
4. En la parte 3.1, activa la entrada estándar del editor y proporciona el nombre y la edad en líneas separadas. Usa una edad entera para seguir el ejemplo.
5. Repite con el ejemplo completo, reemplazando todo el contenido. No ejecutes todos los archivos juntos: repiten nombres de clases y son programas independientes.
6. Compara con las [salidas verificadas](./verification/java-results.json). En OneCompiler, la entrada estándar se encuentra bajo I/O / STDIN, según su documentación del editor.

Todos los ejemplos se compilaron y ejecutaron de forma aislada con JDK 27 y destino Java 17, sin dependencias externas. Esto verifica el código localmente; la ejecución en cada editor concreto aún requiere la revisión indicada en las prácticas.

## Recursos adicionales


* **Código fuente completo:** [Repositorio de GitHub](https://github.com/Open-Source-1ASI0729-2620-7750/java-fundamentals-course-perutech)


### Todas las actividades prácticas


| Número de lección | Actividad | Empezar a programar |
| :--- | :--- | :--- |
| 1 | Hola mundo y variables | [Carga manual](https://www.onlinegdb.com/online_java_compiler); falta enlace precargado |
| 2 | Decisiones y bucles | [Proyecto del equipo](https://onlinegdb.com/-HlatXPEr); validar carga y ejecución |
| 3 | Scanner y objetos | [Carga manual](https://www.jdoodle.com/online-java-compiler); faltan enlaces de 3.1 y 3.2 |
| 4 | Estudiantes, encapsulación, arrays y cadenas | [OnlineGDB](https://www.onlinegdb.com/online_java_compiler) · [Código inicial](./starter-files/lesson-04/Main.java) · [Ejemplo completo](./completed-examples/lesson-04/Main.java) |
| 5 | Proyecto integrador POO - Gestor de Mascotas | [Carga manual](https://onecompiler.com/java); falta enlace precargado |


* **Compartir:** #JavaBeginners


**¡Gracias por completar el curso!**


---


## Elaboración


* **Institución:** Universidad Peruana de Ciencias Aplicadas
* **Carrera:** Ingeniería de Software
* **Período:** 202620
* **Curso:** 1ASI0729 Desarrollo de Aplicaciones Open Source
* **NRC:** 7750
* **Nombre del equipo:** PeruTech
* **Líder del equipo:** Capillo Lema, Mía Valentina
* **Integrantes del equipo:**
  * Capillo Lema, Mía Valentina
  * Pardo Chumpitazi, Kevin Patrick
  * Becerra Durand, Sebastian Uriel
  * Miranda Romero, Sergio Luis
  * Casos Torre, Miguel Andre
* **Fecha de preparación:** 14/11/2026. Confirmar el plazo oficial en el Aula Virtual.
