import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {

    // input
    static int a;
    static int b;
    static int t;

    /**
     * input
     */
    static void input(){
        Scanner sc = new Scanner(System.in);
        a = sc.nextInt();
        b = sc.nextInt();
        t = sc.nextInt();
        sc.close();
    }
 
    /**
     * solver
     */
    static void solve(){
        int ans;

        if (a <= 0) {
            ans = 0;
        } else {
            ans = (int)(Math.floor(t/a)) * b;
        }
        
        System.out.println(ans);
    }

    public static void main(String args[]) {

        input();

        solve();
    }
}
