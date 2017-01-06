"""A tic-tac-toe game made with Python using Tkinter. The game uses an AI as a second player instead of another human.

   Known Issue(s): Opponent automatically goes first after 'the cat' wins."""

from Tkinter import *
import tkMessageBox

master = Tk()
master.title('Tic-Tac-Toe')
master.geometry('135x125')
master.resizable(width=False, height=False)

gameRunning = True



#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________	

#registers the player's move on the screen
def playerMove(button):
	if button['text'] == ' ':
		button['text'] = 'X' 
	elif button['text'] == 'O':
		tkMessageBox.showinfo(' ', 'This spot is taken by the opponent. Try again.')
		return
	elif button['text'] == 'X':
		tkMessageBox.showinfo(' ', 'You  have already made a move in this spot. Try again.')
		return
	
	#every time the player makes a move, check to see if the game is over
	winCheck()
	
	#if the player wins after his last move, don't have the AI determine a move
	if gameRunning:
		opponentDetermineMove()
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________



#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________

#determines move that AI makes	
#this function is set up in three sections that are ranked in order of importance
def opponentDetermineMove():
	
	#section 1 (lowest importance)
	#this section focuses on finding the square which optimizes the number of winning paths
	#***********************************************************************************************************************************************************************************************
	button1_ways_to_win = 0
	button2_ways_to_win = 0 
	button3_ways_to_win = 0		#all states are initialized to 0 since we haven't checked them yet
	button4_ways_to_win = 0
	button5_ways_to_win = 0
	button6_ways_to_win = 0
	button7_ways_to_win = 0
	button8_ways_to_win = 0
	button9_ways_to_win = 0
	
	#by default, the first button is the best choice until something better is found
	max_ways_to_win = button1_ways_to_win
	choice = 'button1'
	
	#the rest of the section works identically to the following group of four if statements
	if button1['text'] == ' ':	#the square must first be empty in order to be considered
		if (button2['text'] == 'O' or button2['text'] == ' ' and button3['text'] == 'O' or
			button3['text'] == ' '): #then we check surrounding squares to see if they are occupied by O's or if they are empty. 
			button1_ways_to_win += 1 #essentially, we are looking for potential winning routes
									
									 #we will tally the number of winning routes together from each button and choose the highest among them for the move
									 
		if (button4['text'] == 'O' or button4['text'] == ' ' and button7['text'] == 'O' or
			button7['text'] == ' '):
			button1_ways_to_win += 1
			
		if (button5['text'] == 'O' or button5['text'] == ' ' and button9['text'] == 'O' or
			button9['text'] == ' '):
			button1_ways_to_win += 1
	
	
	if button2['text'] == ' ':
		if (button1['text'] == 'O' or button1['text'] == ' ' and button3['text'] == 'O' or
			button3['text'] == ' '):
			button2_ways_to_win += 1
			
		if (button5['text'] == 'O' or button5['text'] == ' ' and button8['text'] == 'O' or
			button8['text'] == ' '):
			button2_ways_to_win += 1
	
		if button2_ways_to_win > max_ways_to_win:
			max_ways_to_win = button2_ways_to_win
			choice = 'button2'
	
	
	if button3['text'] == ' ':
		if (button1['text'] == 'O' or button1['text'] == ' ' and button2['text'] == 'O' or
			button2['text'] == ' '):
			button3_ways_to_win += 1
		
		if (button5['text'] == 'O' or button5['text'] == ' ' and button7['text'] == 'O' or
			button7['text'] == ' '):
			button3_ways_to_win += 1
			
		if (button6['text'] == 'O' or button6['text'] == ' ' and button9['text'] == 'O' or
			button9['text'] == ' '):
			button3_ways_to_win += 1
	
		if button3_ways_to_win > max_ways_to_win:
			max_ways_to_win = button3_ways_to_win
			choice = 'button3'
	
	
	if button4['text'] == ' ':
		if (button1['text'] == 'O' or button1['text'] == ' ' and button7['text'] == 'O' or
			button7['text'] == ' '):
			button4_ways_to_win += 1
		
		if (button5['text'] == 'O' or button5['text'] == ' ' and button6['text'] == 'O' or
			button6['text'] == ' '):
			button4_ways_to_win += 1
		
		if button4_ways_to_win > max_ways_to_win:
			max_ways_to_win = button4_ways_to_win
			choice = 'button4'
	
	
	if button5['text'] == ' ':
		if (button1['text'] == 'O' or button1['text'] == ' ' and button9['text'] == 'O' or
			button9['text'] == ' '):
			button5_ways_to_win += 1
		
		if (button3['text'] == 'O' or button3['text'] == ' ' and button7['text'] == 'O' or
			button7['text'] == ' '):
			button5_ways_to_win += 1
			
		if (button2['text'] == 'O' or button2['text'] == ' ' and button8['text'] == 'O' or
			button8['text'] == ' '):
			button5_ways_to_win += 1
			
		if (button4['text'] == 'O' or button4['text'] == ' ' and button6['text'] == 'O' or
			button6['text'] == ' '):
			button5_ways_to_win += 1
			
		if button5_ways_to_win > max_ways_to_win:
			max_ways_to_win = button5_ways_to_win
			choice = 'button5'
		
			
	if button6['text'] == ' ':
		if (button3['text'] == 'O' or button3['text'] == ' ' and button9['text'] == 'O' or
			button9['text'] == ' '):
			button6_ways_to_win += 1
		
		if (button4['text'] == 'O' or button4['text'] == ' ' and button5['text'] == 'O' or
			button5['text'] == ' '):
			button6_ways_to_win += 1
			
		if button6_ways_to_win > max_ways_to_win:
			max_ways_to_win = button6_ways_to_win
			choice = 'button6'
		
			
	if button7['text'] == ' ':
		if (button1['text'] == 'O' or button1['text'] == ' ' and button4['text'] == 'O' or
			button4['text'] == ' '):
			button7_ways_to_win += 1
		
		if (button5['text'] == 'O' or button5['text'] == ' ' and button3['text'] == 'O' or
			button3['text'] == ' '):
			button7_ways_to_win += 1
			
		if (button8['text'] == 'O' or button8['text'] == ' ' and button9['text'] == 'O' or
			button9['text'] == ' '):
			button7_ways_to_win += 1
		
		if button7_ways_to_win > max_ways_to_win:
			max_ways_to_win = button7_ways_to_win
			choice = 'button7'
		
			
	if button8['text'] == ' ':
		if (button5['text'] == 'O' or button5['text'] == ' ' and button2['text'] == 'O' or
			button2['text'] == ' '):
			button3_ways_to_win += 1
		
		if (button9['text'] == 'O' or button9['text'] == ' ' and button7['text'] == 'O' or
			button7['text'] == ' '):
			button3_ways_to_win += 1
		
		if button8_ways_to_win > max_ways_to_win:
			max_ways_to_win = button8_ways_to_win
			choice = 'button8'
		
			
	if button9['text'] == ' ':
		if (button7['text'] == 'O' or button7['text'] == ' ' and button8['text'] == 'O' or
			button8['text'] == ' '):
			button9_ways_to_win += 1
		
		if (button3['text'] == 'O' or button3['text'] == ' ' and button6['text'] == 'O' or
			button6['text'] == ' '):
			button9_ways_to_win += 1
			
		if (button1['text'] == 'O' or button1['text'] == ' ' and button5['text'] == 'O' or
			button5['text'] == ' '):
			button9_ways_to_win += 1
	
		if button9_ways_to_win > max_ways_to_win:
			max_ways_to_win = button9_ways_to_win
			choice = 'button9'
	#***********************************************************************************************************************************************************************************************
				
	#section 2 (higher importance)
	#this section focuses on preventing the player from winning
	#***********************************************************************************************************************************************************************************************
	if button1['text'] == ' ': #as always, the square must be empty so that we can consider it for a move	
		if (button2['text'] == 'X' and button3['text'] == 'X' or button4['text'] == 'X' and 
			button7 == 'X' or button5['text'] == 'X' and button9['text'] == 'X'):	#all we do is search for two X's in a row, in other words, we're looking for where 
			choice = 'button1'														#the human player is likely to make a winning move and stop him
																					#choices made in this section override the previous section
	if button2['text'] == ' ':
		if (button1['text'] == 'X' and button3['text'] == 'X' or
			button5['text'] == 'X' and button8['text'] == 'X'):
			choice = 'button2'
	
	if button3['text'] == ' ':
		if (button1['text'] == 'X' and button2['text'] == 'X' or button5['text'] == 'X' and 
			button7['text'] == 'X' or button6['text'] == 'X' and button9['text'] == 'X'):
			choice = 'button3'
	
	if button4['text'] == ' ':
		if (button1['text'] == 'X' and button7['text'] == 'X' or button5['text'] == 'X' and
			button6['text'] == 'X'):
			choice = 'button4'
			
	if button5['text'] == ' ':
		if (button1['text'] == 'X' and button9['text'] == 'X' or button3['text'] == 'X' and
			button7['text'] == 'X' or button2['text'] == 'X' and button8['text'] == 'X' or
			button4['text'] == 'X' and button6['text'] == 'X'): 
			choice = 'button5'
					
	if button6['text'] == ' ':
		if (button3['text'] == 'X' and button9['text'] == 'X' or button4['text'] == 'X' and
			button5['text'] == 'X'):
			choice = 'button6'
			
	if button7['text'] == ' ':
		if (button1['text'] == 'X' and button4['text'] == 'X' or button5['text'] == 'X' and
			button3['text'] == 'X' or button8['text'] == 'X' and button9['text'] == 'X'):
			choice = 'button7'
			
	if button8['text'] == ' ':
		if (button5['text'] == 'X' and button2['text'] == 'X' or button9['text'] == 'X' and
			button7['text'] == 'X'):
			choice = 'button8'
			
	if button9['text'] == ' ':
		if (button7['text'] == 'X' and button8['text'] == 'X' or button3['text'] == 'X' and
			button6['text'] == 'X' or button1['text'] == 'X' and button5['text'] == 'X'):
			choice = 'button9'
	#***********************************************************************************************************************************************************************************************
	
	#section 3 (highest importance)
	#has the AI look for winning moves
	#***********************************************************************************************************************************************************************************************
	if button1['text'] == ' ': #the square must still be empty for move consideration	
		if (button2['text'] == 'O' and button3['text'] == 'O' or button4['text'] == 'O' and 
			button7 == 'O' or button5['text'] == 'O' and button9['text'] == 'O'): #the only difference between this section and the last is that we're checking for where there are two O's in a row
			choice = 'button1'													  #in other words, we're looking for a finishing move
																				  #choices made in this section override the previous two sections
	if button2['text'] == ' ':
		if (button1['text'] == 'O' and button3['text'] == 'O' or
			button5['text'] == 'O' and button8['text'] == 'O'):
			choice = 'button2'
	
	if button3['text'] == ' ':
		if (button1['text'] == 'O' and button2['text'] == 'O' or button5['text'] == 'O' and 
			button7['text'] == 'O' or button6['text'] == 'O' and button9['text'] == 'O'):
			choice = 'button3'
	
	if button4['text'] == ' ':
		if (button1['text'] == 'O' and button7['text'] == 'O' or button5['text'] == 'O' and
			button6['text'] == 'O'):
			choice = 'button4'
			
	if button5['text'] == ' ':
		if (button1['text'] == 'O' and button9['text'] == 'O' or button3['text'] == 'O' and
			button7['text'] == 'O' or button2['text'] == 'O' and button8['text'] == 'O' or
			button4['text'] == 'O' and button6['text'] == 'O'): 
			choice = 'button5'
				
	if button6['text'] == ' ':
		if (button3['text'] == 'O' and button9['text'] == 'O' or button4['text'] == 'O' and
			button5['text'] == 'O'):
			choice = 'button6'
	
	if button7['text'] == ' ':
		if (button1['text'] == 'O' and button4['text'] == 'O' or button5['text'] == 'O' and
			button3['text'] == 'O' or button8['text'] == 'O' and button9['text'] == 'O'):
			choice = 'button7'
		
	if button8['text'] == ' ':
		if (button5['text'] == 'O' and button2['text'] == 'O' or button9['text'] == 'O' and
			button7['text'] == 'O'):
			choice = 'button8'
			
	if button9['text'] == ' ':
		if (button7['text'] == 'O' and button8['text'] == 'O' or button3['text'] == 'O' and
			button6['text'] == 'O' or button1['text'] == 'O' and button5['text'] == 'O'):
			choice = 'button9'
	#***********************************************************************************************************************************************************************************************
	
	#tell our AI which choice was decided on
	opponentMove(choice)
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________



