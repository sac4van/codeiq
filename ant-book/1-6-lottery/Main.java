import java.util.*;
import java.util.stream.*;

public class Main {

    // input
    static int n;
    static int m;
    static List<Integer> k;

    /**
     * input
     */
    static void input(){
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        k = Arrays.asList(
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
        // create (k_1 + k_2) list
        HashSet<Integer> ksum = new HashSet<>();
        for (int k1 : k) {
            for (int k2 : k){
                ksum.add(k1+k2);
            }
        }

        for (int a: ksum){
            if (ksum.contains(m-a)) {
                System.out.println("Yes.");
                return;
            }
        }

        System.out.println("No.");
    }

    public static void main(String args[]) {

        input();

        long start = System.currentTimeMillis();
        solve();
        long end = System.currentTimeMillis();

        System.out.println("n: " + n + " msec: " + (end-start));
    }
}
