// Clase Cocinero
class Cocinero {
    private String nombre;
    private int sueldoMes;
    private int horasExtra;
    private float sueldoHora;
 
    public Cocinero(String nombre, int sueldoMes, int horasExtra, float sueldoHora) {
        this.nombre = nombre;
        this.sueldoMes = sueldoMes;
        this.horasExtra = horasExtra;
        this.sueldoHora = sueldoHora;
    }
 
    public float sueldoTotal() {
        return sueldoMes + (horasExtra * sueldoHora);
    }
 
    public int getSueldoMes() {
        return sueldoMes;
    }
 
    public void mostrarSueldoMesIgual(int sueldo) {
        if (sueldoMes == sueldo) {
            System.out.println("Empleado: " + nombre + " - SueldoMes: " + sueldoMes);
        }
    }
}
 
class Mesero {
    private String nombre;
    private int sueldoMes;
    private int horasExtra;
    private float sueldoHora;
    private float propina;

 
    public Mesero(String nombre, int sueldoMes, int horasExtra, float sueldoHora, float propina) {
        this.nombre = nombre;
        this.sueldoMes = sueldoMes;
        this.horasExtra = horasExtra;
        this.sueldoHora = sueldoHora;
        this.propina = propina;
    }
 
    public float sueldoTotal() {
        return sueldoMes + (horasExtra * sueldoHora) + propina;
    }
 
    public int getSueldoMes() {
        return sueldoMes;
    }
 
    public void mostrarSueldoMesIgual(int sueldo) {
        if (sueldoMes == sueldo) {
            System.out.println("Empleado: " + nombre + " - SueldoMes: " + sueldoMes);
        }
    }
}
 
class Administrativo {
    private String nombre;
    private float sueldoMes;
    private String cargo;
 
    public Administrativo(String nombre, float sueldoMes, String cargo) {
        this.nombre = nombre;
        this.sueldoMes = sueldoMes;
        this.cargo = cargo;
    }
 
    public float sueldoTotal() {
        return sueldoMes;
    }
 
    public float getSueldoMes() {
        return sueldoMes;
    }
 
    public void mostrarSueldoMesIgual(float sueldo) {
        if (sueldoMes == sueldo) {
            System.out.println("Empleado: " + nombre + " - SueldoMes: " + sueldoMes + " - Cargo: " + cargo);
        }
    }
}

 
public class Restaurante {
    public static void main(String[] args) {
        // a) Instanciar 1 Cocinero, 2 Meseros y 2 Administrativos
        Cocinero cocinero = new Cocinero("Juan", 2000, 10, 15.50f);
        Mesero mesero1 = new Mesero("Pedro", 1500, 20, 10.0f, 100.0f);
        Mesero mesero2 = new Mesero("Ana", 1400, 15, 9.0f, 120.0f);
        Administrativo administrativo1 = new Administrativo("Carlos", 1800.0f, "Gerente");
        Administrativo administrativo2 = new Administrativo("Maria", 1800.0f, "Secretaria");

        // b) Sobrecargar el método SueldoTotal para mostrar el sueldo total
        System.out.println("Sueldo total del Cocinero: " + cocinero.sueldoTotal());
        System.out.println("Sueldo total de Mesero 1: " + mesero1.sueldoTotal());
        System.out.println("Sueldo total de Mesero 2: " + mesero2.sueldoTotal());
        System.out.println("Sueldo total Administrativo 1: " + administrativo1.sueldoTotal());
        System.out.println("Sueldo total Administrativo 2: " + administrativo2.sueldoTotal());

        // c) Sobrecargar el método para mostrar empleados con sueldoMes igual a un valor X
        System.out.println("\nEmpleados con SueldoMes igual a 1800:");
        cocinero.mostrarSueldoMesIgual(1800);
        mesero1.mostrarSueldoMesIgual(1800);
        mesero2.mostrarSueldoMesIgual(1800);
        administrativo1.mostrarSueldoMesIgual(1800);
        administrativo2.mostrarSueldoMesIgual(1800);
    }
}
