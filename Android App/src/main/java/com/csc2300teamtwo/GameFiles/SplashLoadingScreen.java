package com.csc2300teamtwo.GameFiles;

import com.csc2300teamtwo.framework.Game;
import com.csc2300teamtwo.framework.Graphics;
import com.csc2300teamtwo.framework.Graphics.ImageFormat;
import com.csc2300teamtwo.framework.Screen;

public class SplashLoadingScreen extends Screen {
	public SplashLoadingScreen(Game game) {
		super(game);
	}

	@Override
	public void update(float deltaTime) {
		Graphics g = game.getGraphics();
		Assets.splash= g.newImage("splash.png", ImageFormat.RGB565);

		
		game.setScreen(new LoadingScreen(game));

	}

	@Override
	public void paint(float deltaTime) {

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