#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________

#assign opponent's move to the board
def opponentMove(choice):
	if choice == 'button1':
		button1['text'] = 'O'
	elif choice == 'button2':
		button2['text'] = 'O'
	elif choice == 'button3':
		button3['text'] = 'O'
	elif choice == 'button4':
		button4['text'] = 'O'
	elif choice == 'button5':
		button5['text'] = 'O'
	elif choice == 'button6':
		button6['text'] = 'O'
	elif choice == 'button7':
		button7['text'] = 'O'
	elif choice == 'button8':
		button8['text'] = 'O'
	elif choice == 'button9':
		button9['text'] = 'O'
	
	winCheck()
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________
	
	
	
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________	

#checks if the game has been won by either the player, the AI, or the cat
def winCheck():
	#check rows for player win
	if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or 
	   button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
	   button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or 
	   
	   #check columns for player win
	   button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
	   button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or 
	   button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or
	   
	   #check diagonals for player win
	   button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
	   button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):
		
		#display winning message and reset the board
		tkMessageBox.showinfo('WINNER!', 'Congratulations, you won the game!')
		gameRunning = False
		newGame()
		
	#check rows for opponent win
	elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or 
	   button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
	   button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or 
	   
	   #check columns for opponent win
	   button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
	   button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or 
	   button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or
	   
	   #check diagonals for opponent win
	   button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
	   button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'):
		
		#display losing message and reset the board
		tkMessageBox.showinfo('LOSER!', 'Congratulations, you lost the game! :D')
		gameRunning = False
		newGame()
		
	#check to see if the 'cat' won
	#this is done by checking to see if every square is filled with either an X or an O
	elif ((button1['text'] == 'X' or button1['text'] == 'O') and (button2['text'] == 'X' or 
		  button2['text'] == 'O') and (button3['text'] == 'X' or button3['text'] == 'O') and
		  (button4['text'] == 'X' or button4['text'] == 'O') and (button5['text'] == 'X' or
		  button5['text'] == 'O') and (button6['text'] == 'X' or button6['text'] == 'O') and
		  (button7['text'] == 'X' or button7['text'] == 'O') and (button8['text'] == 'X' or 
		  button8['text'] == 'O') and (button9['text'] == 'X' or button9['text'] == 'O')):
		
		#display cat message and reset the board
		tkMessageBox.showinfo('MEOW!', "The invisible cat won! Cats are pretty good at this game!")
		gameRunning = False
		newGame()
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________
		
		

