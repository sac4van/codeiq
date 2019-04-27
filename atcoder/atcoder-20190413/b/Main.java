import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {

    // input
    static int n;
    static int[] h;

    /**
     * input
     */
    static void input(){
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        h = new int[n];
        for (int i=0;i<n;i++){
            h[i] = sc.nextInt();
        }
        sc.close();
    }
 
    /**
     * solver
     */
    static void solve(){
        int ans = 0;
        int maxHeight = 0;
        for(int i=0;i<n;i++){
            if (h[i]>=maxHeight) {
                maxHeight = h[i];
                ans++;
            }
        }
        System.out.println(ans);
    }

    public static void main(String args[]) {

        input();

        solve();
    }
}
