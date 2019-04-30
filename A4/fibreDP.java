import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class fibreDP {
	static BigInteger maxSum(List<BigInteger> bigInts) {
		BigInteger maxProfit = new BigInteger("0");
		BigInteger tempProfit = new BigInteger("0");
		
        for (int i = 0; i < bigInts.size(); i++) {
            tempProfit = tempProfit.add(bigInts.get(i));
            if (tempProfit.compareTo(maxProfit) == 1) {
            	maxProfit = tempProfit; 
            }
            if (tempProfit.compareTo(BigInteger.ZERO) < 0) {
            	tempProfit = new BigInteger("0");
            }
        }
        return maxProfit;
	}
	
	public static void main(String args[]) throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int isNegative = 1;
		while (true) {
			String inputString = reader.readLine();
			List<String> myList = new ArrayList<String>(Arrays.asList(inputString.split(" ")));
			if (inputString.length() == 1 && myList.get(0).equals("1")) { break; }
			
			List<BigInteger> bigInts = new ArrayList<BigInteger>(100000);
			for (String i: myList) {
				if (isNegative == 1 && i.charAt(0) == '-') {
					continue;
				}
				isNegative = 0;
				bigInts.add(new BigInteger(i));
			}
			System.out.println(maxSum(bigInts));
		}
	}
}