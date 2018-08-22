package dragonLore;
import java.util.Random;
import java.util.Scanner;

public class Game {
	private Scanner in;
	private String uinput;
	private Character p;
	private Character lucifer;
	private Character jesus;
	private Random r;
	private int luciferScore;
	private static final boolean SLEEP = true;
	
	public Game(String[] playerList, String[] luciferList, String[] jesusList) {
		this.uinput = "";
		this.in = new Scanner(System.in);
		this.r = new Random();
		this.p = new Character("", 150, 20, playerList);
		this.lucifer = new Character("Lucifer", 228, 15, luciferList, 60);
		this.jesus = new Character("Jesus™", 456, 22, jesusList, 80);
		this.luciferScore = 0;
	}
	
	public void start() {
		level0();
	}
	
	public void level0() {
		System.out.println("What is your name, benevolent one?");
		this.p.setName(in.nextLine());
		level1();
	}

	public void level1() {
		System.out.println("\nHello, "+p.getName()+", our lord and savior.");
		System.out.println("We're so glad you could make it, we were about to start The Rapture without you, Raptor Jesus™!");
		sleep(3000);
		System.out.println("Just then, Jesus™ himself walks into the room:");
		System.out.println("Jesus™: BINGBONG YOU AIN'T GON DO SHORT");
		sleep(1000);
		System.out.println("You are killed by Jesus™\n");
		sleep(3000);
		level2();
	}
	
	private void level2() {
		System.out.println("You wake up after three long days.");
		System.out.println("You are dead.");
		System.out.println("1) Oh well...");
		System.out.println("2) Go to heaven!");
		System.out.print("Choose: ");
		uinput = in.nextLine();
		System.out.println();
		
		if(uinput.equalsIgnoreCase("Oh well...") ||
		   uinput.equalsIgnoreCase("Oh well")    ||
		   uinput.equalsIgnoreCase("1"))
		{
			System.out.println(p.getName()+" has left the game.\n");
		} 
		else if(uinput.equalsIgnoreCase("Go to heaven!") ||
		        uinput.equalsIgnoreCase("Go to heaven")  ||
				uinput.equalsIgnoreCase("heaven")        ||
				uinput.equalsIgnoreCase("2"))
		 {
			heaven();
		 } else {
			 System.out.println("I don't understand :/\n");
			 level2();
		 }
		
	}

	private void heaven() {
		System.out.println("Despite Jesus™ going out of his way to kill you, you somehow manage to get to Heaven.");
		System.out.println("Upon arriving in Heaven, you realize that things are not as they have seemed in magazines and postcards");
		System.out.println("Heaven's glorious white walls and floors made of clouds had taken a dreary and rundown appearance.");
		System.out.println("You then come to the realization that Heaven had been corrupted by some outside force...");
		sleep(6000);
		System.out.println("");
		System.out.println("Knowing that Jesus™ is probably around somewhere, you sneak around the less than optimal final destination.");
		System.out.println("You then reach a vantage point where you can see miles of nothing but dirty clouds.");
		System.out.println("A little old lady tells you that Jesus™ has been corrupted by a certain forbidden Drink");
		System.out.println("When asked for more information, she says that the corruption is because of the most disgusting drink in the world, \"Go Go Juice\"");
		sleep(6000);
		System.out.println("");
		System.out.println("The Go Go juice had done something to Heaven and probably Jesus™, as the environment looked very worn down and corrupt.");
		System.out.println("You decide to go find Jesus™ even though he might kill you again.");
		System.out.println("Suddenyly, you spot a conveniently placed mansion that would be fit for a god to live in.");
		System.out.println("Following the plot driven path you come across a figure in the center of the mansion.");
		sleep(6000);
		System.out.println("");
		doyouwanttodie();
	}

