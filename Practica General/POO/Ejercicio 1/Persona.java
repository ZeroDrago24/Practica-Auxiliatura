public class Persona {
    private String nombre;
    private int edad;
    private String ciudad;

    public Persona(String nombre, int edad, String ciudad) {
        this.nombre = nombre;
        this.edad = edad;
        this.ciudad = ciudad;
    }

    public void saludar() {
        System.out.println("Hola, soy " + nombre + " de " + ciudad);
    }

    public boolean esMayorEdad() {
        return edad >= 18;
    }

    public static void main(String[] args) {
        Persona p1 = new Persona("Ana", 22, "La Paz");
        Persona p2 = new Persona("Luis", 17, "Cochabamba");
        Persona p3 = new Persona("Marta", 30, "Santa Cruz");

        Persona[] personas = {p1, p2, p3};

        for (Persona p : personas) {
            p.saludar();
            System.out.println("Mayor de edad: " + (p.esMayorEdad() ? "Sí" : "No"));
            System.out.println("---");
        }
    }
}
