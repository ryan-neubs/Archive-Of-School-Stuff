package tempConverter;

import java.util.Scanner;

public class tempConverting {

	public static void main(String[] args) {	//the main for the converter
		Scanner scan = new Scanner(System.in);
		tempConverter.tempUnitChecker checker = new tempConverter.tempUnitChecker();	//open an object for the tempUnitChecker in the same package
		System.out.println("This program converts tempurtures.");
		boolean valid = false; char tempUnit1 = 'p'; char tempUnit2 = 'p'; double temp = 0; double newTemp = 0; //declare variables
		while(valid == false) {		//get the value for the original temperature and check that it is valid
			System.out.print("Please choose the measuring system of your temperature (c, f, k): ");
			tempUnit1 = scan.next().charAt(0);	//scan for only one char
			valid = checker.checkTempUnit(tempUnit1);	//use one of the methods of the tempUnitChecker class
		}
		valid = false;
		while (valid == false) {	//get the value of which the temperature is to be converted
			System.out.print("Please enter the measuring system to convert to (c, f, k): ");
			tempUnit2 = scan.next().charAt(0);	//scan for only one char
			valid = checker.checkTempUnit(tempUnit2);	//use one of the methods of the tempUnitChecker class
		}
		System.out.print("Please enter the value for the temperature: ");	//get the number value for the temperature
		temp = scan.nextDouble(); scan.close();	//scan for the next double and then close the scanner
		newTemp = convertTemp(tempUnit1, tempUnit2, temp);
		System.out.print("The new temperature is " + newTemp + "\u00B0 " + tempUnit2);	//tell the user the new temperature
	}
	
	static double convertTemp(char tempUnit1, char tempUnit2, double temp) {	//convert the temperature
		switch(tempUnit1) {
		default:
			System.out.print("The temperature could not be converted");
			return 0.0;
		case 'c':	//convert the temperature from Celsius
			switch(tempUnit2) {
			default:
				System.out.print("The temperature could not be converted");
				return 0.0;
			case 'c':
				return (temp);
			case 'f':
				return ((temp * 9.0 / 5.0) + 32.0);
			case 'k':
				return (temp + 273.15);
			}
		case 'f':	//Convert the temperature from Fahrenheit
			switch(tempUnit2) {
			default:
				System.out.print("The temperature could not be converted");
				return 0.0;
			case 'c':
				return ((temp - 32.0) * 5.0 / 9.0);
			case 'f':
				return temp;
			case 'k':
				return ((temp - 32.0) * 5.0 / 9.0 + 273.15);
			}
		case 'k':	//covert the temperature from Kelvin
			switch(tempUnit2) {
				default:
					System.out.print("The temperature could not be converted");
					return 0.0;
				case 'c':
					return (temp - 273.15);
				case 'f':
					return ((temp-273.15) * 9.0 / 5.0 + 32.0);
				case 'k':
					return temp;
			}
		}
	}
}
