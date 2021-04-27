package exercise;

public class CableModem extends exercise.Modem {
    String method = "łącze kablowe";
    public void connect(){
        System.out.println("Łącze z internetem...");
        System.out.println("Za  pomocą: "+this.method);
    }
}
