//2. Dodaj metodę disconnect() do jednej z klas w projekcie Modem i zastanów się gdzie ją umieścić aby obsługiwała odłączenie modemu kablowego, DSL i Commodore64
package exercise;

public class Modem {
    int speed;
    public void displaySpeed(){
        System.out.println("Prędkość modemu to: "+this.speed);
    }
    public void disconnect(){
        System.out.println("Rozłączanie internetu...");
    }
}
