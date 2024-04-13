import java.util.Scanner;
import java.io.OutputStreamWriter;
import java.io.BufferedWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++)
                bw.write("*");
            bw.write("\n");
        }
        bw.flush();
    }
}