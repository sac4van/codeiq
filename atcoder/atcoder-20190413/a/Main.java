import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {

    // input
    static int a;
    static int b;

    /**
     * input
     */
    static void input(){
        Scanner sc = new Scanner(System.in);
        a = sc.nextInt();
        b = sc.nextInt();
        sc.close();
    }
 
    /**
     * solver
     */
    static void solve(){
        int ans;

        if (a>b){
            ans = 2*a-1;
        } else if (a==b) {
            ans = a + b;
        } else {
            ans = 2*b-1;
        }
        
        System.out.println(ans);
    }

    public static void main(String args[]) {

        input();

        solve();
    }
}
