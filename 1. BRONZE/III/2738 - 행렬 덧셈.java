import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer line = new StringTokenizer(br.readLine(), " ");

        int n = Integer.parseInt(line.nextToken());
        int m = Integer.parseInt(line.nextToken());

        int[][] a = new int[n][m];

        for (int i = 0; i < n; i++){
            line = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++)
                a[i][j] = Integer.parseInt(line.nextToken());
        }

        for (int i = 0; i < n; i++){
            line = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++)
                bw.write(a[i][j] + Integer.parseInt(line.nextToken()) + " ");

            bw.write("\n");
        }
        bw.flush();
    }
}
