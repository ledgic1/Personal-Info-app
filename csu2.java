import java.util.Scanner;

public class WeeklyTaxEstimator {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Input weekly earnings: $");
        double weeklyEarnings = input.nextDouble();
        double withholdingRate;
        double estimatedWithholding;

        // Determine applicable tax withholding rate
        if (weeklyEarnings < 500) {
            withholdingRate = 0.10;
        } else if (weeklyEarnings < 1500) {
            withholdingRate = 0.15;
        } else if (weeklyEarnings < 2500) {
            withholdingRate = 0.20;
        } else {
            withholdingRate = 0.30;
        }

        // Calculate estimated tax withheld
        estimatedWithholding = weeklyEarnings * withholdingRate;

        System.out.printf("Estimated weekly tax withholding: $%.2f%n", estimatedWithholding);
        input.close();
    }
}