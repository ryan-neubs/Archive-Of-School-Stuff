
import java.util.Scanner;	//import the scanner class

public class ifElsePractice {

	public static void main() {
		Scanner scan = new Scanner(System.in);	//create scanner object 
		System.out.print("Enter the first number: ");
		int num1 = scan.nextInt();	//use scanner to take the input for the next int that is input
		System.out.print("Enter the second number: ");
		int num2 = scan.nextInt(); scan.close();	//close the scanner object
		if(num2 > num1) System.out.print("The numbers add to: " + (num1 + num2));	//compare the values of 2 varibles for an if statement
		else System.out.print("The difference is: " + (num1 - num2));
	}
}
