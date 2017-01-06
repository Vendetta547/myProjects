package com.csc2300teamtwo.GameFiles;

import java.util.List;

import android.graphics.Color;
import android.graphics.Paint;
import java.util.Random;
import android.graphics.Rect;

import com.csc2300teamtwo.framework.Game;
import com.csc2300teamtwo.framework.Graphics;
import com.csc2300teamtwo.framework.Image;
import com.csc2300teamtwo.framework.Input.TouchEvent;
import com.csc2300teamtwo.framework.Screen;
import com.csc2300teamtwo.framework.Sound;


//This is the game screen

public class Starting extends Screen {

	enum GameState {
		Ready, Running, Paused, GameOver
	}

	GameState state = GameState.Ready;

	private Random random = new Random();
	public static Player player, opponent;
	private static MathProblems problems;				// declare objects and variables to use
	public static int score = 0;
	private static Sound good, bad, punch, win, lose;
	private boolean hasBeenPlayed = false;


	private Image image, currentPlayer, character, character2, characterAttack, characterHit;
	private Image currentEnemy, enemy, enemy2, enemyAttack, enemyHit, background;			// more objects and variables to use.
	private Graphics graphics;
	private Animation panim, oanim;

	private int loc1 = 80;
	private int loc2 = 295;			// location of answers to be painted to the screen
	private int loc3 = 510;
	private int loc4 = 725;

	private int config;
	private boolean hasBeenRandomized = false;		// variable to control randomization of answer set locations

	private int choice1;
	private int choice2;		// variables to hold player choices
	private int choice3;
	private int choice4;


	Paint paint, paint2, paint3, paint4;	// paint objects for drawing strings


	public Starting(Game game) {
		super(game);


		player = new Player(280, 180);
		opponent = new Player(420, 180);		// initialize and construct objects
		problems = new MathProblems();


		// Image setups
		background = Assets.background;

		character = Assets.character;
		character2 = Assets.character2;		// initialize all of our image declarations with pictures.
		characterAttack = Assets.characterAttack;
		characterHit = Assets.characterHit;

		enemy = Assets.enemy;
		enemy2 = Assets.enemy2;
		enemyHit = Assets.enemyHit;
		enemyAttack = Assets.enemyAttack;


		// Make animation objects and add frames to their arrays
		panim = new Animation(); // animation object for player character
		panim.addFrame(character, 50);
		panim.addFrame(character2, 50);
		currentPlayer = panim.getImage();


		good = Assets.correct;	// initialize sound declarations.
		bad = Assets.incorrect;
		punch = Assets.punch;
		win = Assets.win;
		lose = Assets.lose;

		oanim = new Animation(); // animation object for opponent
		oanim.addFrame(enemy, 50);
		oanim.addFrame(enemy2, 50);
		currentEnemy = oanim.getImage();


		paint = new Paint();
		paint.setTextSize(30);						// paint object definitions.
		paint.setTextAlign(Paint.Align.CENTER);
		paint.setAntiAlias(true);
		paint.setColor(Color.WHITE);

		paint2 = new Paint();
		paint2.setTextSize(100);
		paint2.setTextAlign(Paint.Align.CENTER);
		paint2.setAntiAlias(true);
		paint2.setColor(Color.WHITE);

		paint3 = new Paint();
		paint3.setTextSize(70);
		paint3.setTextAlign(Paint.Align.CENTER);
		paint3.setAntiAlias(true);
		paint3.setColor(Color.WHITE);

		paint4 = new Paint();
		paint4.setTextSize(50);
		paint4.setTextAlign(Paint.Align.CENTER);
		paint4.setAntiAlias(true);
		paint4.setColor(Color.BLACK);
	}

	@Override
	public void update(float deltaTime) {
		List<TouchEvent> touchEvents = game.getInput().getTouchEvents();

		if (state == GameState.Ready)
			updateReady(touchEvents);
		if (state == GameState.Running)				// four separate update methods based on the state of the game.
			updateRunning(touchEvents, deltaTime);
		if (state == GameState.Paused)
			updatePaused(touchEvents);
		if (state == GameState.GameOver)
			updateGameOver(touchEvents);
	}

