// 1. EL MOLDE (La Clase)
class Mascota {
    // Atributos (Lo que la mascota TIENE)
    String nombre;
    int energia;

    // El Constructor (Una función especial que da vida al objeto al nacer)
    public Mascota(String nombreInicial) {
        nombre = nombreInicial;
        energia = 100; // Toda mascota nace con 100 de energía por defecto
    }

    // Método (Lo que la mascota HACE)
    public void comer() {
        energia += 20;
        System.out.println(nombre + " comió croquetas. Su energía subió a: " + energia);
    }
}

// 2. EL PROGRAMA PRINCIPAL
public class Main {
    public static void main(String[] args) {
        // Creamos los objetos (Las mascotas reales usando el molde)
        Mascota m1 = new Mascota("Firulais");
        Mascota m2 = new Mascota("Pelusa");

        // Usamos los métodos de cada objeto de forma independiente
        m1.comer();
        m2.comer();
    }
}