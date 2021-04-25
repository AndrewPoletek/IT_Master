/*
* Napisz program który przychowuje w tablicy pierwszych 400 liczb które są wielokrotnościami liczby 13
* */
public class FirstFourHundred {
    public static void main(String[] arguments){
        int[] numbers = new int[401];
        for(int i=0; i<numbers.length; i++){
            numbers[i] = i*13;
            System.out.println(String.valueOf(i)+"*"+String.valueOf(13)+"="+String.valueOf(numbers[i]));
        }
    }
}