	private void updateReady(List<TouchEvent> touchEvents) {	// the first state that the game enters
		if (touchEvents.size() > 0)
			state = GameState.Running;
	}

	private boolean checkAnswer(int choice) {		// function that compares the user input to the correct answer.
		if (choice == problems.getCorrect_answer()) {
			return true;
		} else {
			return false;
		}
	}

	private void checkHealth() {		// checks player and opponent health to see if the game should still be running.
		if (player.getHealth() == 0 || opponent.getHealth() == 0) {
			state = GameState.GameOver;
		}
	}

	private void updateRunning(List<TouchEvent> touchEvents, float deltaTime) { // update function for the running game

		int len = touchEvents.size();


		currentPlayer = panim.getImage();	// cycle through animation images for the player and the opponent.
		currentEnemy = oanim.getImage();


		for (int i = 0; i < len; i++) {	// handle touch events.
			TouchEvent event = touchEvents.get(i);

			if (event.type == TouchEvent.TOUCH_UP) {

				if (inBounds(event, 0, 0, 50, 50)) { // if user presses the pause button, then the game pauses
					pause();
				}
			}

			if (event.type == TouchEvent.TOUCH_DOWN) {
				if (inBounds(event, loc1 - 80, 360, 135, 100)) {	// if the user selects choice one, then check their answer.
					player.setChoice(choice1);						// if they are correct, then the positive sound clip plays,
					if (checkAnswer(player.getChoice()) == true) {	// the punch sound effect plays, the player punches the opponent,
						player.setCorrect(true);					// and the opponent takes damage.
						punch.play(0.20f);
						good.play(0.55f);
						currentPlayer = characterAttack;
						currentEnemy = enemyHit;
						assignDamage("opponent");
					}
					else {
						bad.play(0.55f);				// if they are wrong, then the bad sound clip plays, the punch sound effect plays,
						currentEnemy = enemyAttack;		// the enemy punches them, and they take damage.
						punch.play(0.20f);
						currentPlayer = characterHit;
						assignDamage("player");
					}

					problems.setHasBeenAnswered(true);	// eiher way, when they select a choice, the problem has been answered, and a new one is generate afterwards.
														// the rest of the touch event checks work the same way.
				} else if (inBounds(event, loc2 - 80, 360, 135, 100)) {
					player.setChoice(choice2);
					if (checkAnswer(player.getChoice()) == true) {
						player.setCorrect(true);
						punch.play(0.20f);
						good.play(0.55f);
						currentPlayer = characterAttack;
						currentEnemy = enemyHit;
						assignDamage("opponent");
					}
					else {
						bad.play(0.55f);
						currentEnemy = enemyAttack;
						punch.play(0.20f);
						currentPlayer = characterHit;
						assignDamage("player");
					}

					problems.setHasBeenAnswered(true);


				} else if (inBounds(event, loc3 - 80, 360, 135, 100)) {
					player.setChoice(choice3);
					if (checkAnswer(player.getChoice()) == true) {
						player.setCorrect(true);
						punch.play(0.20f);
						good.play(0.55f);
						currentPlayer = characterAttack;
						currentEnemy = enemyHit;
						assignDamage("opponent");
					}
					else {
						bad.play(0.55f);
						currentEnemy = enemyAttack;
						punch.play(0.20f);
						currentPlayer = characterHit;
						assignDamage("player");
					}

					problems.setHasBeenAnswered(true);

				} else if (inBounds(event, loc4 - 80, 360, 135, 100)) {
					player.setChoice(choice4);
					if (checkAnswer(player.getChoice()) == true) {
						player.setCorrect(true);
						punch.play(0.20f);
						good.play(0.55f);
						currentPlayer = characterAttack;
						currentEnemy = enemyHit;
						assignDamage("opponent");
					}
					else {
						bad.play(0.55f);
						currentEnemy = enemyHit;
						punch.play(0.20f);
						currentPlayer = characterHit;
						assignDamage("player");
					}

					problems.setHasBeenAnswered(true);
				}

			}


		}

		if (problems.isHasBeenAnswered() == true) {		// if the problem has been answered, then make a new problem
			problems.generateProblem();					// this problem hasn't been answered yet, so hasBeenAnswered is false.
			problems.setHasBeenAnswered(false);			// since it is a new problem, the answer set locations haven't been randomized either.
			hasBeenRandomized = false;					// the player's and opponent's choices are also reset for the next round.
			player.setChoice(-999);
			opponent.setChoice(-999);
		}

		player.update();		//update player and opponent information
		opponent.update();
		animate();		//run through the animations.

		checkHealth();		// and check their health.


	}


