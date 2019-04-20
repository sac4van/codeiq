import java.util.Scanner;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		// 整数の入力
		int a = sc.nextInt();
		// スペース区切りの整数の入力
		int b = sc.nextInt();
        
        String ans;

        if ( a % 2 == 0 || b % 2 == 0) {
            // a b いずれかが偶数
            ans = "Even";
        } else {
            // a b いずれも奇数
            ans = "Odd";
        }
        // 出力
		System.out.println(ans);
	}
}