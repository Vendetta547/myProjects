'''
Dylan Martin
CSC 2950
Term Project Script 3 - Maze Runner
'''

"""A maze solving program. Reads in a map written in a text file, solves it behind the scenes, and then graphically recreates the solution on the screen.
    
   MAP CREATION:
   1's in the text file represent a closed path.
   0's in the text file represent an open path.
   Lowercase c represents the cube which will run the maze.
   Lowercase f represents the marker for the finish line.
   
   Text must be written in a complete square or rectangle.
   A single blank space --only one-- must be left at the end of EVERY line. This is due to the way the data is parsed. If this is not adhered to, then it will throw errors. 
   
    ex:	Valid Map
		 1 f 1 
		 1 0 1 
		 c 0 1 
		 
	ex: Invalid Map
		1 f 
		1 0 1
		c 0 1
	
	ex: Invalid Map (check the space at the end of the lines)
		1 f 1
		1 0 1
		c 0 1
		
	KNOWN ISSUE(S): There have been no error handling mechanisms implemented, so leaving out crucial pieces of map information (the solving cube, the finish line) will more 
					than likely throw errors. The phrase 'more than likely' is used because these scenarios have not been tested.
					
					Also, when creating a map, ensure that the map is actually solvable. That is, make sure there is a path of 0's to the finish line that is traversable by the cube
					at some point. There is currently not a method that checks whether the maze is solvable.
					
					And again, be sure to leave a blank space at the end of every line. Not doing so causes index out of range errors when the program tries to run."""


from Tkinter import *
import tkMessageBox
import random
from time import sleep

########################################################################################################################################################################################################

#the Rectangle class contains all the data attributes necessary for the graphical side of the program 
class Rectangle():

	#______________________________________________________________________________________________________________________________________________________________________________
	
	def __init__(self, canvas, x1, y1, x2, y2, color):
		print 'creating rectangle'
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.color = color
		self.canvas = canvas
		self.rectangle = canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill = color)
	#______________________________________________________________________________________________________________________________________________________________________________
	
	
	
	#______________________________________________________________________________________________________________________________________________________________________________	
	
	#handles the visuals of moving the cube through the maze
	def moveCube(self, moves, x_increment, y_increment):
		for x in range(0, len(moves)):							#go through the move list that solves the maze, and have our cube move in those directions
			if moves[x] == 'right':
				self.xchange = x_increment
				self.ychange = 0
		
			elif moves[x] == 'left':
				self.xchange = -(x_increment)
				self.ychange = 0
				
			elif moves[x] == 'up':
				self.xchange = 0
				self.ychange = -(y_increment)
			
			elif moves[x] == 'down':
				self.xchange = 0
				self.ychange = y_increment
			
			#after passing through the if/elif statements, move the cube in the appropriate direction
			for x in range(10):
				sleep(0.025)
				self.canvas.move(self.rectangle, self.xchange, self.ychange)
				self.canvas.update()
	#______________________________________________________________________________________________________________________________________________________________________________	
		
########################################################################################################################################################################################################



########################################################################################################################################################################################################

