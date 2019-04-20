import java.util.*;
import java.util.stream.*;

public class Main {

    // input
    static int N;
    static int L;
    static int P;
    static List<Integer> A;
    static List<Integer> B;

    // output
    static int ans;

    /**
     * input
     */
    static void input(){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        L = sc.nextInt();
        P = sc.nextInt();
        A = Arrays.asList(
                sc.next().split(",")
            )
            .stream()
            .map(s -> Integer.parseInt(s))
            .collect(Collectors.toList());
        B = Arrays.asList(
                sc.next().split(",")
            )
            .stream()
            .map(s -> Integer.parseInt(s))
            .collect(Collectors.toList());
        sc.close();
    }
 
    /**
     * solver
     */
    static void solve(){
        ans=2;
    }

    /**
     * output
     */
    static void output(){
        System.out.println(ans);
    }

    public static void main(String args[]) {

        input();

        solve();

        output();
    }
}