package dragonLore;

public class GameRunner {

	public static void main(String[] args) {
		String[] p = {"Giant Fists", "Elephant Eruption", "Savage Cold", "Blitz"};
		String[] l = {"Shameless Cricket", "Jolt", "Parallel Crocodile", "Guarding Assault"};
		String[] j = {"Lost Horse", "Dreaming Attack", "Harming Rock", "Evil Wasp", "Enforcing Swan", "Alighting Force of Blind Phantom Diving Stomp of Watchful Phoenix"};
		Game newGame = new Game(p, l, j);
		newGame.start();
		
//		int min = 150;
//		int max = 0;
//		int x = 0;
//		Random rand = new Random();
//		for(int i=0; i<1000; i++) {
//			x = rand.nextInt(20)+61;
//			if(x<min) {
//				min = x;
//			} else if(x > max) {
//				max = x;
//			}
//			System.out.println(x);
//			System.out.println(max+", "+min);
//		}
	}
}
