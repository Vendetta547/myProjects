package com.csc2300teamtwo.GameFiles;

import com.csc2300teamtwo.framework.Image;
import com.csc2300teamtwo.framework.Music;
import com.csc2300teamtwo.framework.Sound;

public class Assets {
	
	public static Image menu, settings, splash, background, image;
	public static Image currentPlayer, character, character2, characterAttack, characterHit;
	public static Image currentEnemy, enemy, enemy2, enemyAttack, enemyHit;
	public static Image backbutton, empty, filled, pause_button;
	public static Sound correct, incorrect, punch, win, lose;
	public static Music theme;
	
	public static void load(SampleGame sampleGame) {
		// TODO Auto-generated method stub
		correct = sampleGame.getAudio().createSound("ting.mp3");
		incorrect = sampleGame.getAudio().createSound("buzzer.mp3");
		punch = sampleGame.getAudio().createSound("Punch_sound.mp3");		// initializes sounds and music
		win = sampleGame.getAudio().createSound("victory.mp3");
		lose = sampleGame.getAudio().createSound("failure.mp3");
		theme = sampleGame.getAudio().createMusic("Theme.mp3");

		theme.setLooping(true);
		theme.setVolume(1.10f);
		theme.play();
	}
	
}
