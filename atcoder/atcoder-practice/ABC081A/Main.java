import java.util.Scanner;
public class Main {
	public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        // 入力
        String s = sc.next();

        // 計算
        int ans = solve(s);

        // 出力
		System.out.println(ans);
    }
    
    public static int solve(String s) {
        char[] cList = s.toCharArray();
        int ans = 0;
        for ( char c : cList){
            if ( '1' == c ) {
                ans ++;
            }
        }
        return ans;
    };
}