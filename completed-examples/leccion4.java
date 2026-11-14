
class Libro {
    private String titulo;
    private String autor;
    private int paginas;

    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }

    public int getPaginas() {
        return paginas;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public void setPaginas(int paginas) {
        if (paginas > 0) {
            this.paginas = paginas;
        } else {
            System.out.println("El número de páginas debe ser mayor que cero.");
        }
    }
}

public class Main {
    public static void main(String[] args) {

        Libro[] biblioteca = new Libro[3];

        biblioteca[0] = new Libro();
        biblioteca[1] = new Libro();
        biblioteca[2] = new Libro();

        biblioteca[0].setTitulo("Java desde cero");
        biblioteca[0].setAutor("Carlos Ruiz");
        biblioteca[0].setPaginas(180);

        biblioteca[1].setTitulo("Aprendiendo programación");
        biblioteca[1].setAutor("Ana Torres");
        biblioteca[1].setPaginas(220);

        biblioteca[2].setTitulo("Introducción a Java");
        biblioteca[2].setAutor("Luis Pérez");
        biblioteca[2].setPaginas(150);

        System.out.println("CATÁLOGO DE LA BIBLIOTECA");

        for (int i = 0; i < biblioteca.length; i++) {
            System.out.println("\nLibro " + (i + 1));
            System.out.println("Título: " + biblioteca[i].getTitulo());
            System.out.println("Autor: " + biblioteca[i].getAutor());
            System.out.println("Páginas: " + biblioteca[i].getPaginas());
        }

        String palabraBuscada = "java";
        boolean encontrado = false;

        System.out.println("\nRESULTADO DE LA BÚSQUEDA");

        for (int i = 0; i < biblioteca.length; i++) {
            String titulo = biblioteca[i].getTitulo();

            if (titulo.toLowerCase().contains(palabraBuscada.toLowerCase())) {
                System.out.println("Libro encontrado: " + titulo);
                encontrado = true;
            }
        }

        if (!encontrado) {
            System.out.println("No se encontraron libros con esa palabra.");
        }
    }
}
