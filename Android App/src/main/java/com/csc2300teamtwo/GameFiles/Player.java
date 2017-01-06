package com.csc2300teamtwo.GameFiles;



public class Player {

	public Player(int x, int y) {  // constructor for player object
		centerX = x;
		centerY = y;
	}
	
	private int health = 330;
	private int centerX;			// centerX and centerY are the x and y screen coordinates of the character
	private int centerY;
	private int healthBarX = 470;

	private boolean isCorrect = false;
	private int choice = -999;


	public void update() {
		if (isCorrect) {
			Starting.score += 1000;		// if the player is correct, update the score.
		}

		choice = -999;
		isCorrect = false;			// reset the player's choice and set isCorrect to false in order to avoid endless looping within the main game loop

	}

	public int getHealth() {	// the rest are getters and setters for all Player variables so that they may be accessed by other classes.
		return health;
	}

	public int getCenterX() {
		return centerX;
	}

	public int getCenterY() {
		return centerY;
	}

	public void setHealth(int health) {
		this.health = health;
	}

	public void setCenterX(int centerX) {
		this.centerX = centerX;
	}

	public void setCenterY(int centerY) {
		this.centerY = centerY;
	}

	public boolean isCorrect() {
		return isCorrect;
	}

	public void setCorrect(boolean isCorrect) {
		this.isCorrect = isCorrect;
	}

	public int getChoice() {
		return choice;
	}

	public void setChoice(int choice) {
		this.choice = choice;
	}

	public int getHealthBarX() { return healthBarX; }

	public void setHealthBarX(int healthBarX) { this.healthBarX = healthBarX; }
	}


