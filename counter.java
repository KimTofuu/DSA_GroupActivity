import java.util.Scanner;

public class counter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter string: ");
        String input = scanner.nextLine();
        input = input.toLowerCase();

        int vowNum = 0, conNum = 0;
        String vowels = "aeiou";

        for(int i = 0; i < input.length(); i++){
            char ch = input.charAt(i);
            if(vowels.indexOf(ch) != -1){
                vowNum++;
            }else{
                conNum++;
            }
        }

        System.out.println(input + ": vowels = " + vowNum + ", consonants = " + conNum);

        scanner.close();
    }
}
