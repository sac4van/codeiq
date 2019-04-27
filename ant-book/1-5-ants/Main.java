import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {

    // input
    static int N;
    static int L;
    static List<Integer> X;

    /**
     * input
     */
    static void input(){
        Scanner sc = new Scanner(System.in);
        L = sc.nextInt();
        N = sc.nextInt();
        X = Arrays.asList(
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
        int maxTime = 0;
        int minTime = 0;

        for (int x : X) {
            int _maxTime = Math.max(x, L-x);
            int _minTime = Math.min(x, L-x);
            maxTime = Math.max(maxTime, _maxTime);
            minTime = Math.max(minTime, _minTime); 
        }

        System.out.println("max: " + maxTime);
        System.out.println("min: " + minTime);
    }

    public static void main(String args[]) {

        input();

        solve();
    }
}
