import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer line = new StringTokenizer(br.readLine(), " ");

        int n = Integer.parseInt(line.nextToken());
        int x = Integer.parseInt(line.nextToken());

        line = new StringTokenizer(br.readLine(), " ");
        int num;

        for (int i = 0; i < n; i++) {
            if ((num = (Integer.parseInt(line.nextToken()))) < x)
                sb.append(num + " ");
        }
        System.out.println(sb);
    }
}