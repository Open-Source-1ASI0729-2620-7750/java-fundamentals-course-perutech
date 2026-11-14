# Verificación pública de la entrega

Preparación: 14/11/2026. PeruTech, UPC, curso 1ASI0729, ciclo 202620, NRC 7750.

Los reportes de participación Word/PDF se conservan exclusivamente en local por indicación del usuario. No están en los archivos, commits, historial o ZIP de esta rama. La documentación pública del curso mantiene los nombres del equipo que ya figuran en main, sin publicar calificaciones ni evaluaciones individuales.

## Matriz de requisitos

| Requisito | Estado | Evidencia | Observaciones |
| :--- | :--- | :--- | :--- |
| Revisión inicial del repositorio | COMPLETO | Status, remotos, fetch, estructura y commits | Base origin/main: 423b00a; se preservaron todos los aportes |
| Rama publicable aislada | COMPLETO | docs/entrega-trabajo-complementario | Parte directamente de origin/main; no hereda commits de los reportes locales |
| Cinco lecciones documentadas | COMPLETO | README y course-plan.md | Objetivos, descripción, conceptos, código, ejercicio y continuidad |
| Código independiente | COMPLETO | java-results.json | 14 Java compilados y ejecutados con comparación de salidas |
| Lección 4 y validación | COMPLETO | lesson-04/Main.java y pruebas | Constructor, private, getters/setters, array, for y mayúsculas; ocho casos límite de notas |
| Conservación de aportaciones | COMPLETO | Diff y archivos originales | Sin cambios de comportamiento ni eliminaciones de Java o guiones anteriores |
| Enlaces actuales por HTTP | COMPLETO | links-results.json | Respuestas 200; los enlaces ficticios anteriores de JDoodle dieron 404 |
| Duraciones documentadas | COMPLETO | Metadatos videoDetails.lengthSeconds | Seis videos, total 52:41 |
| Videos de 5-15 minutos | REQUIERE VALIDACIÓN | Partes 3.1 de 3:14 y 3.2 de 4:14 | Resolver con el docente; no se modificaron los videos |
| Aproximadamente una hora | REQUIERE VALIDACIÓN | Total audiovisual 52:41 | Confirmar aceptación académica |
| Correspondencia de 3.2 | REQUIERE VALIDACIÓN | Su título en YouTube dice Lección 4 | Confirmar la etiqueta de la secuencia |
| Privacidad y calidad de videos | REQUIERE VALIDACIÓN | Enlaces y metadatos consultados | Revisar reproducción, audio, legibilidad, contenido y No listado; no se afirma revisión audiovisual completa |
| Prácticas precargadas | PENDIENTE | Tabla inferior | El host de automatización del navegador no está disponible |
| Enlace compartido de 2 | REQUIERE VALIDACIÓN | OnlineGDB -HlatXPEr, HTTP 200 | Se conserva; verificar código, ejecución y acceso sin cuenta |
| README y plan | COMPLETO | Archivos corregidos y ampliados | Se mantuvo el plan del equipo como base y se corrigió la etiqueta PDF |
| Plan PDF completo | COMPLETO | deliverables y artifact-results.json | Siete páginas, enlaces clicables y revisión visual |
| ZIP de artefactos | COMPLETO | zip-manifest.json | 23 archivos, sin Git, IDE, reportes, credenciales ni compilados |
| Reporte de participación | REQUIERE VALIDACIÓN | Conservado solo en local | La líder completa calificaciones y valida el documento; no se publica |
| Rúbrica y plazo oficial | REQUIERE VALIDACIÓN | Requisitos proporcionados por el usuario | Contrastar con el enunciado específico y los campos del Aula Virtual |

## Prácticas: intervención exacta

| Lección | Código inicial | Acción pendiente |
| :--- | :--- | :--- |
| 1 | starter-files/leccion1.java | Crear Share de OnlineGDB y probar sin cuenta |
| 2 | starter-files/leccion2.java | Revisar y ejecutar el enlace existente del equipo |
| 3.1 | starter-files/lesson3.1.java | Compartir proyecto del editor y probar nombre y edad por entrada estándar |
| 3.2 | starter-files/lesson3.2.java | Compartir proyecto independiente y probar el reto completado |
| 4 | starter-files/lesson-04/Main.java | Crear y comprobar Share con Estudiante |
| 5 | starter-files/leccion5.java | Crear proyecto compartido en OneCompiler y probar el ejemplo final |

Los enlaces de carga manual no se presentan como proyectos precargados. Los enlaces ficticios `your-id` y `your-lesson3` se retiraron; el registro HTTP anterior está en links-baseline.json.

## Precisiones técnicas

Cada archivo histórico contiene public class Main y se copia como Main.java para ejecutarlo. Los iniciales con TODO pueden terminar sin salida. El reto verificarRecord de lección 2 es adicional al ejemplo completo. El array del gestor de mascotas debe contener al menos un elemento; no se cambió el comportamiento grabado.

En la lección 4 se recomienda Estudiante. Los archivos leccion4.java de libros y su guion se conservan como alternativa. La correspondencia de la excepción de notas con lo grabado requiere revisión del responsable; no se afirma que el guion de apoyo sea una transcripción.

## Rúbrica suministrada

| Criterio | Máximo | Estado |
| :--- | :--- | :--- |
| Course Structure & Flow | 4 | Documentado; validar secuencia audiovisual |
| Technical Accuracy | 4 | Código probado; validar correspondencia en pantalla |
| Target Audience Engagement | 5 | Retos documentados; revisar interacción y narración |
| Video Production Quality | 4 | Requiere revisión audiovisual |
| Course Outline Document | 3 | Plan Markdown y PDF preparados |

No se asigna una nota anticipada. La rúbrica oficial específica no se encontró en los archivos disponibles; el enunciado general de otro proyecto no la sustituye.

## Entrega en el Aula Virtual

1. La líder revisa los reportes locales, confirma responsabilidades y calificaciones, y valida el Word. Exportar otra vez ese Word editado a PDF para que ambos formatos coincidan.
2. El equipo valida videos, visibilidad, duraciones y prácticas con código precargado. Si se actualizan enlaces, regenerar plan PDF y ZIP.
3. Revisar el PR de documentación. No hacer merge automáticamente.
4. Adjuntar al Aula Virtual el plan PDF y los reportes locales aprobados. Adjuntar el ZIP si corresponde y completar los campos de enlaces requeridos.
5. Confirmar plazo, adjuntos y comprobante de envío. Este trabajo no envía nada al Aula Virtual.
