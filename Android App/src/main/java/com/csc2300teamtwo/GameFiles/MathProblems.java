package com.csc2300teamtwo.GameFiles;

import java.util.Random;
import java.lang.String;


// Procedural database for the game. Utilizes randomized integers to generate math problems and answer sets.


public class MathProblems {

	Random random = new Random();


	private boolean easy = Settings.isEasy();
	private boolean medium = Settings.isMedium();		// read from settings and set to variables for readability
	private boolean hard = Settings.isHard();

	private boolean add = Settings.isAdd();
	private boolean sub = Settings.isSub();
	private boolean mult = Settings.isMult();
	private boolean div = Settings.isDiv();

	private static int correct_answer;
	private int fake_answer;					// answer set to be created
	private int wrong_answer2;
	private int wrong_answer3;


	private String correct_string;
	private String wrong_string1;		// variables used to paint answer sets to screen
	private String wrong_string2;
	private String wrong_string3;

	private String problem;

	private boolean hasBeenAnswered = true;		// controls flow of problem generation in the game


	public int randomOperator() {
		int selector = 1 + random.nextInt(4);		// returns a random integer to help randomize generated operators in math problems
		return selector;
	}


	String convertToString(int a, int b, String c) {	// converts randomly generated numbers into a problem to be displayed on the game screen
		Integer.toString(a);
		Integer.toString(b);

		if (c == "A") {
			return a + " " + "+" + " " + b;
		}

		else if (c == "S") {
			return a + " " + "-" + " " + b;
		}

		else if (c == "M") {
			return a + " " + "x" + " " + b;
		}

		else {
			return a + " " + "/" + " " + b;
		}
	}
	//added by jps5a
	public MathProblems() {
		generateProblem();
	}
	//end of added method
	//The first section of generateProblem (everything within "if (easy){ if (add && randomOperator() == 1) {}}) will be commented since the rest follows a similar pattern

