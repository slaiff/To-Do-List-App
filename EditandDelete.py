#Microservice which allows communication via main program using .txt files
#Allows Editing and deleting 

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

def deleteTask(tasksList):
	printList(tasksList)
	selection =  input("Which task would you like to remove?: ")
	del tasksList[int(selection) - 1]
	printList(tasksList) #rewrite to file

def main():
	tasksList = readFile()
	printList(tasksList)
	deleteTask(tasksList)


#main call
main()

