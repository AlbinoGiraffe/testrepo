package textExcel;
import java.util.*;

public class CodeTesting {
	public static void main(String[] args) {
		String in = "";
		Scanner ui = new Scanner(System.in);
		while(!(in.equalsIgnoreCase("quit"))) {
			System.out.println("Input:");
			in = ui.nextLine();
			if(in.matches("[a-zA-Z]\\d+")){
				System.out.println("Good");
			} else {
				System.out.println("nope");
			}
		}
		ui.close();
	}
}
