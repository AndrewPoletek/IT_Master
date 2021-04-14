public class Benchmark {
    public static void main(String[] arguments){
        long startTime = System.currentTimeMillis();
        long endTime = startTime+60000;
        long counter=0;
        for(int i=5, j=10; i>0; i+=2, j+=3){
            int sum = i*j;
            if(System.currentTimeMillis() >= endTime){
                System.out.println(counter);
                counter=0;
                break;
            }
            counter++;
        }

    }
}
