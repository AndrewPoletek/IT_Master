package exercise;
public class DslModem extends exercise.Modem {
    String method = "łącze telefoniczne DSL";
    public void connect(){
        System.out.println('Łączę z internetem...');
        System.out.println("Za pomocą: "+this.method);
    }
}
