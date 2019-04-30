import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class fibreDC {
	public static BigInteger sumConc(List<BigInteger> bigInts, int l, int m, int h) {
		BigInteger sum = new BigInteger("0");
		BigInteger left_sum = new BigInteger("0");
		BigInteger right_sum = new BigInteger("0");
		for (int i = m; i >= l; i--) {
			sum = sum.add(bigInts.get(i));
			if (sum.compareTo(left_sum) == 1) {
				left_sum = sum; 
			}
		}
		
		sum = new BigInteger("0");
		for (int i = m + 1; i <= h; i++) { 
			sum = sum.add(bigInts.get(i));
			if (sum.compareTo(right_sum) == 1) {
				right_sum = sum;
			}
		}
		return left_sum.add(right_sum);
	}
	
	public static BigInteger divideConc(List<BigInteger> bigInts, int l, int h) {
		if (l == h) {
			return bigInts.get(l);
		}
	
		int m = (l + h) / 2;

		BigInteger left = divideConc(bigInts, l, m);
		BigInteger right = divideConc(bigInts, m + 1, h);
		BigInteger intersection = sumConc(bigInts, l, m, h);
		
		BigInteger maxProfit = left.max(right);
		maxProfit = maxProfit.max(intersection);
		return maxProfit;
	}
	
	public static void main(String args[]) throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
	
		while (true) {
			String inputString = reader.readLine();
			List<String> myList = new ArrayList<String>(Arrays.asList(inputString.split(" ")));
			if (inputString.length() == 1 && myList.get(0).equals("1")) { break; }
			
			List<BigInteger> bigInts = new ArrayList<BigInteger>(100000);
			for (String i: myList) {
				bigInts.add(new BigInteger(i));
			}
			System.out.println(divideConc(bigInts, 0 , bigInts.size() - 1));
		}
	}
}