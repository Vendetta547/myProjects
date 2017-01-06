package com.csc2300teamtwo.GameFiles;

import com.csc2300teamtwo.framework.Game;
import com.csc2300teamtwo.framework.Graphics;
import com.csc2300teamtwo.framework.Input.TouchEvent;
import com.csc2300teamtwo.framework.Screen;

import java.util.List;

public class MainMenuScreen extends Screen {
	public MainMenuScreen(Game game) {
		super(game);
	}

	@Override
	public void update(float deltaTime) {
		Graphics g = game.getGraphics();
		List<TouchEvent> touchEvents = game.getInput().getTouchEvents();

		int len = touchEvents.size();
		for (int i = 0; i < len; i++) {
			TouchEvent event = touchEvents.get(i);
			if (event.type == TouchEvent.TOUCH_UP) {

				if (inBounds(event, 50, 350, 250, 450)) {
					game.setScreen(new Starting(game));			// starts the game
				}

				else if (inBounds(event, 400, 350, 250, 450)) {
					game.setScreen(new SettingsScreen(game));	// brings user to the settings menu
				}

			}
		}
	}

	private boolean inBounds(TouchEvent event, int x, int y, int width,
			int height) {
		if (event.x > x && event.x < x + width - 1 && event.y > y		// inBounds is an input detection function
				&& event.y < y + height - 1)
			return true;
		else
			return false;
	}

	@Override
	public void paint(float deltaTime) {
		Graphics g = game.getGraphics();		// draws the menu screen
		g.drawImage(Assets.menu, 0, 0);
	}

	@Override
	public void pause() {
	}

	@Override
	public void resume() {

	}

	@Override
	public void dispose() {

	}

	@Override
	public void backButton() {
       // android.os.Process.killProcess(android.os.Process.myPid());

	}
}
