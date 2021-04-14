public class Grade {
    public static void main(String[] arguments){
        int grade = 50;
        if(grade >90){
            System.out.println("Gratulacje Twoja ocena to A");
        }else if(grade>70){
            System.out.println("Gratulacje Twoja ocena to B");
        }else if(grade>=50){
            System.out.println("Twoja ocena to C");
        }else{
            System.out.println("Twoja ocena to D");
        }
    }
}
