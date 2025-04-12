public class Coche {
    private String marca;
    private String modelo;
    private int velocidad;

    public Coche(String marca, String modelo) {
        this.marca = marca;
        this.modelo = modelo;
        this.velocidad = 0;
    }

    public void acelerar() {
        this.velocidad += 10;
    }

    public void frenar() {
        this.velocidad = Math.max(0, this.velocidad - 5);
    }

    public void mostrarVelocidad() {
        System.out.println(this.marca + " " + this.modelo + " - Velocidad: " + this.velocidad + " km/h");
    }

    public static void main(String[] args) {
        Coche c1 = new Coche("Toyota", "Corolla");
        Coche c2 = new Coche("Ford", "Fiesta");

        // Acelerar
        c1.acelerar();
        c1.acelerar();
        c2.acelerar();

        // Frenar
        c1.frenar();
        c2.frenar();
        c2.frenar();

        // Mostrar velocidad
        c1.mostrarVelocidad();
        c2.mostrarVelocidad();
    }
}
