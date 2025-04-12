import java.util.HashSet;
import java.util.Set;

class Universidad {
    private String nombre;
    private String[] carreras;
    private int cantidadEstudiantes;

    public Universidad(String nombre, String[] carreras, int cantidadEstudiantes) {
        this.nombre = nombre;
        this.carreras = carreras;
        this.cantidadEstudiantes = cantidadEstudiantes;
    }

    public String getNombre() {
        return nombre;
    }

    public String[] getCarreras() {
        return carreras;
    }

    public int getCantidadEstudiantes() {
        return cantidadEstudiantes;
    }
}

public class Main {
    public static void main(String[] args) {
        // Crear universidades
        Universidad u1 = new Universidad("UMSA", new String[]{"Informática", "Matemáticas", "Física"}, 5000);
        Universidad u2 = new Universidad("UCB", new String[]{"Informática", "Derecho", "Administración", "Arquitectura"}, 3000);
        Universidad u3 = new Universidad("UPB", new String[]{"Electrónica", "Administración", "Informática"}, 2500);

        // a) Universidad con más carreras
        Universidad[] universidades = {u1, u2, u3};
        Universidad mayor = u1;
        for (Universidad u : universidades) {
            if (u.getCarreras().length > mayor.getCarreras().length) {
                mayor = u;
            }
        }
        System.out.println("Universidad con más carreras: " + mayor.getNombre());

        // b) Carreras en común entre UMSA y UCB
        System.out.println("Carreras en común entre " + u1.getNombre() + " y " + u2.getNombre() + ":");
        Set<String> comunes = new HashSet<>();
        for (String carrera1 : u1.getCarreras()) {
            for (String carrera2 : u2.getCarreras()) {
                if (carrera1.equals(carrera2)) {
                    comunes.add(carrera1);
                }
            }
        }
        for (String carrera : comunes) {
            System.out.println("- " + carrera);
        }

        // c) Total de estudiantes
        int total = 0;
        for (Universidad u : universidades) {
            total += u.getCantidadEstudiantes();
        }
        System.out.println("Total de estudiantes: " + total);
    }
}
