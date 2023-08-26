public class GSTest {
  public static void main(String[] args) {
    Museo entrada = new Museo();
    new Visitante("Visitante1", entrada);
    new Visitante("Visitante2", entrada);
    new Visitante("Visitante3", entrada);
    new Visitante("Visitante4", entrada);
    new Visitante("Visitante5", entrada);
    new Visitante("Visitante6", entrada);
  }

} class Museo {
  //Assume 4 parking slots for simplicity
  public static final int MAX_CAPACITY = 3;
  private int capacidad = 0;

  public synchronized void entrar(String visitante) {
    while (capacidad >= MAX_CAPACITY) {
      try {
        System.out.println(" El museo esta lleno " +
                           visitante + " tiene que esperar ");
        wait();
      } catch (InterruptedException e) {
        //
      }
    }
    //precondition is true
    System.out.println(visitante + " entro");
    capacidad = capacidad + 1;
  }
  public synchronized void leave(String visitante) {
    capacidad = capacidad - 1;
    System.out.println(visitante +
                       " se ha ido, notificar a un vistitante esperando");
    notify();
  }
}

class Visitante extends Thread {
  private Museo museo;
  private String name;

  Visitante(String n, Museo p) {
    name = n;
    museo = p;
    start();
  }
  public void run() {
    System.out.println(name + " esta listo para entrar");
    museo.entrar(name);
    try {
      sleep(15000);
    } catch (InterruptedException e) {
      //
    }
    //leave after 15000ms
    museo.leave(name);
  }
}
