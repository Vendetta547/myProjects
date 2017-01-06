"""An automated employee scheduler that graphically displays information using Tkinter. 
   
   Creation of a new employee follows this method:
   emp = Employee(name of employee, number of hours for the week, a boolean list of day availability, a list of start hour availability for each day, a list of end hour availability for each day)
   
   To add an employee to the scheduling list, type: employees.append(emp) after creating the employee object
   
   ELABORATION: Boolean list of day availability - [False, False, True, True, True, True, True] would mean that the employee is available every day except for Sunday and Monday
				List of start hour availability - [0, 0, 8, 8, 10, 15, 9] means that the employee can come in as early as 8 on Tuesday and 10 on Thursday. 0's mean that the employee isn't available that day
				List of end hour availability - [0, 0, 21, 21, 19, 21, 17] works the same way as start hour availability, but is instead information as to how late the employee can work
				
	KNOWN ISSUE(S): Program occasionally schedules an employee for a couple of hours over their allotted amount."""


from Tkinter import *
from random import *

###################################################################################################################################################################################

#the employee class holds all information relevant to the individual employee, such as their name, availability, and number of hours allotted

#methods of the employee class focus on returning details as to the employee's schedule for the current day 
#ex: ensuring that the employee has not been scheduled too early, too late, or for more hours than they're available that day
class Employee:

	#______________________________________________________________________________________________________________________________________________________________________________
	
	#class constructor
	def __init__(self, name, hours, day_availability, start_hour_availability, end_hour_availability):
		self.name = name
		self.hours = hours
		
		self.day_availability = []
		for x in range(0, 7):
			self.day_availability.append(day_availability[x])
		
		self.start_hour_availability = []
		for x in range(0, 7):
			self.start_hour_availability.append(start_hour_availability[x])
			
		self.end_hour_availability = []
		for x in range(0, 7):
			self.end_hour_availability.append(end_hour_availability[x])
			
		self.clock_in_times = []
		for x in range(0, 7):
			self.clock_in_times.append(0)
			
		self.clock_out_times = []
		for x in range(0, 7):
			self.clock_out_times.append(0)
		
		self.hours_can_work = []
		for x in range(0, 7):
			self.hours_can_work.append(end_hour_availability[x] - start_hour_availability[x])
		
		self.workdays = []
		for x in range(0, 7):
			self.workdays.append(False)
	#______________________________________________________________________________________________________________________________________________________________________________
			
	
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#check is the employee is working on a given day
	def isWorking(self, x):
		return self.workdays[x]
	#______________________________________________________________________________________________________________________________________________________________________________



	#______________________________________________________________________________________________________________________________________________________________________________
	
	#check is employee is available to work on a given day
	def isAvailable(self, x):
		return self.day_availability[x]
	#______________________________________________________________________________________________________________________________________________________________________________
	
	
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#check if employee has enough hours left for the shortest shift that can be worked, which in this case is 6 hours
	def hasHours(self):
		return self.hours > 6
	#______________________________________________________________________________________________________________________________________________________________________________	
	
	
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#add up the hours scheduled for each day and return the total 
	#this precaution is implemented in case the system accidentally schedules an hour or two over, that way the display is still accurate
	def determineScheduledHours(self):
		scheduled_hours = 0
		for x in range(0, 7):
			if self.isWorking(x):
				scheduled_hours += (self.clock_out_times[x] - self.clock_in_times[x])
		
		return scheduled_hours
	#______________________________________________________________________________________________________________________________________________________________________________
	
	
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#check if the employee is coming in too early, staying too late, or working more hours than their availability for that day
	def shiftNotWithinAvailability(self, day):
		return self.clock_in_times[day] < self.start_hour_availability[day] or self.clock_out_times[day] > self.end_hour_availability[day] or self.clock_out_times[day] - self.clock_in_times[day] > self.hours_can_work[day]
	#______________________________________________________________________________________________________________________________________________________________________________
	
	
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#check if the employee is working too many hours on a given day
	def workingTooManyHours(self, day):
		return self.clock_out_times[day] - self.clock_in_times[day] > self.hours_can_work[day]
	#______________________________________________________________________________________________________________________________________________________________________________
	
	
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#check if the employee is coming in too late in the day to work at least a 6 hour shift
	def comingInTooLate(self, day):
		return self.end_hour_availability[day] - self.clock_in_times[day] < 6
	#______________________________________________________________________________________________________________________________________________________________________________	
	
	
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#check if the employee is scheduled for earlier than they can be at work
	def comingInTooEarly(self, day):
		return self.clock_in_times[day] <= self.start_hour_availability[day]
	#______________________________________________________________________________________________________________________________________________________________________________
	
	
	
	#______________________________________________________________________________________________________________________________________________________________________________	
	
	#check if the employee is scheduled for later than they can stay at work
	def stayingTooLate(self, day):
		return self.clock_out_times[day] >= self.end_hour_availability[day]
	#______________________________________________________________________________________________________________________________________________________________________________


	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#check if there is room to add more hours to an employee's schedule for the day
	def hasHoursLeftForDay(self, day):
		return self.clock_out_times[day] - self.clock_in_times[day] > self.hours_can_work[day]
	#______________________________________________________________________________________________________________________________________________________________________________
	
