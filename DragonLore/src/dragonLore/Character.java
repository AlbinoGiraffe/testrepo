package dragonLore;

import java.util.Random;

public class Character {
	private String name;
	private int health;
	private int speed;
	private String[] moveList;
	private int maxHealth;
	private int maxDamage;
	
	//Default Constructor
	public Character() {
		name = null;
		health = 0;
		speed = 0;
		moveList = null;
		maxHealth = health;
	}
	
	//Custom Constructor
	public Character(String n, int value, int value2, String[] moves) {
		this.name = n;
		this.health = value;
		this.speed = value2;
		this.moveList = moves;
		this.maxHealth = health;
		this.maxDamage = 100;
	}
	
	public Character(String n, int value, int value2, String[] moves, int maxDamage) {
		this.name = n;
		this.health = value;
		this.speed = value2;
		this.moveList = moves;
		this.maxHealth = health;
		this.maxDamage = maxDamage;
	}
	
	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public int getHealth() {
		return health;
	}
	
	public int getMaxHealth() {
		return maxHealth;
	}
	
	public int getSpeed() {
		return speed;
	}
	
	public void getMoveList() {
		for(int i=0; i<moveList.length; i++) {
			System.out.println(i+1+": "+moveList[i]);
		}
	}
	
	public int attack(String s) {
		int damage = damageDealt();
		for(int i=1; i<=moveList.length; i++) {
			if(s.equalsIgnoreCase(moveList[i-1]) || s.equalsIgnoreCase(""+i)) {
				System.out.println(name + " used " + moveList[i-1] + " and dealt " + damage+ " damage!");
				return damage;
			}
		}
		System.out.println("This isn't valid! What r u doing? U dont get a turn!");
		return 0;
	}
	
	public int computerAttack() {
		Random rand = new Random();
		int damage = damageDealt();
		System.out.println(name + " used " + moveList[rand.nextInt(moveList.length)] + " and dealt " + damage +" damage!");
		return damage;
	}
	
	public int damageDealt() {
		Random rand = new Random();
		int x = rand.nextInt(20)+maxDamage;
		return x;
	}
	
	public void setHealth(int n) {
		health = n;
	}
	
	public void damage(int n) {
		health -= n;
	}
	
	public void heal() {
		health = maxHealth;
	}
}
