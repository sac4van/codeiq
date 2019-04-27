import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {

    // input
    static int n;
    static int[] c;
    static int[] v;

    /**
     * input
     */
    static void input(){
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        v = new int[n];
        c = new int[n];
        for (int i=0;i<n;i++){
            v[i] = sc.nextInt();
        }
        for (int i=0;i<n;i++){
            c[i] = sc.nextInt();
        }
        sc.close();
    }
 
    /**
     * solver
     */
    static void solve(){
        int ans = 0;
        for(int i=0;i<n;i++){
            int s = v[i] - c[i];
            if (s > 0) {
                ans += s;
            }
        }
        System.out.println(ans);
    }

    public static void main(String args[]) {

        input();

        solve();
    }
}
