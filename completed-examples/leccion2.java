public class Main {

    // METODOS DEFINIDOS PARA EL BLOQUE 4
    public static void saludarJugador(String nombreJugador) {
        System.out.println("-----------------------------------");
        System.out.println("Hola, " + nombreJugador + "! Listo para la mision.");
    }

    public static int calcularPuntajeTotal(int puntosMision, int puntosExtra) {
        int resultado = puntosMision + puntosExtra;
        return resultado;
    }

    public static void main(String[] args) {
        System.out.println("=== LECCION 2: ESTRUCTURAS DE CONTROL Y METODOS ===");

        // === BLOQUE 1: CONDICIONAL IF - ELSE ===
        
        System.out.println("\n--- 1. Decisiones con if - else ---");
        int monedas = 120;
        int precioEspada = 100;

        if (monedas >= precioEspada) {
            System.out.println("Caso 1: Compra exitosa! Te alcanza para la espada.");
            monedas = monedas - precioEspada;
            System.out.println("Monedas restantes: " + monedas);
        } else {
            System.out.println("Caso 1: No tienes suficientes monedas.");
        }

        int precioArmadura = 80;
        if (monedas >= precioArmadura) {
            System.out.println("Caso 2: Compra exitosa! Te alcanza para la armadura.");
        } else {
            System.out.println("Caso 2: No te alcanza para la armadura, solo tienes " + monedas + " monedas.");
        }
        

        // === BLOQUE 2: MULTIPLES CONDICIONES (ELSE IF) ===

        System.out.println("\n--- 2. Rangos con else if ---");
        int nivel = 15;

        if (nivel >= 20) {
            System.out.println("Rango actual: Maestro");
        } else if (nivel >= 10) {
            System.out.println("Rango actual: Avanzado");
        } else {
            System.out.println("Rango actual: Principiante");
        }


        // === BLOQUE 3: BUCLES FOR Y WHILE ===

        System.out.println("\n--- 3. Repeticiones con bucle for ---");
        for (int mision = 1; mision <= 3; mision++) {
            System.out.println("Completando mision diaria numero: " + mision);
        }

        System.out.println("\n--- 4. Repeticiones con bucle while ---");
        int energia = 3;
        while (energia > 0) {
            System.out.println("Entrenando personaje... Energia actual: " + energia);
            energia--;
        }
        System.out.println("Personaje sin energia, hora de descansar!");


        // === BLOQUE 4: LLAMADA A LOS METODOS ===

        System.out.println("\n--- 5. Usando nuestros metodos ---");
        saludarJugador("Alex");
        saludarJugador("Sofia");

        int puntajeFinal = calcularPuntajeTotal(250, 50);
        System.out.println("El puntaje total obtenido es: " + puntajeFinal);

    }
}