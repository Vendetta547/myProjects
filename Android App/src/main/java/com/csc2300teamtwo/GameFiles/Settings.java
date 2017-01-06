package com.csc2300teamtwo.GameFiles;

/* This class is straight forward. It is simply a list of boolean values for our game settings. Everything is coded as static so that a settings object does not need
   to be instantiated. */  

public class Settings {

	private static boolean easy = true;
	private static boolean medium = false;
	private static boolean hard = false;

	private static boolean add = true;
	private static boolean sub = true;
	private static boolean mult = true;
	private static boolean div = true;

	public static boolean isEasy() {
		return easy;
	}

	public static boolean isMedium() {
		return medium;
	}

	public static boolean isHard() {
		return hard;
	}

	public static boolean isAdd() {
		return add;
	}

	public static boolean isSub() {
		return sub;
	}

	public static boolean isMult() {
		return mult;
	}

	public static boolean isDiv() {
		return div;
	}

	public static void setEasy(boolean easy) {
		Settings.easy = easy;
	}

	public static void setMedium(boolean medium) {
		Settings.medium = medium;
	}

	public static void setHard(boolean hard) {
		Settings.hard = hard;
	}

	public static void setAdd(boolean add) {
		Settings.add = add;
	}

	public static void setSub(boolean sub) {
		Settings.sub = sub;
	}

	public static void setMult(boolean mult) {
		Settings.mult = mult;
	}

	public static void setDiv(boolean div) {
		Settings.div = div;
	}
}