#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________		

#resets the board when the game is over		
def newGame():
	button1['text'] = ' '
	button2['text'] = ' '
	button3['text'] = ' '
	button4['text'] = ' '
	button5['text'] = ' '
	button6['text'] = ' '
	button7['text'] = ' '
	button8['text'] = ' '
	button9['text'] = ' '
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________



#set up all of our buttons for the game
button1 = Button(master, text = ' ', width = 5, height = 2, command = lambda:playerMove(button1))
button1.grid(row = 0, column = 0)

button2 = Button(master, text = ' ', width = 5, height = 2, command = lambda:playerMove(button2))
button2.grid(row = 0, column = 1)

button3 = Button(master, text = ' ', width = 5, height = 2, command = lambda:playerMove(button3))
button3.grid(row = 0, column = 2)

button4 = Button(master, text = ' ', width = 5, height = 2, command = lambda:playerMove(button4))
button4.grid(row = 1, column = 0)

button5 = Button(master, text = ' ', width = 5, height = 2, command = lambda:playerMove(button5))
button5.grid(row = 1, column = 1)

button6 = Button(master, text = ' ', width = 5, height = 2, command = lambda:playerMove(button6))
button6.grid(row = 1, column = 2)

button7 = Button(master, text = ' ', width = 5, height = 2, command = lambda:playerMove(button7))
button7.grid(row = 2, column = 0)

button8 = Button(master, text = ' ', width = 5, height = 2, command = lambda:playerMove(button8))
button8.grid(row = 2, column = 1)

button9 = Button(master, text = ' ', width = 5, height = 2, command = lambda:playerMove(button9))
button9.grid(row = 2, column = 2)



master.mainloop()
