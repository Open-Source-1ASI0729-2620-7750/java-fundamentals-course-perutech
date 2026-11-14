# Lección 4: Estudiantes, encapsulación, arrays y cadenas

Video: https://youtu.be/ft9aQ1GIczU. Duración según metadatos: 11:01.

Esta secuencia de apoyo utiliza los archivos recomendados de `Estudiante`. No es una transcripción del video; su correspondencia audiovisual debe revisarla el responsable.

1. Abrir `starter-files/lesson-04/Main.java` como `Main.java` en el editor. Ejecutar y observar `Ana: 16`.
2. Recordar clase, atributos, constructor, `new` y `mostrar()`. Explicar que los atributos sin protección pueden recibir datos que no representan una nota válida.
3. Añadir `private` y los getters/setters del ejemplo completo. Mostrar que el constructor llama a `setNota()` y que se admiten notas de 0 a 20.
4. Explicar brevemente `IllegalArgumentException` y `try/catch`: el código completo rechaza 21 y continúa, conservando la nota 18. Contrastar esa decisión con lo grabado antes de presentar este material como transcripción.
5. Crear a Luis y Sofia, agruparlos con Ana en `Estudiante[]` y recorrer el array desde cero hasta `grupo.length - 1`.
6. Mostrar los nombres mediante `toUpperCase()` y comparar la salida con `course-plan.md`. El nombre almacenado no cambia.
7. Proponer agregar a Diego y probar 0, 20, -1 y 21, tanto en constructor como en setter. Conectar con el array de mascotas de la lección 5.

El guion anterior `leccion4.md` y los archivos de libros se conservan como alternativa, sin sustituir las aportaciones de sus autores.