###################################################################################################################################################################################		
		
		
		
###################################################################################################################################################################################	
	
class Schedule:

	#______________________________________________________________________________________________________________________________________________________________________________
	
	#class constructor 
	def __init__(self, employees):
		self.employees = []
		for x in range(0, len(employees)):
			self.employees.append(employees[x])
			
		self.shifts = [6, 7, 8, 9, 10, 11, 12]
		
		self.days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
	#______________________________________________________________________________________________________________________________________________________________________________
	
	
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#starts the chain of function calls that begin with assignDays
	#after getting all the data in place, it goes ahead and prints everything
	def generateSchedule(self):
		self.assignDays()
		self.printScheduleGUI()
	#______________________________________________________________________________________________________________________________________________________________________________	
	
	
	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#assigns workdays to the employee
	def assignDays(self):
		for employee in self.employees:					#for each employee
			for x in range(0, 7):						#check each of the seven days
				assign_day = randint(1, 3)				#randomly decide whether or not to schedule them
				if assign_day == 1:
					pass
				else:
					if employee.isAvailable(x) and not employee.isWorking(x) and employee.hasHours():		#if the employee can work that day, is not already scheduled, and has enough hours for the shortest shift
								employee.workdays[x] = True													#schedule them for that day, then go ahead and assign them a shift for that day
								self.addHours(x, employee)
			
			
			#if the employee still has hours after cycling through all the days, 
			#go back and add extra days where needed
			if employee.hasHours():								
				self.addExtraDay(employee)
				
		#go back through each day and tack on the remaining hours to already assigned shifts
		self.fineTuneHours()
	#______________________________________________________________________________________________________________________________________________________________________________	
		
		
		
	#______________________________________________________________________________________________________________________________________________________________________________	
	
	#assigns out the last remaining few hours that weren't caught by any other of the main functions
	#this function is why our scheduled hour count is so accurate in the end
	def fineTuneHours(self):
		for employee in employees:										#go through each employee and check each day for them (make sure that they're scheduled to work on that day, too)
			for x in range(0, 7):										#if they're not coming in too early, make them come in earlier until the earliest time possible is reached
				if employee.isWorking(x):								#do the same thing with the time they're supposed to be leaving
					while employee.hours > 0:							#at the end, adjust the hours accordingly
						if not employee.comingInTooEarly(x):
							employee.clock_in_times[x] -= 1
							employee.hours -= 1
							
						if not employee.stayingTooLate(x):
							employee.clock_out_times[x] += 1
							employee.hours -= 1
							
						if employee.clock_out_times[x] - employee.clock_in_times[x] == employee.hours_can_work[x]:		#break out early if they've reached the max hours they can work that day
							break
				
			if employee.hasHours():
				self.addExtraDay(employee)		
	#______________________________________________________________________________________________________________________________________________________________________________
	
	
	
	#______________________________________________________________________________________________________________________________________________________________________________			
	
	#add extra days to an employee's schedule if hours come up short the first time through the scheduler
	def addExtraDay(self, employee):
		for x in range(0, 7):
			if employee.hasHours():
				if employee.isAvailable(x) == True and employee.isWorking(x) == False:
					employee.workdays[x] = True
					self.addHours(x, employee)
	#______________________________________________________________________________________________________________________________________________________________________________
	

	
	#______________________________________________________________________________________________________________________________________________________________________________	
	
	#assign a work shift to an employee on a given day
	def addHours(self, day, employee):
			
		if employee.isWorking(day):
		
			if employee.hasHours():
			
				clock_in_time = randint(employee.start_hour_availability[day], employee.end_hour_availability[day])				#randomize the starting hour of the shift
				shift_time = randint(0, 6)																						#randomly choose how long the shift is
				clock_out_time = clock_in_time + self.shifts[shift_time]														#obviously, an employee clocks out at the end of their shift
				
				employee.clock_in_times[day] = clock_in_time												
				employee.clock_out_times[day] = clock_out_time
				
					
				while employee.shiftNotWithinAvailability(day):			#check if we've scheduled the employee too early, too late, or for too long
					if employee.comingInTooEarly(day):					#then adjust the shift times accordingly
						employee.clock_in_times[day] += 1
						
					if employee.comingInTooLate(day):
						employee.clock_in_times[day] -= 1
						
					if employee.stayingTooLate(day):
						employee.clock_out_times[day] -= 1
					
					if employee.workingTooManyHours(day):				#if the employee is working too many hours for a particular day, reduce the shift time
						shift_time -= 1
				
				employee.hours -= (employee.clock_out_times[day] - employee.clock_in_times[day])		#then adjust the hours left after the shift is settled
	#______________________________________________________________________________________________________________________________________________________________________________						


	
	#______________________________________________________________________________________________________________________________________________________________________________
	
	#used for debugging purposes
	'''
	def printScheduleCommandLine(self):
		for employee in self.employees:
			print employee.name
			print 'WORKDAYS'
			for x in range(0, 7):
				if employee.isWorking(x):
					print self.days[x], 'from', employee.clock_in_times[x], 'to', employee.clock_out_times[x], '\n'
	'''
	#______________________________________________________________________________________________________________________________________________________________________________			

	
	
	#______________________________________________________________________________________________________________________________________________________________________________

	#graphically displays the scheduling information
	def printScheduleGUI(self):
		
		#make the employee and hours header
		Label(master, text = "Employee", width = 20, padx = 5).grid(row = 0, column = 0)
		Label(master, text = "Hours", width = 20, padx = 5).grid(row = 0, column = 8)
		
		#print the employees' names
		rowcount = 1
		for employee in employees:
			Label(master, text = employee.name, width = 20, padx = 5).grid(row = rowcount, column = 0)
			rowcount += 1
		
		#print the days of the week header
		for x in range(0, 7):
			Label(master, text = self.days[x], width = 20, padx = 5).grid(row = 0, column = x + 1)
		
		#print work times
		rowcount = 1
		for employee in employees:
			for x in range(0, 7):
				if employee.isWorking(x):
					Label(master, text = str(employee.clock_in_times[x]) + ' - ' + str(employee.clock_out_times[x]), width = 20, padx = 5).grid(row = rowcount, column = x + 1)
				else:
					Label(master, text = 'Off', width = 20, padx = 5).grid(row = rowcount, column = x + 1)
			rowcount += 1
		
		#print total hours working in the last column
		rowcount = 1
		for employee in employees:
			Label(master, text = str(employee.determineScheduledHours()), width = 20, padx = 5).grid(row = rowcount, column = 8)
			rowcount += 1
		
		#this button's original purpose was to generate new schedules from within the GUI window
		#Button(master, text = "New Schedule", command = self.generateSchedule).grid(row = len(self.employees) + 1, column = 4)
	#______________________________________________________________________________________________________________________________________________________________________________
	
###################################################################################################################################################################################		
			
employees = []	



master = Tk()
master.title = ('Schedule Generator')
master.geometry = ('500x500')


#create employee objects		
john = Employee('John', 40, [False, True, True, True, True, True, True], [0, 8, 8, 8, 15, 12, 8], [0, 21, 21, 18, 21, 21, 19]) 
						   					   
sam = Employee('Sam', 40, [True, False, False, True, True, True, True], [8, 0, 0, 8, 12, 8, 8], [21, 0, 0, 21, 21, 21, 21])

brittney = Employee('Brittney', 20, [False, False, True, True, True, True, True], [0, 0, 8, 8, 11, 13, 8], [0, 0, 21, 21, 21, 21, 21])			

cindy = Employee('Cindy', 30, [True, True, True, True, True, True, True], [8, 8, 8, 8, 8, 8, 8], [18, 18, 18, 18, 18, 18, 18])					


#append them to an employee list
employees.append(john)
employees.append(sam)
employees.append(brittney)
employees.append(cindy)



schedule = Schedule(employees)



button = Button(master, text = "Generate Schedule", command = schedule.generateSchedule)
button.pack()



master.mainloop()

	
