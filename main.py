#imports

from math import fabs
import sys
import os

#class definition for our tasks array
class Task:
	def __init__(self, title, dueDate, importance, status):
		self.title = title
		self.dueDate = dueDate
		self.importance = importance
		self.status = status

	def __str__(self):
        
		return f"{self.title} - {self.dueDate} days until due - {self.importance} importance. - {self.status}"

def initWrite():
	print("- Task List Builder -")
	print("Created by: Dylan Keyhantaj, 2/9/2025")
	print() #just makes a \n

#welcome function!
def welcome(username, welcomeString):
	instructions = f"""Fill the supplied text file ('tasks.txt') with your tasks in the following shown format, and this app will build you a task list, {username}!

		Example format for .txt file: 
					(Title, Days till Due, Importance, Status)

					Prepare Thesis for WR122,7,low, Incomplete
					Message Ruth about team meeting,2,medium, Incomplete
					Walk Brody,0,high, Complete

	"""
	print(instructions)
	userInput = input(welcomeString).lower()
	return userInput

#quit function
def goodbye():
	confirmMssg = """
	"Are you sure you want to close the app? Please note your progress will *not* be saved to file,
	and all progress will be lost. If you wish to save, please take note of your additions, changes, etc
	and add these to your text file before closing.
	"""
	print(confirmMssg)
	userConfirm = input("Close app? 'y' or 'n' > ").lower()
	if(userConfirm in ['y']):
		goodbye = """
		Thank you for using Task List Builder! I hope it helped you with your schedule!
				Have a good day :)
		"""
		print(goodbye)
		sys.exit(0)
	else:
		print("Going back...")
		userConfirm = 'n'

	return userConfirm

#open file function
def readFile():
	tasksList = [] #init an empty list (array) 
	file = "tasks.txt"

	#using a nested loop to interate through the text file-
	#pulling line by line, stripping for whitespace, sorting into a local object-
	#then stripping and splitting each piece into a new class Task object and 
	#loading into list
	with open(file, 'r') as file:	#'with' ensures file is automatically closed, even upon error!
		for line in file:
			partsOfLine = line.strip().split(',')	#splits by delimter into indexed pieces
			title = partsOfLine[0].strip()	#set's title to first piece and strips away any whitespace
			dueDate = int(partsOfLine[1].strip()) #'int' encapsulation converts input to integer
			importance = partsOfLine[2].strip() 
			status = partsOfLine[3].strip()

			#build object - like passing to a function, which is our class
			tasksList.append(Task(title, dueDate, importance,status)) 

	return tasksList #returns array of tasks called 'tasks'

#home menu 
def homeMenu(tasksList, username, welcomeString):
	print()
	userInput1 = input("To keep working, do nothing. To view the Home Menu, enter 'm' >> ")
	userInput2 = str(0)

	message = """
	Select an option from below:

				  Options
		---------------------------
		1. Add a task 
		2. Complete a task
		3. Build a new task list from file
		4. Print task list
		5. Close app
		Want more info? Enter 'more'

Select >> : """
	if(userInput1 == "m"):
		userInput2 = input(message)
	if(userInput2 == "1"):
		#call add
		os.system('cls') #clear screen 
		addTask(tasksList, username)
	if(userInput2 == "2"):
		#call complete
		os.system('cls') #clear screen 
		completeTask(tasksList, username)
	if(userInput2 == "3"):
		#call re-build
		os.system('cls') #clear screen 
		rebuild()
	if(userInput2 == "4"):
		#call print
		os.system('cls') #clear screen 
		printList(tasksList, username)
	if(userInput2 == "5"):
		#call goodbye
		os.system('cls') #clear screen 
		userConfirm = goodbye()
		if(userConfirm in ['n']):
			userInput2 = "1"
	if(userInput2 == "more"):
		moreInfo()
	return userInput2

#allows user to add a task to their list
def addTask(tasks,username):
	importance = """Importance (select one):
	1. Low
	2. Medium
	3. High
	<< : """
	print()
	print("Fill-in the following".center(40))
	print("_" * 40)
	title = input("Task name: ")
	dueDate = input("Days till due (a number): ")
	importance = input(importance)
	while importance not in ["1","2","3"]:
		print("Invalid input, please select 1,2, or 3.")
		importance = input(">> : ")
	if importance == "1":
		importance = "Low"
	if importance == "2":
		importance = "Medium"
	if importance == "3":
		importance = "High"

	status = input("Completion status (C for complete/I for incomplete): ").lower()
	while status not in ["I", "C", "i", "c"]:
		print("Invalid input for status, please input I or C : ")
		status = input(">> : ").lower()
	if status == "i":
		status = "Incomplete"
	if status == "c":
		status = "Complete"
	tasks.append(Task(title, dueDate, importance, status)) 
	os.system('cls') #clear screen
	printList(tasks,username)

