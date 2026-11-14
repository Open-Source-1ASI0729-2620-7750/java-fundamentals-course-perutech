"""Verifica cada ejemplo por separado sin generar .class en el repositorio."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--java-home', type=Path, required=True)
    args = parser.parse_args()
    suffix = '.exe' if (args.java_home / 'bin/java.exe').exists() else ''
    java, javac = [str(args.java_home / 'bin' / (name + suffix)) for name in ('java', 'javac')]
    expected = {
        'starter-files/leccion1.java': '',
        'starter-files/leccion2.java': '=== BIENVENIDO A LA LECCION 2 ===\n',
        'starter-files/leccion4.java': '',
        'starter-files/leccion5.java': '',
        'starter-files/lesson3.1.java': '',
        'starter-files/lesson3.2.java': '',
        'starter-files/lesson-04/Main.java': 'Ana: 16\n',
        'completed-examples/leccion1.java': 'Hola, estoy aprendiendo Java\nNombre: Lucia\nEdad: 16\nNota: 18.5\nEstudiante activo: true\nTotal a pagar: 150\n',
        'completed-examples/lesson3.1.java': '¡Hola! ¿Cómo te llamas?\n¿Cuántos años tienes?\nGenial, Ana. Tienes 15 años. ¡Bienvenido al mundo de la programación!\n',
        'completed-examples/lesson3.2.java': 'Firulais comió croquetas. Su energía subió a: 120\nPelusa comió croquetas. Su energía subió a: 120\n',
        'completed-examples/lesson-04/Main.java': 'Nota invalida: debe estar entre 0 y 20.\nANA -> 18\nLUIS -> 10\nSOFIA -> 14\n',
        'completed-examples/leccion4.java': 'CATÁLOGO DE LA BIBLIOTECA\n\nLibro 1\nTítulo: Java desde cero\nAutor: Carlos Ruiz\nPáginas: 180\n\nLibro 2\nTítulo: Aprendiendo programación\nAutor: Ana Torres\nPáginas: 220\n\nLibro 3\nTítulo: Introducción a Java\nAutor: Luis Pérez\nPáginas: 150\n\nRESULTADO DE LA BÚSQUEDA\nLibro encontrado: Java desde cero\nLibro encontrado: Introducción a Java\n',
        'completed-examples/leccion5.java': '=== MIS MASCOTAS ===\nNombre: Luna | Edad: 3 | Tipo: Perro\nNombre: Michi | Edad: 2 | Tipo: Gato\nNombre: Rocky | Edad: 5 | Tipo: Perro\nNombre: Nala | Edad: 1 | Tipo: Gato\n\nCantidad de mascotas registradas: 4\n\nLa mascota de mayor edad es: Rocky con 5 años.\n\n=== PROGRAMA FINALIZADO ===\n',
    }
    expected['completed-examples/leccion2.java'] = '\n'.join([
        '=== LECCION 2: ESTRUCTURAS DE CONTROL Y METODOS ===', '',
        '--- 1. Decisiones con if - else ---',
        'Caso 1: Compra exitosa! Te alcanza para la espada.', 'Monedas restantes: 20',
        'Caso 2: No te alcanza para la armadura, solo tienes 20 monedas.', '',
        '--- 2. Rangos con else if ---', 'Rango actual: Avanzado', '',
        '--- 3. Repeticiones con bucle for ---',
        *[f'Completando mision diaria numero: {n}' for n in (1, 2, 3)], '',
        '--- 4. Repeticiones con bucle while ---',
        *[f'Entrenando personaje... Energia actual: {n}' for n in (3, 2, 1)],
        'Personaje sin energia, hora de descansar!', '', '--- 5. Usando nuestros metodos ---',
        '-----------------------------------', 'Hola, Alex! Listo para la mision.',
        '-----------------------------------', 'Hola, Sofia! Listo para la mision.',
        'El puntaje total obtenido es: 300', ''])
    files = sorted([*ROOT.glob('starter-files/**/*.java'), *ROOT.glob('completed-examples/**/*.java')])
    assert {f.relative_to(ROOT).as_posix() for f in files} == set(expected), 'Actualizar expectativas para archivos nuevos'
    results = []
    version = subprocess.run([javac, '-version'], capture_output=True, text=True, check=True).stdout.strip()
    with tempfile.TemporaryDirectory(prefix='perutech-java-') as temporary:
        for index, source in enumerate(files):
            relative = source.relative_to(ROOT).as_posix()
            folder = Path(temporary) / str(index)
            folder.mkdir()
            shutil.copyfile(source, folder / 'Main.java')
            subprocess.run([javac, '-encoding', 'UTF-8', '--release', '17', '-d', str(folder), str(folder / 'Main.java')], capture_output=True, check=True, timeout=30)
            stdin = 'Ana\n15\n' if relative == 'completed-examples/lesson3.1.java' else ''
            process = subprocess.run([java, '-Dfile.encoding=UTF-8', '-Dstdout.encoding=UTF-8', '-Dstderr.encoding=UTF-8', '-cp', str(folder), 'Main'], input=stdin.encode(), capture_output=True, check=True, timeout=15)
            output = process.stdout.decode('utf-8').replace('\r\n', '\n')
            assert output == expected[relative], f'Salida distinta: {relative}: {output!r}'
            results.append({'file': relative, 'sha256': hashlib.sha256(source.read_bytes()).hexdigest(), 'compiled': True, 'executed': True, 'exact_output': True, 'stdin': stdin, 'stdout': output})
            if relative == 'completed-examples/lesson-04/Main.java':
                harness = '''public class BoundaryCheck {
    public static void main(String[] args) {
        int checks = 0;
        for (int grade : new int[]{0, 20}) {
            Estudiante e = new Estudiante("Ana", grade);
            if (e.getNota() != grade) throw new AssertionError("constructor " + grade);
            checks++;
            e.setNota(10); e.setNota(grade);
            if (e.getNota() != grade) throw new AssertionError("setter " + grade);
            checks++;
        }
        for (int grade : new int[]{-1, 21}) {
            boolean rejected = false;
            try { new Estudiante("Ana", grade); } catch (IllegalArgumentException ex) { rejected = true; }
            if (!rejected) throw new AssertionError("constructor " + grade);
            checks++;
            Estudiante e = new Estudiante("Ana", 16); rejected = false;
            try { e.setNota(grade); } catch (IllegalArgumentException ex) { rejected = true; }
            if (!rejected || e.getNota() != 16) throw new AssertionError("setter " + grade);
            checks++;
        }
        Estudiante e = new Estudiante("Ana", 16); e.setNombre("Sofia");
        if (!e.getNombre().equals("Sofia")) throw new AssertionError("get/set nombre");
        System.out.println("PASS " + checks + " casos limite y get/set nombre");
    }
}'''
                (folder / 'BoundaryCheck.java').write_text(harness, encoding='utf-8')
                subprocess.run([javac, '--release', '17', '-cp', str(folder), '-d', str(folder), str(folder / 'BoundaryCheck.java')], check=True, capture_output=True)
                boundary = subprocess.run([java, '-cp', str(folder), 'BoundaryCheck'], check=True, capture_output=True, text=True).stdout.strip()
            print('PASS', relative)
    report = {'prepared_date': '2026-11-14', 'compiler': version, 'release': 17, 'independent_files': len(results), 'boundary_result': boundary, 'results': results}
    target = ROOT / 'verification/java-results.json'
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(boundary)


if __name__ == '__main__':
    main()
