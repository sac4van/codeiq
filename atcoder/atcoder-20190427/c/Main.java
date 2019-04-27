import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.math.BigInteger;

public class Main {

    // input
    static int n;
    static BigInteger[] a;

    /**
     * input
     */
    static void input(){
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        a = new BigInteger[n];
        for (int i=0;i<n;i++){
            a[i] = BigInteger.valueOf(sc.nextInt());
        }
        sc.close();
    }
 
    /**
     * solver
     */
    static void solve(){
        BigInteger[] f = new BigInteger[n];
        BigInteger[] g = new BigInteger[n];

        f[0] = a[0];
        g[n-1] = a[n-1];

        for(int i=1;i<n;i++){
            f[i] = f[i-1].gcd(a[i]);
            g[n-i-1] = g[n-i].gcd(a[n-i-1]);
        }

        BigInteger ans = BigInteger.ZERO;

        // 0<i<n-1
        for (int i=0;i<n;i++) {
            BigInteger tmp;

            if (i==0){
                tmp = g[1];
            } else if (i==n-1) {
                tmp = f[n-2];
            } else {
                tmp = f[i-1].gcd(g[i+1]);
            }

            if (tmp.compareTo(ans) >= 0) {
                ans = tmp;
            }
        }

        System.out.println(ans);

    }

    public static void main(String args[]) {

        input();
        solve();
    }
}
