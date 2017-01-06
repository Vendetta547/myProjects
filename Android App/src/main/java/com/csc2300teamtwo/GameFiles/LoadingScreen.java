package com.csc2300teamtwo.GameFiles;

import com.csc2300teamtwo.framework.Game;
import com.csc2300teamtwo.framework.Graphics;
import com.csc2300teamtwo.framework.Graphics.ImageFormat;
import com.csc2300teamtwo.framework.Image;
import com.csc2300teamtwo.framework.Screen;

public class LoadingScreen extends Screen {
	public LoadingScreen(Game game) {
		
		super(game);
	}

	@Override
	public void update(float deltaTime) {
		Graphics g = game.getGraphics();
		Assets.menu = g.newImage("menu.png", ImageFormat.RGB565);
		Assets.settings = g.newImage("Ring_settings.png", ImageFormat.RGB565);      // assigns pictures to the image declarations
		Assets.background = g.newImage("Boxing_Ring.png", ImageFormat.RGB565);
		Assets.pause_button = g.newImage("pause.png", ImageFormat.RGB565);
		Assets.empty = g.newImage("empty_checkbox.png", ImageFormat.RGB565);
		Assets.filled = g.newImage("filled_checkbox.png", ImageFormat.RGB565);
		Assets.backbutton = g.newImage("back-button.png", ImageFormat.RGB565);
		Assets.character = g.newImage("Figure1.png", ImageFormat.ARGB4444);
		Assets.character2 = g.newImage("Figure2.png", ImageFormat.ARGB4444);
		Assets.characterAttack = g.newImage("FigureHit.png", ImageFormat.ARGB4444);
		Assets.characterHit = g.newImage("FigurePunched.png", ImageFormat.ARGB4444);

		
		Assets.enemy = g.newImage("OpponentFigure1.png", ImageFormat.ARGB4444);
		Assets.enemy2 = g.newImage("OpponentFigure2.png", ImageFormat.ARGB4444);
		Assets.enemyAttack = g.newImage("OpponentFigureHit.png", ImageFormat.ARGB4444);
		Assets.enemyHit = g.newImage("OpponentFigurePunched.png", ImageFormat.ARGB4444);


		
		game.setScreen(new MainMenuScreen(game));

	}

	@Override
	public void paint(float deltaTime) {
		Graphics g = game.getGraphics();			// draws a splash screen while loading
		g.drawImage(Assets.splash, 0, 0);
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

	}
}