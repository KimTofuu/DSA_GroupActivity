import java.util.Scanner;

public class palindrome{
    static boolean toCheck(String input){
        StringBuilder sb = new StringBuilder(input);
        String rev = sb.reverse().toString();
        if(input.equals(rev)){
            return true;
        }else{
            return false;
        }
    }
public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter string: ");
        String input = scanner.nextLine();
        
        System.out.println(toCheck(input));

        scanner.close();
    }
}