	private void doyouwanttodie() {
		// TODO Auto-generated method stub
		System.out.println("Jesus™ turns around and says, \"Do you want to die?!\"");
		System.out.println("1) Yes");
		System.out.println("2) No");
		System.out.println("Choose: ");
		uinput = in.nextLine();
		if(uinput.equalsIgnoreCase("yes") ||
		   uinput.equalsIgnoreCase("1"))
		   {
			savetheworld();
		   } else if(uinput.equalsIgnoreCase("no") ||
				     uinput.equalsIgnoreCase("2")) 
		   {	
			System.out.println("Jesus™ yells for you to run, but you don't listen to him.");
			System.out.println("You die of Indignation.");
			System.out.println("");
			restart();
		   } else {
			   System.out.println("What are you saying???");
			   System.out.println("");
			   doyouwanttodie();
		   }
	}

	private void restart() {
		// TODO Auto-generated method stub
		System.out.println("Play again?");
		System.out.println("1) YES");
		System.out.println("2) Nah...");
		System.out.println("Choose: ");
		uinput = in.nextLine();
		if(uinput.equalsIgnoreCase("yes") ||
		   uinput.equalsIgnoreCase("yea") ||
		   uinput.equalsIgnoreCase("1")) {
			start();
		} else {
			quit();
		}
	}

	private void quit() {
		System.out.println("Okay.....");
		System.out.println(p.getName()+" left the game.");
	}

	private void savetheworld() {
		System.out.println("Jesus™ struggles to compose  himself, not letting the corrupted side of him to take over.");
		System.out.println("Jesus™ says, \"the source of the Go Go Juice has to be stopped at once!\"");
		System.out.println("\"I've sent many men out of Heaven on this quest to destroy the source, but Heaven succumbed to the corruption soon enough.\"");
		System.out.println("\"I believe the source of the Go Go Juice is somewhere in hell, but it is very important to tell you that Satan IS NOT at fault\" (ily satan <3)");
		System.out.println("\"Go on and fight for me, even though I killed you...\"");
		sleep(3000);
		System.out.println("");
		System.out.println("You go down to Hell(how ironic) and meet up with the squad that Jesus™ sent down to fight the Go Go Juice");
		System.out.println("Apparently, as said by your squad, the Go Go Juice is being produced and distributed by some random redneck");
		System.out.println("mom. (Somehow, this doesn't surprise you)");
		System.out.println("Arriving at the place where the source of the Go Go Juice was supposed to be, you find ");
		System.out.println("that there was now a giant hole where the source was supposed to be.");
		System.out.println("It was still burning and releasing noxious fumes of Go Go Juice.");
		sleep(3000);
		System.out.println("");
		System.out.println("You and your squad decide to go to Satan's crib to find an explanation");
		System.out.println("Arriving at Satan's luxury cardboard box, you find Lucifer instead.");
		System.out.println("Lucifer:  I'm the grumpy old troll who lives under the bridge, hey I'm the grumpy old troll who lives under the bridge");
		System.out.println("who's there if you wanna come over, All you have to do is this! all you have to do is this;");
		System.out.println("");
		System.out.println("Answer 3 questions correctly and I let you pass:");
		answerQuestions();
	}

	private void answerQuestions() {
		String[] questions = {"How do you like your steak?", "If your friend gets castrated, will you snort their ashes?", "Do you want to build a snowman?"};
		String[] responses = {"Hmmm. Interesting", "Intriguing.", "Nani?", "Interesting...", "Lol wut?"};
		for(int i = 0; i<3; i++) {
			System.out.println(questions[i]);
			uinput = in.nextLine();
			sleep(1000);
			System.out.println("Lucifer: "+responses[r.nextInt(responses.length)]);
			if(r.nextInt(100)+1 >= 60) {
				luciferScore++;
			}
			System.out.println("Lucifer Score: "+luciferScore);
		}
		if(luciferScore>=2) {
			System.out.println("");
			lucifer();
		} else {
			System.out.println("");
			System.out.println("These answers suck! U wot m8?!?!? Fite me!!!");
			if(fight(p, lucifer)) {
				System.out.println("You have killed Lucifer, magically blowing up the rest of the Go Go Juice factories.");
				sleep(1000);
				System.out.println("You win!!!");
			} else {
				quit();
			}
		}
	}
	
