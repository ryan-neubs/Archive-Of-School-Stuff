

import java.util.Scanner;

public class switchPractice {
	
	public static void main(String[] args) {
		System.out.println("This program tells you how many days have passed this week");
		String day = "notDay";
		Scanner scan = new Scanner(System.in);
		while (day != "stop") {
		switch(day) {	//a switch that hinges on the char day
			default:
				System.out.println("Please enter the day of the week(Ex. Monday). Enter stop to end this program. ");
				break;	//leave the switch
			case "Monday":
				System.out.println("1 day has passed this week. Enter stop to end this program. ");
				break;	//leave the switch
			case "Tuesday":
				System.out.println("2 days have passed this week. Enter stop to end this program.");
				break;	//leave the switch
			case "Wednesday":
				System.out.println("3 days have passed this week. Enter stop to end this program.");
				break;	//leave the switch
			case "Thursday":
				System.out.println("4 days have passed this week. Enter stop to end this program.");
				break;	//leave the switch
			case "Friday":
				System.out.println("5 days have passed this week. Enter stop to end this program.");
				break;	//leave the switch
			case "Saturday":
				System.out.println("6 days have passed this week. Enter stop to end this program.");
				break;	//leave the switch
			case "Sunday":
				System.out.println("You are on the first day of the week. Enter stop to end this program.");
				break;	//leave the switch
			case "stop":
				break;	//leave the switch and the while loop
		}
		day = scan.nextLine();
		}
		scan.close();
	}
}
