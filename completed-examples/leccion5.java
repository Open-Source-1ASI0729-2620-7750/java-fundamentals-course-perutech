// ==========================================================
// LECCIÓN 5 - PROYECTO FINAL
// Gestor de Mascotas
// ==========================================================


// Creamos la clase Pet.
// Esta clase funciona como una plantilla para representar mascotas.

class Pet {

    // Atributos de cada mascota.
    private String name;
    private int age;
    private String type;


    // Constructor.
    // Permite asignar los datos al crear una nueva mascota.
    public Pet(String name, int age, String type) {
        this.name = name;
        this.age = age;
        this.type = type;
    }


    // Devuelve el nombre de la mascota.
    public String getName() {
        return name;
    }


    // Devuelve la edad de la mascota.
    public int getAge() {
        return age;
    }


    // Muestra toda la información de una mascota.
    public void showInfo() {
        System.out.println(
                "Nombre: " + name
                        + " | Edad: " + age
                        + " | Tipo: " + type
        );
    }
}


// Clase principal.
public class Main {


    // Este método busca la mascota de mayor edad.
    public static Pet findOldestPet(Pet[] pets) {

        // Inicialmente suponemos que la primera mascota
        // es la de mayor edad.
        Pet oldestPet = pets[0];


        // Recorremos todas las mascotas.
        for (Pet pet : pets) {

            // Si encontramos una mascota con mayor edad,
            // actualizamos oldestPet.
            if (pet.getAge() > oldestPet.getAge()) {
                oldestPet = pet;
            }
        }


        // Devolvemos la mascota encontrada.
        return oldestPet;
    }


    public static void main(String[] args) {


        // Array de objetos.
        // Cada posición contiene un objeto Pet.
        Pet[] pets = {

                new Pet("Luna", 3, "Perro"),
                new Pet("Michi", 2, "Gato"),
                new Pet("Rocky", 5, "Perro"),
                new Pet("Nala", 1, "Gato")

        };


        // Mostramos todas las mascotas.
        System.out.println("=== MIS MASCOTAS ===");


        // Recorremos el array utilizando for-each.
        for (Pet pet : pets) {
            pet.showInfo();
        }


        // Mostramos cuántas mascotas existen.
        System.out.println();

        System.out.println(
                "Cantidad de mascotas registradas: " + pets.length
        );


        // Buscamos la mascota de mayor edad.
        Pet oldestPet = findOldestPet(pets);


        // Mostramos el resultado.
        System.out.println();

        System.out.println(
                "La mascota de mayor edad es: "
                        + oldestPet.getName()
                        + " con "
                        + oldestPet.getAge()
                        + " años."
        );


        // ==================================================
        // EJEMPLO DE DEPURACIÓN
        // ==================================================
        //
        // El arreglo tiene cuatro elementos.
        // Sus posiciones válidas son:
        //
        // pets[0]
        // pets[1]
        // pets[2]
        // pets[3]
        //
        // La siguiente instrucción produciría:
        // ArrayIndexOutOfBoundsException
        //
        // porque la posición 10 no existe.
        //
        // System.out.println(pets[10].getName());


        System.out.println();

        System.out.println("=== PROGRAMA FINALIZADO ===");
    }
}