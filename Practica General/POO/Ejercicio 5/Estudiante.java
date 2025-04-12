public class Estudiante {
    private String nombre;
    private double nota1;
    private double nota2;

    public Estudiante(String nombre, double nota1, double nota2) {
        this.nombre = nombre;
        this.nota1 = nota1;
        this.nota2 = nota2;
    }

    public double calcularPromedio() {
        return (nota1 + nota2) / 2;
    }

    public boolean verificarAprobado() {
        return calcularPromedio() >= 6;
    }

    public void mostrarInfo() {
        double promedio = calcularPromedio();
        String estado = verificarAprobado() ? "Aprobado" : "Reprobado";
        System.out.printf("%s - Promedio: %.2f - %s%n", nombre, promedio, estado);
    }

    public static void main(String[] args) {
        Estudiante e1 = new Estudiante("Lucía", 8, 7);
        Estudiante e2 = new Estudiante("Carlos", 5, 6);
        Estudiante e3 = new Estudiante("Ana", 4, 5);

        System.out.println("=== Información de Estudiantes ===");
        Estudiante[] estudiantes = {e1, e2, e3};

        for (Estudiante e : estudiantes) {
            e.mostrarInfo();
        }
    }
}