	public void generateProblem() {		// generates the problem and answer sets
		int first_number;
		int second_number;
		int value_holder; // used to swap places in subtraction sections' IF statements.

		if (easy) {		// if easy is selected in the settings menu
			first_number = 1 + random.nextInt(5);			//generate two numbers
			second_number = 1 + random.nextInt(10);

			if (add && randomOperator() == 1) {		// if addition is randomly selected
				problem = convertToString(first_number, second_number, "A");
				correct_answer = arithmetic(first_number, second_number, 'A');
				correct_string = Integer.toString(correct_answer);				// compute the correct answer, along with fake answers
				fake_answer = correct_answer + (1 + random.nextInt(10));		// and then convert them into strings for screen display
				wrong_string1 = Integer.toString(fake_answer);
				wrong_answer2 = correct_answer + (1 + random.nextInt(5));
				wrong_string2 = Integer.toString(wrong_answer2);
				wrong_answer3 = correct_answer - (1 + random.nextInt(5));
				wrong_string3 = Integer.toString(wrong_answer3);
			}

			else if (sub && randomOperator() == 2) {

				first_number = 1 + random.nextInt(10);		// the rest of the code is very similar, with the exception of subtraction and division.
															// extra checks are needed to make sure two numbers do not subtract to give a negative number
															// and that two numbers divide evenly
				if (first_number < second_number) {
					value_holder = first_number;
					first_number = second_number;
					second_number = value_holder;
					
					problem = convertToString(first_number, second_number, "S");
					correct_answer = arithmetic(first_number, second_number, 'S');
					correct_string = Integer.toString(correct_answer);
					fake_answer = arithmetic(first_number, second_number, 'A');
					wrong_string1 = Integer.toString(fake_answer);
					wrong_answer2 = correct_answer + (1 + random.nextInt(5));
					wrong_string2 = Integer.toString(wrong_answer2);
					wrong_answer3 = correct_answer - (1 + random.nextInt(5));
				} else {
					problem = convertToString(first_number, second_number, "S");
					correct_answer = arithmetic(first_number, second_number, 'S');
					correct_string = Integer.toString(correct_answer);
					fake_answer = arithmetic(first_number, second_number, 'A');
					wrong_string1 = Integer.toString(fake_answer);
					wrong_answer2 = correct_answer + (1 + random.nextInt(5));
					wrong_string2 = Integer.toString(wrong_answer2);
					wrong_answer3 = correct_answer - (1 + random.nextInt(5));
					wrong_string3 = Integer.toString(wrong_answer3);
				}
			}

			else if (mult && randomOperator() == 3) {
				problem = convertToString(first_number, second_number, "M");
				correct_answer = arithmetic(first_number, second_number, 'M');
				correct_string = Integer.toString(correct_answer);
				fake_answer = arithmetic(first_number, second_number, 'S');
				wrong_string1 = Integer.toString(fake_answer);
				wrong_answer2 = correct_answer + (1 + random.nextInt(5));
				wrong_string2 = Integer.toString(wrong_answer2);
				wrong_answer3 = correct_answer - (1 + random.nextInt(5));
				wrong_string3 = Integer.toString(wrong_answer3);
			}

			else if (div && randomOperator() == 4) {

				first_number = 1 + random.nextInt(10);
				second_number = 1 + random.nextInt(10);

				if (first_number % second_number != 0) {
					generateProblem();
				} else {
					problem = convertToString(first_number, second_number, "D");
					correct_answer = arithmetic(first_number, second_number, 'D');
					correct_string = Integer.toString(correct_answer);
					fake_answer = arithmetic(first_number, second_number, 'A');
					wrong_string1 = Integer.toString(fake_answer);
					wrong_answer2 = correct_answer + (1 + random.nextInt(5));
					wrong_string2 = Integer.toString(wrong_answer2);
					wrong_answer3 = correct_answer - (1 + random.nextInt(5));
					wrong_string3 = Integer.toString(wrong_answer3);
				}
			}
		}

	else if (medium) {
		first_number = 1 + random.nextInt(5);
		second_number = 1 + random.nextInt(25);

		if (add && randomOperator() == 1) {
			problem = convertToString(first_number, second_number, "A");
			correct_answer = arithmetic(first_number, second_number, 'A');
			correct_string = Integer.toString(correct_answer);
			fake_answer = correct_answer + (1 + random.nextInt(10));
			wrong_string1 = Integer.toString(fake_answer);
			wrong_answer2 = correct_answer + (1 + random.nextInt(5));
			wrong_string2 = Integer.toString(wrong_answer2);
			wrong_answer3 = correct_answer - (1 + random.nextInt(5));
			wrong_string3 = Integer.toString(wrong_answer3);
		}

		else if (sub && randomOperator() == 2) {
			
			first_number = 1 + random.nextInt(25);
			
			if (first_number < second_number) {
				value_holder = first_number;
				first_number = second_number;
				second_number = value_holder;
				
				problem = convertToString(first_number, second_number, "S");
				correct_answer = arithmetic(first_number, second_number, 'S');
				correct_string = Integer.toString(correct_answer);
				fake_answer = arithmetic(first_number, second_number, 'A');
				wrong_string1 = Integer.toString(fake_answer);
				wrong_answer2 = correct_answer + (1 + random.nextInt(5));
				wrong_string2 = Integer.toString(wrong_answer2);
				wrong_answer3 = correct_answer - (1 + random.nextInt(5));
				wrong_string3 = Integer.toString(wrong_answer3);
			} else {
				problem = convertToString(first_number, second_number, "S");
				correct_answer = arithmetic(first_number, second_number, 'S');
				correct_string = Integer.toString(correct_answer);
				fake_answer = arithmetic(first_number, second_number, 'A');
				wrong_string1 = Integer.toString(fake_answer);
				wrong_answer2 = correct_answer + (1 + random.nextInt(5));
				wrong_string2 = Integer.toString(wrong_answer2);
				wrong_answer3 = correct_answer - (1 + random.nextInt(5));
				wrong_string3 = Integer.toString(wrong_answer3);
			}
		}

		else if (mult && randomOperator() == 3) {
			problem = convertToString(first_number, second_number, "M");
			correct_answer = arithmetic(first_number, second_number, 'M');
			correct_string = Integer.toString(correct_answer);
			fake_answer = arithmetic(first_number, second_number, 'S');
			wrong_string1 = Integer.toString(fake_answer);
			wrong_answer2 = correct_answer + (1 + random.nextInt(5));
			wrong_string2 = Integer.toString(wrong_answer2);
			wrong_answer3 = correct_answer - (1 + random.nextInt(5));
			wrong_string3 = Integer.toString(wrong_answer3);
		}

		else if (div && randomOperator() == 4) {

			first_number = 1 + random.nextInt(25);

			if (first_number % second_number != 0) {
				generateProblem();
			} else {
				problem = convertToString(first_number, second_number, "D");
				correct_answer = arithmetic(first_number, second_number, 'D');
				correct_string = Integer.toString(correct_answer);
				fake_answer = arithmetic(first_number, second_number, 'A');
				wrong_string1 = Integer.toString(fake_answer);
				wrong_answer2 = correct_answer + (1 + random.nextInt(5));
				wrong_string2 = Integer.toString(wrong_answer2);
				wrong_answer3 = correct_answer - (1 + random.nextInt(5));
				wrong_string3 = Integer.toString(wrong_answer3);
			}
		}

	}

	else if(hard) {
		first_number = 10 + random.nextInt(6);
		second_number = 1 + random.nextInt(60);

		if (add && randomOperator() == 1) {
			problem = convertToString(first_number, second_number, "A");
			correct_answer = arithmetic(first_number, second_number, 'A');
			correct_string = Integer.toString(correct_answer);
			fake_answer = correct_answer + (1 + random.nextInt(10));
			wrong_string1 = Integer.toString(fake_answer);
			wrong_answer2 = correct_answer + (1 + random.nextInt(5));
			wrong_string2 = Integer.toString(wrong_answer2);
			wrong_answer3 = correct_answer - (1 + random.nextInt(5));
			wrong_string3 = Integer.toString(wrong_answer3);
		}

		else if (sub && randomOperator() == 2) {
			
			first_number = 1 + random.nextInt(60);
			
			if (first_number < second_number) {
				value_holder = first_number;
				first_number = second_number;
				second_number = value_holder;
				
				problem = convertToString(first_number, second_number, "S");
				correct_answer = arithmetic(first_number, second_number, 'S');
				correct_string = Integer.toString(correct_answer);
				fake_answer = arithmetic(first_number, second_number, 'A');
				wrong_string1 = Integer.toString(fake_answer);
				wrong_answer2 = correct_answer + (1 + random.nextInt(5));
				wrong_string2 = Integer.toString(wrong_answer2);
				wrong_answer3 = correct_answer - (1 + random.nextInt(5));
				wrong_string3 = Integer.toString(wrong_answer3);
			} else {
				problem = convertToString(first_number, second_number, "S");
				correct_answer = arithmetic(first_number, second_number, 'S');
				correct_string = Integer.toString(correct_answer);
				fake_answer = arithmetic(first_number, second_number, 'A');
				wrong_string1 = Integer.toString(fake_answer);
				wrong_answer2 = correct_answer + (1 + random.nextInt(5));
				wrong_string2 = Integer.toString(wrong_answer2);
				wrong_answer3 = correct_answer - (1 + random.nextInt(5));
				wrong_string3 = Integer.toString(wrong_answer3);
			}
		}

		else if (mult && randomOperator() == 3) {
			problem = convertToString(first_number, second_number, "M");
			correct_answer = arithmetic(first_number, second_number, 'M');
			correct_string = Integer.toString(correct_answer);
			fake_answer = arithmetic(first_number, second_number, 'S');
			wrong_string1 = Integer.toString(fake_answer);
			wrong_answer2 = correct_answer + (1 + random.nextInt(5));
			wrong_string2 = Integer.toString(wrong_answer2);
			wrong_answer3 = correct_answer - (1 + random.nextInt(5));
			wrong_string3 = Integer.toString(wrong_answer3);
		}

		else if (div && randomOperator() == 4) {

			first_number = 1 + random.nextInt(60);

			if (first_number % second_number != 0) {
				generateProblem();
			} else {
				problem = convertToString(first_number, second_number, "D");
				correct_answer = arithmetic(first_number, second_number, 'D');
				correct_string = Integer.toString(correct_answer);
				fake_answer = arithmetic(first_number, second_number, 'A');
				wrong_string1 = Integer.toString(fake_answer);
				wrong_answer2 = correct_answer + (1 + random.nextInt(5));
				wrong_string2 = Integer.toString(wrong_answer2);
				wrong_answer3 = correct_answer - (1 + random.nextInt(5));
				wrong_string3 = Integer.toString(wrong_answer3);
			}
		}
	}

	}

