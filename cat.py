import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String userInput = "";

        // Ask the user to enter "yes" to stop the loop
        while (!userInput.equals("yes")) {
            System.out.print("Enter 'yes' to stop the loop: ");
            userInput = scanner.nextLine(); // Read user input
        }

        System.out.println("You typed 'yes', exiting the loop!");

        scanner.close();
    }
}