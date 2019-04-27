import java.util.Arrays;
import java.util.*;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.math.BigInteger;

public class Main {

    // input
    static int n;
    static List<Long> a;

    /**
     * input
     */
    static void input(){
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        a = new ArrayList<Long>();
        for (int i=0;i<n;i++){
            a.add((Long)(sc.nextLong()));
        }
        sc.close();
    }
 
    /**
     * solver
     */
    static void solve(){

        Long ans = new Long(0);

        int countZero = 0;
        int countNegative = 0;

        for (Long l: a) {
            if (l == 0) {
                countZero ++;
            } else if (l < 0) {
                countNegative ++;
            }
        }

        if (countZero > 0 || countNegative % 2 == 0) {
            for (Long l: a) {
                ans += Math.abs(l);
            }
        } else {
            Long tmp = Long.MAX_VALUE;
            for (Long l: a) {
                Long _l = Math.abs(l);
                ans += _l;
                tmp = (tmp < _l) ? tmp : _l;
            }
            ans -= 2 * tmp;
        }

        System.out.println(ans);

    }

    public static void main(String args[]) {

        input();
        solve();
    }
}
