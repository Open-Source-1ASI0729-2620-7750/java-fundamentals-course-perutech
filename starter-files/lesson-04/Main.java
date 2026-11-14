class Estudiante {
    String nombre;
    int nota;

    public Estudiante(String nombre, int nota) {
        this.nombre = nombre;
        this.nota = nota;
    }

    public void mostrar() {
        System.out.println(nombre + ": " + nota);
    }
}

public class Main {
    public static void main(String[] args) {
        Estudiante ana = new Estudiante("Ana", 16);
        ana.mostrar();
        // Reto: protege los atributos y agrega otros estudiantes.
    }
}
