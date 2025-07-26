package DSA_Leetcode.Basic_Programs;

import java.util.Scanner;

public class Negetive_Palindrome{
    public static int negetive_palindrome(int num){
        int num_copy = num;
        int rev = 0;
        int num_abs = Math.abs(num);

        while(num_abs > 0){
            int rem = num % 10;
            rev = (rev*10) + rem;
            num_abs = (int)num/10;
        }
        int limit = (int) Math.pow(2, 31);

        if(limit < (int) Math.pow(2, 31) || limit > (int) Math.pow(2, 31)){
            return 0;
        }

        if(num_copy < 0){
            return -rev;
        }else{
            return rev;
        }
        
    }
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Enter A Value to test : ");
            int num_value = sc.nextInt();
            try {
                int status = negetive_palindrome(num_value);
                System.out.println(status);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

}