	public int arithmetic(int a, int b, char c) {
		switch (c) {
		case 'A':
			return a + b;

		case 'S':
			return a - b;

		case 'M':
			return a * b;

		case 'D':
			return a / b;

		default:
			return 0;

		}

	}

	public static int getCorrect_answer() { return correct_answer;}

	public void setCorrect_answer(int correct_answer) {
		this.correct_answer = correct_answer;
	}

	public int getFake_answer() {
		return fake_answer;
	}

	public void setFake_answer(int fake_answer) {
		this.fake_answer = fake_answer;
	}

	public boolean isHasBeenAnswered() {
		return hasBeenAnswered;
	}

	public void setHasBeenAnswered(boolean hasBeenAnswered) {
		this.hasBeenAnswered = hasBeenAnswered;
	}

	public String getProblem() { return problem;}

	public void setProblem(String problem) { this.problem = problem;}

	public String getCorrectString() {
		return correct_string;
	}

	public String getWrong_string1() {
		return wrong_string1;
	}

	public String getWrong_string2() {
		return wrong_string2;
	}

	public String getWrong_string3() {
		return wrong_string3;
	}

	public void setWrong_string1(String wrong_string1) {
		this.wrong_string1 = wrong_string1;
	}

	public void setWrong_string2(String wrong_string2) {
		this.wrong_string2 = wrong_string2;
	}

	public void setWrong_string3(String wrong_string3) {
		this.wrong_string3 = wrong_string3;
	}
}