	public void sleep(int milis) {
		if(SLEEP) {
			try {
			Thread.sleep(milis);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}

	public void lucifer() {
		System.out.println("Lucifer: I judge that your judgement is judgementally correct.");
		System.out.println("Lucifer: You should seek out the Flying Spaghetti Monster.");
		System.out.println("Lucifer: It's the only thing Satan told me to tell you guys to do so uhh yeah...");
		sleep(2000);
		System.out.println("");
		System.out.println("It takes you three days to find the elusive Flying Spaghetti Monster.");
		sleep(1000);
		System.out.println("");
		System.out.println("You find the Flying Spaghetti Monster at his house called, \"Mom's Spaghetti\"");
		System.out.println("Coincidentally, his house was indeed made by his mum.");
		System.out.println("Flying Spaghetti Monster: Satan is destroying Heaven and is soon going to kill Jesus™");
		System.out.println("in order to stop the spread of corruption and to put and end to Jesus's plan of world domination with Go Go Juice");
		System.out.println("Flying Spaghetti Monster: You need to help Satan kill Jesus™! He will be near the stairs to Heaven");
		sleep(2500);
		System.out.println("");
		System.out.println("You arrive to the stairs to heaven to find that Satan is fighting Jesus™ with little success. Jesus™");
		System.out.println("is on a GIANT FORKING DRAGON and is reking every noob that comes in it's way.");
		System.out.println("Satan gets knocked down and Jesus says, \"Got any last words bingbong?\"");
		System.out.println("You intervene: \"Stop right there HEYSUS\"");
		System.out.println("Jesus™: I thought I killed you. Do you have a deathwish, not real PCMASTERRACE lord?");
		System.out.println("You abruptly reply, \"Nah but I know you have one, wannabe PCMasterRace console peasant\"");
		if(fight(p, jesus)) {
			System.out.println("");
			congrats();
		} else {
			System.out.println("You realize that you were actually running Windows Vista, and you die.");
			quit();
		}
		
		
	}
	
	private void congrats() {
		// TODO Auto-generated method stub
		System.out.println("Flying Spaghetti Monster: WOW!! You beat a console to death... and saved the world! Good job!1!! Now wake up.");
		System.out.println("*Lol wut?*");
		System.out.println("*BLACK*");
		System.out.println("You were actually drunk and this was a dream the whole time. SURPRISE");
	}

	//Battle Methods
	public boolean fight(Character p, Character c) {
		boolean out = false;
		System.out.println("A challenger approaches! " + c.getName() + " wants to fight!");
		while(p.getHealth() > 0 && c.getHealth() > 0) {
			if (p.getSpeed() > c.getSpeed()) {
				System.out.println(p.getName()+ " gets to go first!");
				System.out.println("Choose a move: ");
				p.getMoveList();
				System.out.println("Choose: ");
				uinput = in.nextLine();
				c.damage(p.attack(uinput));
				p.damage(c.computerAttack());
			} else if (p.getSpeed() < c.getSpeed()) {
				System.out.println(c.getName()+ " gets to go first!");
				p.damage(c.computerAttack());
				System.out.println("Choose a move: ");
				p.getMoveList();
				System.out.println("Choose: ");
				uinput = in.nextLine();
				c.damage(p.attack(uinput));
			}
			System.out.println("You have "+p.getHealth()+ " health left.");
			System.out.println("The enemy "+c.getName()+" has "+c.getHealth()+" health left.");
		}
		if(p.getHealth() <= 0) {
			System.out.println("You suck and you lost the fight.  Would you like to try again? (Y/N)");
			uinput = in.nextLine();
			if(uinput.equalsIgnoreCase("y")) {
				p.setHealth(p.getMaxHealth());
				c.setHealth(c.getMaxHealth());
				fight(p, c);
			} else {
				out = false;
			}
		} else {
			System.out.println("You have won against " + c.getName() + "!");
			out = true;
		}
		return out;
	}
}


