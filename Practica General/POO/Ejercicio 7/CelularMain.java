import java.util.ArrayList;

class Aplicacion {
    String nombre;
    int tamanoMB;

    public Aplicacion(String nombre, int tamanoMB) {
        this.nombre = nombre;
        this.tamanoMB = tamanoMB;
    }
}

class Celular {
    ArrayList<Aplicacion> aplicaciones;
    int espacioDisponible;
    double bateria;

    public Celular() {
        aplicaciones = new ArrayList<>();
        espacioDisponible = 1024;
        bateria = 100.0;
    }

    public void instalarAplicacion(Aplicacion app) {
        if (aplicaciones.size() >= 20) {
            System.out.println("No se pueden instalar más de 20 aplicaciones.");
        } else if (espacioDisponible >= app.tamanoMB) {
            aplicaciones.add(app);
            espacioDisponible -= app.tamanoMB;
            System.out.println("Aplicación '" + app.nombre + "' instalada.");
        } else {
            System.out.println("No hay suficiente espacio.");
        }
    }

    public void usarAplicacion(String nombre, int minutos) {
        if (bateria <= 0) {
            System.out.println("Celular apagado");
            return;
        }

        for (Aplicacion app : aplicaciones) {
            if (app.nombre.equals(nombre)) {
                int consumo;
                if (app.tamanoMB > 250) {
                    consumo = 5;
                } else if (app.tamanoMB > 100) {
                    consumo = 2;
                } else {
                    consumo = 1;
                }

                double gasto = (minutos / 10) * consumo;

                if (bateria - gasto <= 0) {
                    bateria = 0;
                    System.out.println("Batería agotada. Celular apagado");
                } else {
                    bateria -= gasto;
                    System.out.printf("Usando %s por %d minutos. Batería restante: %.2f%%\n", nombre, minutos, bateria);
                }
                return;
            }
        }

        System.out.println("Aplicación no encontrada.");
    }

    public void mostrarBateria() {
        System.out.printf("Batería: %.2f%%\n", bateria);
    }

    public static void main(String[] args) {
        Celular cel = new Celular();
        Aplicacion app1 = new Aplicacion("WhatsApp", 120);
        Aplicacion app2 = new Aplicacion("YouTube", 300);
        Aplicacion app3 = new Aplicacion("Notas", 80);

        cel.instalarAplicacion(app1);
        cel.instalarAplicacion(app2);
        cel.instalarAplicacion(app3);

        cel.usarAplicacion("YouTube", 30);
        cel.usarAplicacion("Notas", 20);
        cel.mostrarBateria();
    }
}
