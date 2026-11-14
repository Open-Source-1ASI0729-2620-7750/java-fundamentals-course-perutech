# Verificación y exportación pública del curso

El alumnado solo necesita un navegador. Estas herramientas sirven al equipo para reproducir la documentación y las comprobaciones.

## Dependencias

Python 3.12, Git y JDK 17 o posterior. Para generar y verificar el PDF se necesitan ReportLab y pypdf, con las versiones de `requirements.txt`. La preparación utilizó las bibliotecas del runtime de Codex, sin instalar paquetes Python adicionales.

```text
python -m venv .venv
.venv\Scripts\python -m pip install -r tools/requirements.txt
```

No subir el entorno virtual ni archivos temporales. En Linux o macOS se usa `.venv/bin/python`.

## Ejecutar las comprobaciones

Desde la raíz del repositorio:

```text
python tools/verify_java.py --java-home RUTA_AL_JDK
python tools/check_links.py
python tools/build_deliverables.py
python tools/verify_artifacts.py
```

Los Java se copian como `Main.java` en directorios temporales independientes, se compilan con destino Java 17 y se ejecutan comparando las salidas completas. El programa de Scanner recibe nombre y edad por entrada estándar. Los temporales se eliminan al terminar.

La comprobación HTTP de enlaces no sustituye la reproducción de videos ni la ejecución de prácticas en una sesión del editor. La visibilidad No listado se verifica en YouTube Studio.

El generador público exporta únicamente el plan completo a PDF y el ZIP con README, plan y las tres carpetas pedagógicas. Los enlaces locales del PDF apuntan a la rama de revisión de GitHub. En Windows utiliza Arial y Consolas; en otros sistemas, Helvetica y Courier.

El verificador comprueba contenido completo del plan PDF, enlaces clicables, enlaces relativos de la documentación, salidas Java e integridad y bytes del ZIP. Además hay que revisar visualmente todas las páginas renderizadas, por ejemplo con Poppler: `pdftoppm -png -r 110 archivo.pdf prefijo`.

## Reportes de participación

Por decisión del usuario, el Word, el PDF de participación y su evidencia individual se conservan solo en la copia local del equipo. No se incluyen en esta rama, en su historial ni en el ZIP. Su exportador y su plantilla individual tampoco se publican aquí. La líder debe completarlos y aprobarlos antes del envío académico.