	private boolean inBounds(TouchEvent event, int x, int y, int width,
							 int height) {
		if (event.x > x && event.x < x + width - 1 && event.y > y
				&& event.y < y + height - 1)
			return true;
		else
			return false;
	}

	private void assignDamage(String damagedPlayer) {		// assigns damaged to appropriate player based on string parameter.
		if (damagedPlayer == "player") {
			player.setHealth(player.getHealth() - 33);
		} else if (damagedPlayer == "opponent") {
			opponent.setHealth(opponent.getHealth() - 33);
			opponent.setHealthBarX(opponent.getHealthBarX() + 33);
		}
	}

	private void updatePaused(List<TouchEvent> touchEvents) {		// handles the touch events in the pause menu.
		int len = touchEvents.size();
		for (int i = 0; i < len; i++) {
			TouchEvent event = touchEvents.get(i);
			if (event.type == TouchEvent.TOUCH_UP) {
				if (inBounds(event, 0, 0, 800, 240)) {

					if (!inBounds(event, 0, 0, 35, 35)) {
						resume();
					}
				}

				if (inBounds(event, 0, 240, 800, 240)) {
					nullify();
					goToMenu();
				}
			}
		}
	}

	private void updateGameOver(List<TouchEvent> touchEvents) {	// handles the touch events in the game over screen.
		int len = touchEvents.size();
		for (int i = 0; i < len; i++) {
			TouchEvent event = touchEvents.get(i);
			if (event.type == TouchEvent.TOUCH_DOWN) {
				if (inBounds(event, 300, 190, 200, 100)) {
					nullify();
					game.setScreen(new MainMenuScreen(game));
					return;
				}
			}
		}

	}

	public int randomizeLocation() {		// randomizes answer set locations.
		int selector = 1 + random.nextInt(4);
		return selector;
	}


	@Override
	public void paint(float deltaTime) {

		Graphics g = game.getGraphics();

		g.drawImage(background, 0, -150);
		g.drawImage(currentPlayer, player.getCenterX(), player.getCenterY());


		g.drawImage(currentEnemy, opponent.getCenterX(), opponent.getCenterY());


		g.drawRect(0, 0, player.getHealth(), 40, Color.RED);
		g.drawRect(opponent.getHealthBarX(), 0, opponent.getHealth(), 40, Color.RED);


		g.drawString("Score:", 100, 70, paint);
		g.drawString(Integer.toString(score), 200, 70, paint);


		if (state == GameState.Ready)		// depending on the game state, different things are drawn.
			drawReadyUI();
		if (state == GameState.Running)
			drawRunningUI();
		if (state == GameState.Paused)
			drawPausedUI();
		if (state == GameState.GameOver)
			drawGameOverUI();


	}


	public void animate() { // animation function
		panim.update(15); // integer parameter specifies the speed of the
		// animation
		oanim.update(15);

	}

	private void nullify() {

		// Set all variables to null.
		currentPlayer = null;
		character = null;
		character2 = null;
		characterHit = null;
		characterAttack = null;
		currentEnemy = null;
		enemy = null;
		enemy2 = null;
		enemyAttack = null;
		enemyHit = null;
		background = null;
		panim = null;
		oanim = null;
		score = 0;
		hasBeenPlayed = false;

		// Call garbage collector to clean up memory.
		System.gc();

	}


	private void drawReadyUI() {
		Graphics g = game.getGraphics();

		g.drawARGB(155, 0, 0, 0);
		g.drawString("Tap to Play.", 400, 240, paint);

	}