def completeTask(tasks, username):
	print()
	print("Complete one of your tasks below: ")
	numTasks = printList(tasks, username) #numTasks gathered
	
	while True:
		userInput = input("Select << : ")
		#userInput = int(userInput)

		if userInput.isdigit() and 1 <= int(userInput) <= numTasks:
			task = tasks[int(userInput) - 1];
			confirmInput = input(f"Are you sure you want to complete << {task.title} >> ?\nEnter 'y' for yes, 'n' for no: ").lower()
			if(confirmInput == "y"):
				os.system('cls')
				print(f"<< {task.title} >>  - Completed")
				task.status = "Complete"
				printList(tasks, username)
				break
			else:
				print("Task not completed")
				break
		else:
			print("Not a valid selection, try again.")

def rebuild():
	os.system('cls') #clear screen
	main()
	
def moreInfo():
	os.system('cls') #clear screen
	print("Here is some more info about this app's features!\n")
	moreInfoPara = """
	For 1) 'Add a task', lets you add a task you think of later on or forgot to add to your file!
		1a) Simply requires a title, due date, level of importance, and the status (completed/uncompleted)
			(Title -> name of your task, Due date -> how many days until this is due, 
			Level of importance -> low, medium, high level of importance, 
			Status -> if your task is completed or uncompleted)
	For 2) 'Complete a task', allows you to mark a current task as completed!
		2a) Asks you to pick a task based on it's index, confirms, and marks it as complete. 
	For 3) 'Build a new task list from file', lets you reset the app back to the start.
		3a) It will restart the program and reload your text file, so if you want to make any modifications, 
			add any new information, etc, this is a great option. 
	For 4)	'Print Task List', displays the current task list to terminal, for your viewing pleasure :)
	For 5)	'Close App', shuts down the app, your file will not be deleted upon exit :)

	For any further inquiries, visit our totally exisiting website -> www.weDontHaveAWebsite.com/lol 
	"""
	print(moreInfoPara)
	print()
	input("When ready, press Enter to return back to the home page...")
	#while True:
		#userInput = input("When ready, enter 'r' or 'R' to return back to the home page: ").strip().lower()
		#if userInput == 'r' :
			#os.system('cls')
			#userRequest = welcome(username, welcomeString)
			#return userRequest


def printList(tasks, username):
	#print the task list + format
	print()
	print(f"{username}\'s Task List".center(105))
	print("_" * 105)
	print(f"Title".ljust(30), f"Due Date".ljust(25), f"Importance".ljust(25), f"Status".ljust(25))
	print()

	for numTasks, obj in enumerate(tasks, 1): #1 for starting index of enumerate
		if(obj.dueDate == 0 or obj.dueDate == "0"):	#special case of due today
			print(f"{numTasks}.{obj.title}".ljust(30), f"Due today!".ljust(25), f"{obj.importance} importance".ljust(25), f"Status: {obj.status}".ljust(25))
		else:
			print(f"{numTasks}.{obj.title}".ljust(30), f"{obj.dueDate} days until due".ljust(25), f"{obj.importance} importance".ljust(25), f"Status: {obj.status}".ljust(25))
	return numTasks



#main function!
def main():
	#print claimage and date
	initWrite()
	#gather username
	username = input("Welcome! Could I get your name? >> ")
	print()
	#welcome user
	print(f"Thanks, good to meet you, {username} :) \n")

	#Welcome string and message
	welcomeString = """
	Got the file ready? Enter 'start' (or 's') to begin! - don't worry, you can add tasks later if you forget one ;)
	Want some more info? Enter 'more'
	Changed your mind? Enter 'quit' or 'q' to exit.
	>  """
	userInput = welcome(username, welcomeString)
	
	while True:
		if userInput in ['start', 's']:
			tasksList = readFile()
			printList(tasksList, username)
			break  # Move to the main loop
		elif userInput == 'more':
			moreInfo() #shows more info page
		elif userInput in ['quit' , 'q']:
			userInput2 = goodbye()
			if(userInput2 in ['n']):
				userInput2 = "1"
			else:
				userInput2 = "5"
		else:
			print()
			print("Invalid input. Please enter 'start', 'more', or 'quit'.")

		# Prompt again if invalid input
		userInput = input(welcomeString).strip().lower()
		
	  # Main loop for home menu
	while True:
		userInput2 = homeMenu(tasksList, username, welcomeString)
		if userInput2 == "5":
			break
	#afterloop
	goodbye()
	sys.exit(0)

#call main
main()