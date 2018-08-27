package drawing;

public class Drawing {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		shape();
		shape();
		rect();
		System.out.println("    *    ");
		System.out.println("    *    ");
		System.out.println("    *    ");
		
	}
	
	public static void rect() {
		System.out.println("* * * * *");
		System.out.println("* * * * *");
	}
	
	public static void box() {
		System.out.println("  *   *  ");
		System.out.println("    *    ");
		System.out.println("  *   *  ");
	}
	
	public static void shape() {
		rect();
		box();
	}

}
