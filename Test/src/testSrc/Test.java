package testSrc;
import java.util.Scanner;
import java.util.Random;

public class Test extends Test2 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String uin="";
		while(!uin.equals("quit")) {
			System.out.print("What is your name: ");
			uin = in.nextLine();
			System.out.println("Hello, "+uin+"!");
			System.out.print("How is your day? ")
		}
	}

}