	private void drawRunningUI() {
		Graphics g = game.getGraphics();

		g.drawImage(Assets.pause_button, 0, 0);

		if (problems.isHasBeenAnswered() == false) {
			g.drawString(problems.getProblem(), 380, 120, paint3);	// draws the problem to the screen.

			if (hasBeenRandomized == false) {
				config = randomizeLocation();	// keeps the game from constantly looping through random configurations and drawing them.
				hasBeenRandomized = true;
			}

			switch (config) {	// there are four possible answer configurations depending on what number the random function returns.

				case 1:
					g.drawString(problems.getCorrectString(), loc1, 450, paint4);
					g.drawString(problems.getWrong_string1(), loc2, 450, paint4);
					g.drawString(problems.getWrong_string2(), loc3, 450, paint4);
					g.drawString(problems.getWrong_string3(), loc4, 450, paint4);

					choice1 = problems.getCorrect_answer();
					choice2 = -999;
					choice3 = -999;
					choice4 = -999;


					break;

				case 2:
					g.drawString(problems.getCorrectString(), loc2, 450, paint4);
					g.drawString(problems.getWrong_string1(), loc1, 450, paint4);
					g.drawString(problems.getWrong_string2(), loc3, 450, paint4);
					g.drawString(problems.getWrong_string3(), loc4, 450, paint4);

					choice1 = -999;
					choice2 = problems.getCorrect_answer();
					choice3 = -999;
					choice4 = -999;

					break;

				case 3:
					g.drawString(problems.getCorrectString(), loc3, 450, paint4);
					g.drawString(problems.getWrong_string1(), loc2, 450, paint4);
					g.drawString(problems.getWrong_string2(), loc1, 450, paint4);
					g.drawString(problems.getWrong_string3(), loc4, 450, paint4);

					choice1 = -999;
					choice2 = -999;
					choice3 = problems.getCorrect_answer();
					choice4 = -999;

					break;

				default:
					g.drawString(problems.getCorrectString(), loc4, 450, paint4);
					g.drawString(problems.getWrong_string1(), loc2, 450, paint4);
					g.drawString(problems.getWrong_string2(), loc3, 450, paint4);
					g.drawString(problems.getWrong_string3(), loc1, 450, paint4);

					choice1 = -999;
					choice2 = -999;
					choice3 = -999;
					choice4 = problems.getCorrect_answer();

					break;


			}
		}
	}



	private void drawPausedUI() {
		Graphics g = game.getGraphics();
		// Darken the entire screen so you can display the Paused screen.
		g.drawARGB(155, 0, 0, 0);
		g.drawString("Resume", 400, 165, paint2);
		g.drawString("Menu", 400, 360, paint2);

	}

	private void drawGameOverUI() {		// game over screen. draws different images and plays different sounds according to if player wins or loses.
		Graphics g = game.getGraphics();
		g.drawRect(0, 0, 1281, 801, Color.BLACK);

		if (player.getHealth() == 0) {		// if player loses
			if (hasBeenPlayed == false) {
				lose.play(0.15f);
				hasBeenPlayed = true;
			}
			g.drawString("You Lose", 400, 240, paint2);
			g.drawString("Tap to return.", 400, 290, paint);
		}

		else if (opponent.getHealth() == 0) {	// if player wins
			if (hasBeenPlayed == false) {
				win.play(0.15f);
				hasBeenPlayed = true;
			}
			g.drawString("You Win", 400, 240, paint2);
			g.drawString("Tap to return.", 400, 290, paint);
		}

	}



	@Override
	public void pause() {		// sets the game to paused.
		if (state == GameState.Running)
			state = GameState.Paused;

	}

	@Override
	public void resume() {
		if (state == GameState.Paused)
			state = GameState.Running;
	}

	@Override
	public void dispose() {

	}

	@Override
	public void backButton() {
		pause();
	}

	private void goToMenu() {
		// TODO Auto-generated method stub
		game.setScreen(new MainMenuScreen(game));

	}

}






