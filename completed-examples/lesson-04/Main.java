class Estudiante {
    private String nombre;
    private int nota;

    public Estudiante(String nombre, int nota) {
        this.nombre = nombre;
        // La misma regla se aplica al crear y al modificar una nota.
        setNota(nota);
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getNota() {
        return nota;
    }

    public void setNota(int nuevaNota) {
        if (nuevaNota < 0 || nuevaNota > 20) {
            throw new IllegalArgumentException("Nota invalida: debe estar entre 0 y 20.");
        }
        this.nota = nuevaNota;
    }

    public void mostrar() {
        // toUpperCase() devuelve otro texto; no modifica el nombre guardado.
        System.out.println(nombre.toUpperCase() + " -> " + nota);
    }
}

public class Main {
    public static void main(String[] args) {
        Estudiante ana = new Estudiante("Ana", 16);
        Estudiante luis = new Estudiante("Luis", 10);
        Estudiante sofia = new Estudiante("Sofia", 14);

        ana.setNota(18);
        // Capturamos el error para poder continuar con el programa.
        try {
            ana.setNota(21);
        } catch (IllegalArgumentException error) {
            System.out.println(error.getMessage());
        }

        Estudiante[] grupo = {ana, luis, sofia};
        // Las posiciones del array comienzan en 0.
        for (int i = 0; i < grupo.length; i++) {
            grupo[i].mostrar();
        }
    }
}
