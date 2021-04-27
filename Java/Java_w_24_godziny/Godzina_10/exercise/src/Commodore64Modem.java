//1. Utwórz klasę Commodore64Modem z prędkością 300 oraz własną metodą connect
package excerise;

public class Commodore64Modem extends exercise.Modem {
    String method = "łącze commodore modem";
    public void connect(){
        System.out.println("Łączę z internetem ...");
        System.out.println("Za pomocą: "+this.method);
    }
}
