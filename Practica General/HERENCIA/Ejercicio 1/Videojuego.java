

public class Videojuego {

    // Atributos
    private String nombre;
    private String plataforma;
    private int cantidadJugadores;

    // Constructor 1: Inicializa nombre, plataforma y cantidadJugadores
    public Videojuego(String nombre, String plataforma, int cantidadJugadores) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadJugadores = cantidadJugadores;
    }

    // Constructor 2: Inicializa nombre, plataforma y asigna 1 jugador por defecto
    public Videojuego(String nombre, String plataforma) {
        this(nombre, plataforma, 1); // Llama al constructor principal con cantidadJugadores = 1
    }

    // Método para mostrar los detalles del videojuego
    public void mostrar() {
        System.out.println("Nombre: " + this.nombre);
        System.out.println("Plataforma: " + this.plataforma);
        System.out.println("Cantidad de Jugadores: " + this.cantidadJugadores);
    }

    // Método para agregar jugadores
    // Si no se pasa un argumento, agrega 1 jugador
    public void agregarJugadores() {
        this.cantidadJugadores += 1;
    }

    // Sobrecarga del método agregarJugadores para agregar una cantidad de jugadores
    public void agregarJugadores(int jugadores) {
        this.cantidadJugadores += jugadores;
    }

    // Método main para ejecutar el código
    public static void main(String[] args) {
        // a) Instanciar dos videojuegos
        // Usando el constructor normal (con 3 parámetros)
        Videojuego videojuego1 = new Videojuego("Zelda", "Switch", 2);

        // Usando el constructor sobrecargado (con 2 parámetros)
        Videojuego videojuego2 = new Videojuego("Minecraft", "PC");

        // c) Mostrar los videojuegos
        videojuego1.mostrar();
        videojuego2.mostrar();

        // d) Sobrecargar el método agregarJugadores
        // Agregar 1 jugador a videojuego1 (por defecto)
        videojuego1.agregarJugadores();
        videojuego1.mostrar();

        // Agregar 3 jugadores a videojuego2
        videojuego2.agregarJugadores(3);
        videojuego2.mostrar();
    }
}
