import java.util.Scanner;
public class syracuse {
  public static void main(String[] args) {
    Scanner num = new Scanner(System.in);
    System.out.println("Enter any integer: ");
    int myNum = num.nextInt();
    while(myNum != 1){
      if (myNum % 2 == 0){
        myNum /= 2;
        System.out.println(myNum);
      } else if (myNum % 2 == 1){
        myNum = (myNum * 3) + 1;
        System.out.println(myNum);
      }
    }
  }
}