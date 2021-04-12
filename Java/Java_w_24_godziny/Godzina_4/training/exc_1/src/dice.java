package com.java24hours;
import java.util.*;

public class dice {
    public static void main(String[] arguments){
        Random generator = new Random();
        int digit = generator.nextInt();
        System.out.println(digit);
    }
}
