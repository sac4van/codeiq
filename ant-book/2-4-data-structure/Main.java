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
        L = 
        sc.nextInt();
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
        A.add(L);
        B.add(0);
        N++;

        // gas station queue
        PriorityQueue<Integer> que = new PriorityQueue<Integer>();

        // # of supply
        ans = 0;

        // current position
        int pos = 0;

        // current fuel
        int tank = P;

        for (int i=0; i<N; i++){
            System.out.println("i:  " + i);
            // next distance
            int d = A.get(i) - pos;
            System.out.println(" pos: " + pos);
            System.out.println(" d: " + d);

            // supply sufficient fuel
            System.out.print(" tank: " + tank);
            while (tank - d < 0) {
                if (que.isEmpty()) {
                    System.out.println("-1");
                    return;
                }
                System.out.print(" -> " + que.peek());
                tank += que.poll();
                ans++;
            }
            System.out.println("");

            tank -= d;
            pos = A.get(i);
            que.offer(B.get(i));
        }

        System.out.println(ans);

    }

    public static void main(String args[]) {

        input();

        solve();
    }
}