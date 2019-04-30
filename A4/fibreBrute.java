import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.Arrays;

public class fibreBrute {
	
	public static BigInteger bruteForce(BigInteger[] bigints) {
		BigInteger maxProfit = new BigInteger("0");
		int index = 1;
		for (BigInteger i : bigints) {
			BigInteger sum = new BigInteger("0");
			if (i.compareTo(maxProfit) == 1) {
				maxProfit = i;
			}
			sum = sum.add(i);
				for (int j = index ; j < bigints.length ; j++) {
					sum = sum.add(bigints[j]);
					if (sum.compareTo(maxProfit) == 1) {
						maxProfit = sum;
					}
				}
			index++;
		}
		return maxProfit;
	}
	
	public static void main(String args[]) throws IOException{
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		
		while (true) {
			String[] inputString = reader.readLine().split(" ");
			if (inputString[0].equals("1") && inputString.length == 1) { break; }
			
			BigInteger[] inputBigInteger = Arrays.stream(inputString).map(BigInteger::new).toArray(BigInteger[]::new);
			System.out.println(bruteForce(inputBigInteger));
		}
	}
}
