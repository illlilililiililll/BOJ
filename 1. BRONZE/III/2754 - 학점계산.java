import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String score = sc.next();
        double total = 0;

        switch (score.charAt(0)) {
            case 'A':
                total += 4;
                break;
            case 'B':
                total += 3;
                break;
            case 'C':
                total += 2;
                break;
            case 'D':
                total += 1;
                break;
            default:
                System.out.println(0.0);
                return;
        }

        switch (score.charAt(1)) {
            case '+':
                total += 0.3;
                break;
            case '-':
                total -= 0.3;
                break;
        }

        System.out.println(total);
    }
}