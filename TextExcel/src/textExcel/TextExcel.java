package textExcel;

import java.io.FileNotFoundException;
import java.util.Scanner;

// Update this file with your own code.

public class TextExcel
{

	public static void main(String[] args)
	{
	    // Add your command loop here
		String in = "";
		Scanner uinput = new Scanner(System.in);
		Spreadsheet sheet1 = new Spreadsheet();
		
		while(!(in.equalsIgnoreCase("quit"))) {
			System.out.print("Command: ");
			in = uinput.nextLine();
			sheet1.processCommand(in);
			System.out.println();
			
		}
		uinput.close();
	}
}
