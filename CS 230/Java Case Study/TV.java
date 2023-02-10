// TV.java
// by Ryan Neubauer
import java.util.Scanner;
import java.lang.System;
public class TV{
    int channel;
    boolean power;
    int volume;
    TV(){
        this.channel = 1;
        this.power = false;
        this.volume = 0;
    }
    public void change_channel(int newchannel){
        if(check_power()){
            this.channel = newchannel;
            System.out.println("\nChannel is now: " + this.channel);
        } 
    }
    public void volume_up(){
        if(check_power()){
            this.volume += 1;
            System.out.println("\nVolume is now: " + this.volume);
        }
    }
    public void volume_down(){
        if(check_power()){
            if(volume - 1 < 0){
                this.volume = 0;
                System.out.println("\nVolume is now: " + this.volume);
            } else{
                this.volume -= 1;
                System.out.println("\nVolume is now: " + this.volume);
            }
        }
        if(volume - 1 < 0){
            this.volume = 0;
        }
    }
    public void power_on(){
        this.power = true;
        System.out.println("\nTV is now on");
    }
    public void power_off(){
        this.power = false;
        System.out.println("\nTV is now off");
    }
    public boolean check_power(){
        if(this.power == false){
            System.out.print("\nTV power is off.\n");
            return false;
        }
        System.out.println("\nTV power is on.");
        return true;
    }
    public static void main(String[] args){
        TV TV1 = new TV();
        String option = null;
        Scanner sc = new Scanner(System.in);
        while(true){
            System.out.println("\nEnter a command:");
            option = sc.nextLine();
            switch(option){
                case "power on":
                    TV1.power_on();
                    break;
                case "power off":
                    TV1.power_off();
                    break;
                case "change channel":
                    System.out.print("What channel? ");
                    int channel = sc.nextInt();
                    TV1.change_channel(channel);
                    break;
                case "volume up":
                    TV1.volume_up();
                    break;
                case "volume down":
                    TV1.volume_down();
                    break;
                case "check power":
                    TV1.check_power();
                    break;
                case "quit":
                    sc.close();
                    System.exit(0);
                    break;
            }
        }
    }
}