#the Map class is the heart of the program, being responsible for the maze solving itself
#Map inherits from Rectangle so that it can graphically draw the maze by creating Rectangle objects on the fly
#the general flow of things is that everything in Map actually solves the maze, and then simply keeps a copy of the moves for the rectangle to follow on the screen
class Map(Rectangle):
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	def __init__(self, filename):
		
		self.mapdata = []
		
		self.move_list = []
		
		self.cube_moves = []
		
		self.backtrack_path = []
		
		self.input = open(filename, 'r')
		lines = self.input.readlines()
		
		self.maprows = 0
		for line in lines:
			self.mapdata.append(line.split(' '))	#splitting the lines makes the map easier to read in the command line
			self.maprows += 1
			
		self.input.close()
							
		for x in range(0, len(self.mapdata)):
			self.mapdata[x].pop(-1)
		
			
		self.cube_index = []
		self.finish_index = []
		
		#find the character index and the finish index. also count the columns along the way
		for x in range(0, len(self.mapdata)):
			self.mapcolumns = 0
			for y in range(0, len(self.mapdata[x])):
				if self.mapdata[x][y] == 'c':
					self.cube_index.append(x)
					self.cube_index.append(y)
				elif self.mapdata[x][y] == 'f':
					self.finish_index.append(x)
					self.finish_index.append(y)
				self.mapcolumns += 1
			
	#______________________________________________________________________________________________________________________________________________________________________________
	

	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#uses the text map data to visually recreate the map with rectangles
	def createRectangleMap(self, canvas):
		#the window size will always be 500, so we take the number of columns and rows into consideration so that we can scale the screen to larger/smaller maps.
		self.xcoord_increment = float(500 / self.mapcolumns) 
		self.ycoord_increment = float(500 / self.maprows) 
		
		ycoord1 = 0
		ycoord2 = self.ycoord_increment
		xcoord1 = 0
		xcoord2 = self.xcoord_increment
		
		#this loop is what's responsible for the actual drawing
		for x in range(0, self.maprows):
			xcoord1 = 0
			xcoord2 = self.xcoord_increment
			for y in range(0, self.mapcolumns):
			
				if self.mapdata[x][y] == 'c': #find the maze solving cube and color it red
					self.player_cube = Rectangle(canvas, xcoord1, ycoord1, xcoord2, ycoord2, 'red')
					
				elif self.mapdata[x][y] == 'f': #find where the finish line cube is and color it blue
					rectangle = Rectangle(canvas, xcoord1, ycoord1, xcoord2, ycoord2, 'blue')
					
				elif self.mapdata[x][y] == '1':
					Rectangle(canvas, xcoord1, ycoord1, xcoord2, ycoord2, 'black')
					
				else:
					#draw nothing
					pass
					
				xcoord1 += self.xcoord_increment
				xcoord2 += self.xcoord_increment
				
			ycoord1 += self.ycoord_increment	
			ycoord2 += self.ycoord_increment
	#______________________________________________________________________________________________________________________________________________________________________________	
	


	#______________________________________________________________________________________________________________________________________________________________________________
	
	#this method sets everything in motion
	#it creates the screen, calls the method that generates the map, solves the map behind the scenes, and then passes the move list into the moveCube method so that it will visually recreate the path it took for us
	def runMaze(self):
		self.master = Tk()

		c = Canvas(self.master, width = 500, height = 500)
		c.pack()

		map.createRectangleMap(c)

		map.printMapData() #comment this line out along with line 176 if you don't want to see the text blocks in the command line
		
		
		while not map.isFinished():
			map.checkSurroundings(False)
			map.printMapData()
		
		#after the map is solved, then we make the cube on screen move
		self.player_cube.moveCube(self.cube_moves, float(self.xcoord_increment / 10), float(self.ycoord_increment / 10))
			
		#print self.cube_moves
	#______________________________________________________________________________________________________________________________________________________________________________
	
	

	#______________________________________________________________________________________________________________________________________________________________________________
	
	#print text mapdata in command line	
	def printMapData(self):
		for x in range(0, len(self.mapdata)):
			print self.mapdata[x]
	#______________________________________________________________________________________________________________________________________________________________________________
	
	
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#check if a path is open to the left
	def openLeft(self):
		return self.mapdata[self.cube_index[0]][self.cube_index[1] - 1] == '0' or self.mapdata[self.cube_index[0]][self.cube_index[1] - 1] == 'f'
	#______________________________________________________________________________________________________________________________________________________________________________

	
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#check if a path is open to the right
	def openRight(self):
		return self.mapdata[self.cube_index[0]][self.cube_index[1] + 1] == '0' or self.mapdata[self.cube_index[0]][self.cube_index[1] + 1] == 'f'
	#______________________________________________________________________________________________________________________________________________________________________________

	
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#check if a path is open above
	def openUp(self):
		return self.mapdata[self.cube_index[0] - 1][self.cube_index[1]] == '0' or self.mapdata[self.cube_index[0] - 1][self.cube_index[1]] == 'f'
	#______________________________________________________________________________________________________________________________________________________________________________

	
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#check if a path is open below
	def openDown(self):
		return self.mapdata[self.cube_index[0] + 1][self.cube_index[1]] == '0' or self.mapdata[self.cube_index[0] + 1][self.cube_index[1]] == 'f'
	#______________________________________________________________________________________________________________________________________________________________________________	
	

	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#checks the surroundings for open paths
	def checkSurroundings(self, isbacktracking):
		self.options = []
		
		if not self.isFinished():
		
			if self.isInTopRow():										#there is a bit of redundancy further down this function, for some code gets repeated that could have otherwise been consolidated
																		#ex: I check if it is in the top row here and then if it is in the top row AND in the first column. Those same things get checked in reverse order later.		
				if self.isInFirstColumn():								#    However, I've found that a bit of redundancy isn't a bad thing for the nature of this problem. It would be difficult to combine these checks into 
					if self.openRight():								# 	 'and' 'or' 'not' statements and still have the logic turn out correctly. 
						self.options.append('right')
					if self.openDown():
						self.options.append('down')						#all these blocks do is check whether or not I should restrict where my cube looks for open paths, that way the list index doesn't go out 
																		#of range when it searches
				elif self.isInLastColumn():
					if self.openLeft():
						self.options.append('left')
					if self.openDown():
						self.options.append('down')
				
				else:
					if self.openLeft():
						self.options.append('left')
					if self.openRight():
						self.options.append('right')
					if self.openDown():
						self.options.append('down')
						
			elif self.isInLastRow():
				print 'is in last row'
				if self.isInFirstColumn():
					print 'is in first column'
					if self.openUp():
						self.options.append('up')
					if self.openRight():
						print 'is open to the right'
						self.options.append('right')
				
				elif self.isInLastColumn():
					if self.openUp():
						self.options.append('up')
					if self.openLeft():
						self.options.append('left')
				
				else:
					if self.openLeft():
						self.options.append('left')
					if self.openRight():
						self.options.append('right')
					if self.openUp():
						self.options.append('up')
					
				
			elif self.isInFirstColumn():
				
				if self.isInTopRow():
					if self.openRight():
						self.options.append('right')
					if self.openDown():
						self.options.append('down')
					
				elif self.isInLastRow(): 
					if self.openUp():
						self.options.append('up')
					if self.openRight():
						self.options.append('right')
						
				else:
					if self.openRight():
						self.options.append('right')
					if self.openUp():
						self.options.append('up')
					if self.openDown():
						self.options.append('down')
						
				
			elif self.isInLastColumn():
				if self.isInTopRow():
					if self.openLeft():
						self.options.append('left')
					if self.openDown():
						self.options.append('down')
				
				if self.isInLastRow(): 
					if self.openUp():
						self.options.append('up')
					if self.openLeft():
						self.options.append('left')
						
				else:
					if self.openUp():
						self.options.append('up')
					if self.openDown():
						self.options.append('down')
					if self.openLeft():
						self.options.append('left')
					
					
			else:
				if self.openLeft():
					self.options.append('left')
					
				if self.openRight():
					self.options.append('right')
					
				if self.openUp():
					self.options.append('up')
					
				if self.openDown():
					self.options.append('down')
				
			print self.options
			
			if isbacktracking:					#if the cube is backtracking, we don't need to check if we're at a dead end
					pass						#move options here are ignored when backtracking because there is a separate list of backtrack moves that the cube goes by in the situation
			else:
				if self.isDeadEnd():
					self.backtrack()
				else:
					self.move(random.choice(self.options))
					
	#______________________________________________________________________________________________________________________________________________________________________________
		
	
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#move the index to the right
	def moveRight(self):
		print 'moving to the right'
		self.mapdata[self.cube_index[0]][self.cube_index[1]] = 'b'
		self.mapdata[self.cube_index[0]][self.cube_index[1] + 1] = 'c'
		self.updateCubeIndex(self.cube_index[0], self.cube_index[1] + 1)
		self.move_list.append('right')
		self.backtrack_path.append('left')	#append the opposite move to our backtrack list for whenever we hit a dead end
		self.cube_moves.append('right') #whether or not we're backtracking, we append a matching move direction to the cube moves because the backtrack function calls the same movement functions as everything else
	#______________________________________________________________________________________________________________________________________________________________________________

	
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#move the index to the left
	def moveLeft(self):
		print 'moving to the left'
		self.mapdata[self.cube_index[0]][self.cube_index[1]] = 'b'
		self.mapdata[self.cube_index[0]][self.cube_index[1] - 1] = 'c'
		self.updateCubeIndex(self.cube_index[0], self.cube_index[1] - 1)
		self.move_list.append('left')
		self.backtrack_path.append('right')
		self.cube_moves.append('left')
	#______________________________________________________________________________________________________________________________________________________________________________	
	
	
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#check if we're at a dead end 
	def isDeadEnd(self):
		return len(self.options) == 0
	#______________________________________________________________________________________________________________________________________________________________________________	
	
	
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#move the index up
	def moveUp(self):
		print 'moving up'
		self.mapdata[self.cube_index[0]][self.cube_index[1]] = 'b'
		self.mapdata[self.cube_index[0] - 1][self.cube_index[1]] = 'c'
		self.updateCubeIndex(self.cube_index[0] - 1, self.cube_index[1])
		self.move_list.append('up')
		self.backtrack_path.append('down')
		self.cube_moves.append('up')
	#______________________________________________________________________________________________________________________________________________________________________________	
		
		
		
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#move the index down
	def moveDown(self):
		print 'moving down'
		self.mapdata[self.cube_index[0]][self.cube_index[1]] = 'b'
		self.mapdata[self.cube_index[0] + 1][self.cube_index[1]] = 'c'
		self.updateCubeIndex(self.cube_index[0] + 1, self.cube_index[1])
		self.move_list.append('down')
		self.backtrack_path.append('up')
		self.cube_moves.append('down')
	#______________________________________________________________________________________________________________________________________________________________________________	



	#______________________________________________________________________________________________________________________________________________________________________________
	
	#decides which move function to call based on self.options passed in from checkSurroundings
	def move(self, direction):
		if direction == 'right':
			self.moveRight()
			
		elif direction == 'left':
			self.moveLeft()
			
		elif direction == 'up':
			self.moveUp()
			
		elif direction == 'down':
			self.moveDown()
	#______________________________________________________________________________________________________________________________________________________________________________
	
	
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#backtracking method for when dead ends are reached
	def backtrack(self):
		self.backtrack_moves = []
		for x in range(0, len(self.move_list)):
			if self.move_list[x] == 'right':
				self.backtrack_moves.append('left')
			elif self.move_list[x] == 'left':
				self.backtrack_moves.append('right')
			elif self.move_list[x] == 'up':
				self.backtrack_moves.append('down')
			elif self.move_list[x] == 'down':
				self.backtrack_moves.append('up')
		
		self.backtrack_moves.reverse()
		x = 0
		while self.isDeadEnd():
			self.printMapData()
			print 'backtracking'
			if self.backtrack_moves[x] == 'right':
				self.moveRight()
			elif self.backtrack_moves[x] == 'left':
				self.moveLeft()
			elif self.backtrack_moves[x] == 'up':
				self.moveUp()
			elif self.backtrack_moves[x] == 'down':
				self.moveDown()
			self.checkSurroundings(True)
			x += 1
	#______________________________________________________________________________________________________________________________________________________________________________		
		
		
		
	#______________________________________________________________________________________________________________________________________________________________________________	
	
	#updates maze solving cube location in mapdata
	def updateCubeIndex(self, index1, index2):
		self.cube_index[0] = index1
		self.cube_index[1] = index2
		print self.cube_index[0]
		print self.cube_index[1]
	#______________________________________________________________________________________________________________________________________________________________________________	
	
	
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#checks if the cube is in the first column of the map
	def isInFirstColumn(self):
		return self.cube_index[1] == 0
	#______________________________________________________________________________________________________________________________________________________________________________	
	
	
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#checks if the cube is in the top row of the map
	def isInTopRow(self):
		return self.cube_index[0] == 0
	#______________________________________________________________________________________________________________________________________________________________________________	
	
	
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#checks if the cube is in the last column of the map
	def isInLastColumn(self):
		return self.cube_index[1] == self.mapcolumns - 1
	#______________________________________________________________________________________________________________________________________________________________________________	
	
	
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#checks if the cube is in the last row of the map
	def isInLastRow(self):
		return self.cube_index[0] == self.maprows - 1
	#______________________________________________________________________________________________________________________________________________________________________________	
	
	
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#checks if the map has been solved 
	def isFinished(self):
		if self.cube_index == self.finish_index:
			return True
		else:
			return False
	#______________________________________________________________________________________________________________________________________________________________________________
	
########################################################################################################################################################################################################		


#substitute a text file in Map's parameter for any map you may wish to create		
map = Map('bigmap.txt')



map.runMaze()


	
map.master.mainloop()
