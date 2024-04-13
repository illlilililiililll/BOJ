import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        String word = sc.next();

        for (int i = 0; i < word.length(); i++) {
            char letter = word.charAt(i);
            if (letter > 90)
                sb.append(letter - 32);
            else
                sb.append(letter + 32);
        }

        System.out.println(sb);
    }
}