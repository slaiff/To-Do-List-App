#Microservice which allows communication via main program using .txt files
#Allows Editing and deleting 
#imports
import time
#class definition for our tasks array
class Task:
	def __init__(self, title, dueDate, importance, status):
		self.title = title
		self.dueDate = dueDate
		self.importance = importance
		self.status = status

	def __str__(self):
        
		return f"{self.title} - {self.dueDate} days until due - {self.importance} importance. - {self.status}"
	
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

def printList(tasks):
	#print the task list + format
	print()
	#print(f"{username}\'s Task List".center(105))
	print("_" * 105)
	print(f"Title".ljust(30), f"Due Date".ljust(25), f"Importance".ljust(25), f"Status".ljust(25))
	print()

	for numTasks, obj in enumerate(tasks, 1): #1 for starting index of enumerate
		if(obj.dueDate == 0 or obj.dueDate == "0"):	#special case of due today
			print(f"{numTasks}.{obj.title}".ljust(30), f"Due today!".ljust(25), f"{obj.importance} importance".ljust(25), f"Status: {obj.status}".ljust(25))
		else:
			print(f"{numTasks}.{obj.title}".ljust(30), f"{obj.dueDate} days until due".ljust(25), f"{obj.importance} importance".ljust(25), f"Status: {obj.status}".ljust(25))
	return numTasks

def deleteTask(tasksList, indexOfRemoval):
	del tasksList[int(indexOfRemoval)]
	writeToFile(tasksList) 

def editTask(index, editedTask):
	#user enters an index in main, prompt them for all the changes in main
	#Must retain list order...
	#HERE we read it from a file, and write over the old line
	editFile = "listenEdit&Del.txt"
	tasksFile = "tasks.txt"
	try:
		with open(editFile, "r") as file:
				lines =  file.readlines()	#read all lines
				if len(lines) >= 3 and lines[0].strip() == "edit":	#ensure 3 lines exist, and "edit" too
						#index = int(lines[1].strip()) - 1			#get index of replacement - file and list[] should match
						#editedTask = lines[2].strip()				#next line should be task to be edited
						print("Beginning edit...")
						try:
							with open(tasksFile, "r") as file:		#read in CURR task file to local []
								taskLines = file.readlines()		
								taskLines[index] = editedTask + "\n"  #modify only the specified line []

							with open(tasksFile, "w") as file:		#open and rewrite the tasks file
								file.writelines(taskLines)

						except FileNotFoundError:
							print("Error: Tasks file not found\n")
	except FileNotFoundError:
		print(f"Error: '{editFile}' not found.")

#updates the file to have updated list once removed 
def writeToFile(tasksList):
	tasksFile = "tasks.txt"
	try:
		with open(tasksFile, "w") as f:
			for task in tasksList:
				f.write(f"{task.title},{task.dueDate},{task.importance},{task.status}\n")
		print("Task list successfully updated in 'tasks.txt'.")
	except FileNotFoundError:
		print(f"Error: Could not find/open {tasksFile}")

#Listening function for both Services (Edit and Delete)
def listen():
	listenFile = "listenEdit&Del.txt"
	
	while True:
		try:
			with open(listenFile, "r") as file:
				lines =  file.readlines()	#read all lines

			if len(lines) < 2:
				#print("Error: Invalid file format.")
				time.sleep(2)
				continue
			
			command = lines[0].strip().lower()
			index = int(lines[1].strip()) - 1  # Convert 1-based to 0-based index

			if command == "edit":
				editedTask = lines[2].strip()
				editTask(index, editedTask)
			elif command == "del":
				tasksList = readFile()
				deleteTask(tasksList, index)
			else:
				print("Error: Unknown command in file.")

			# **Clear the file after processing**
			with open(listenFile, "w") as file:
				pass  # Opening in "w" mode clears the file
		except FileNotFoundError:
			print(f"Error: '{listenFile}' not found.")
			
		time.sleep(2)  # Wait 2 seconds before checking again

#call start
listen()