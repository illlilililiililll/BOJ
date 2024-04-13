import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        
        int[] num = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < n; i++) 
            num[i] = Integer.parseInt(st.nextToken());
        
        int x = Integer.parseInt(br.readLine());

        int count = 0;
        for (int i : num)
            if (i == x)
                count += 1;
        
        System.out.println(count);
    }
}
