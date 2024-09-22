import java.util.Scanner;

public class storyTelling {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.print("Enter your age: ");
        int age = scanner.nextInt();        
        scanner.nextLine();
        System.out.print("Enter an animal: ");
        String pet = scanner.nextLine();
        System.out.print("How many years of experience do you have in programming? ");
        int progYears = scanner.nextInt();
        scanner.nextLine();
        System.out.print("Are you good at it? y/n ");
        char inp = scanner.nextLine().charAt(0);

        boolean isGood;
        if(inp == 'y' || inp == 'Y'){
            isGood = true;
        }else{
            isGood = false;
        }

        System.out.println("\nThis is your made up Story!\n");
        System.out.println("Hi! I am " + name + " and I am thrilled to tell you my programming story.");
        System.out.println("I started when I was " + (age - progYears) + " which sums my experience to " + progYears + " years.");
        System.out.println("It has been a very challenging part of my life, but thankfully I have my pet " + pet + " to keep me going.");

        if(isGood){
            System.out.println("After all those years of hard work, I can proudly say that I have mastered programming!");
            System.out.println("Now, I often take on advanced projects, and people seek me out for advice on complex problems.");
            System.out.println("My pet " + pet + " always sits by my side while I code, providing me company during those late-night coding sessions.");
            System.out.println("Together, we have completed numerous projects. In fact, I even created a cool app for " + pet + "!");
            System.out.println("Whenever I need a break, I go for a walk with " + pet + ", recharging myself for more creative ideas.");
            System.out.println("Looking ahead, I plan to share my knowledge by mentoring others and building something groundbreaking!");
        }else{
            System.out.println("Even though I have been at it for " + progYears + " years, I still find myself learning new things every day.");
            System.out.println("Programming is a journey, and I am proud of how far I have come. My pet " + pet + " always reminds me to take breaks when things get tough.");
            System.out.println("With " + pet + " by my side, I keep pushing through challenges, staying determined to improve.");
            System.out.println("One day, I know I will be able to build the most amazing apps and systems.");
            System.out.println("For now, I am taking it one step at a time and loving every moment of the journey.");
            System.out.println("And who knows, maybe " + pet + " will inspire my next big project!");
        }


        scanner.close();
    }
}
