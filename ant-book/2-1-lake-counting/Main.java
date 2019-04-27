import java.util.*;
import java.util.stream.*;

public class Main {

    // input
    static int n;
    static int m;
    static char[][] f;

    /**
     * input
     */
    static void input(){
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        f = new char[n][m];

        for(int i=0;i<n;i++){
            String s = sc.next();
            for(int j=0;j<m;j++){
                f[i][j] = s.charAt(j);
            }
        }
        sc.close();
    }
 
    /**
     * solver
     */
    static void solve(){
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                System.out.print(f[i][j]);
            }
            System.out.println();
        }

    }

    public static void main(String args[]) {

        input();

        long start = System.currentTimeMillis();
        solve();
        long end = System.currentTimeMillis();

        System.out.println("n: " + n + " msec: " + (end-start));
    }
}
