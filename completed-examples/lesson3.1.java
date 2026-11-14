import java.util.Scanner; // 1. Importamos la herramienta de lectura

public class Main {
    public static void main(String[] args) {
        // 2. Creamos el "Scanner" para leer el teclado
        Scanner microfono = new Scanner(System.in);

        System.out.println("¡Hola! ¿Cómo te llamas?");
        // 3. Leemos un texto (String) escrito por el usuario
        String nombre = microfono.nextLine();

        System.out.println("¿Cuántos años tienes?");
        // 4. Leemos un número entero (int)
        int edad = microfono.nextInt();

        // 5. Mostramos el resultado usando los datos que nos dio
        System.out.println("Genial, " + nombre + ". Tienes " + edad + " años. ¡Bienvenido al mundo de la programación!");
    }
}