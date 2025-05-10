import java.util.Scanner;

public class caleculatetaxwitholding {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter weekly income: $");
        double income = scanner.nextDouble();
        double taxRate;
        double taxes;

        if (income < 500) {
            taxRate = 0.10;
        } else if (income < 1500) {
            taxRate = 0.15;
        } else if (income < 2500) {
            taxRate = 0.20;
        } else {
            taxRate = 0.30;
        }

        taxes = income * taxRate;

        System.out.printf("Weekly average tax withholding: $%.2f\n", taxes);
        scanner.close();
    }
}