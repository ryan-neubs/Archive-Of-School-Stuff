
import java.util.Scanner;

public class fibonacci { //Calculates the numbers in the fibonacci sequence up to a desired number
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.print("Up to: ");	//ask for and record the desired number
		int n = scan.nextInt();
		scan.close();
		int num1 = 0; int num2 = 1; int sum = 0;	//Declare variables
		while(num1 <= n) {		//until the desired number is reached perform the math for fibonacci
			System.out.print(num1 + ", ");
			sum = num1 + num2;
			num1 = num2;
			num2 = sum;
		}
	}
}
