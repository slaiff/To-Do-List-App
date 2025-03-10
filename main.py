#imports
#globals?
timerOn = 0
from math import fabs
import sys
import os
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

#Prints program header/credits
def initWrite():
    print("- Task List Builder -")
    print("Created by: Dylan Keyhantaj - \u00A9 2025")  #encoding for copyright symbol
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

#Rewrites the tasks file in original format with current list
def updateFile(tasksList):
    file = "tasks.txt"
    try:
        with open(file, 'w') as f:
            for task in tasksList:
                f.write(f"{task.title},{task.dueDate},{task.importance},{task.status}\n")
        print("Task list successfully updated in 'tasks.txt'.")
    except Exception as e:
        print(f"Error updating file: {e}")

#Home menu of program
def homeMenu(tasksList, username, welcomeString):
    print()
    userInput1 = input("To keep working, do nothing. To view the Home Menu, enter 'm' >> ")
    userInput2 = str(0)

    message = """
    Select an option from below:

                  Options
        ---------------------------
        1. Add a task 
        2. Edit a task
        3. Complete a task
        4. Remove a task
        5. Display the task list
        6. Begin / End Timer
        7. Sort the task list- FIXME
        8. Save to file - WIP
        9. Rebuild a new task list - from file
        E. Close app
        Want more info? Enter 'more'

Select >> : """
    if(userInput1 == "m"):
        userInput2 = input(message)
    if(userInput2 == "1"):
        os.system('cls') #clear screen 
        addTask(tasksList, username)
    if(userInput2 == "2"):
        os.system('cls')
        wakeEditMS(tasksList, username)
    if(userInput2 == "3"):
        os.system('cls') #clear screen 
        completeTask(tasksList, username)
    if(userInput2 == "4"):
        os.system('cls')
        updateFile(tasksList)
        printList(tasksList, username)
        wakeEditAndDeleteMS(tasksList)
        time.sleep(3)
        tasksList = readFile()
        print("Updated list:\n")
        printList(tasksList,username)
    if(userInput2 == "5"):
        os.system('cls') #clear screen 
        printList(tasksList, username)
    if(userInput2 == "6"):
        os.system('cls')
        print("waking timer..\n")
        wakeTimerMS()
    if(userInput2 == "7"):
        os.system('cls')
        print("waking sort..\n")
        wakeSortMS()
    if(userInput2 == "8"): 
        os.system('cls')
        print("waking save..\n")
        wakeSaveMS()
    if(userInput2 == "9"):
        os.system('cls')
        rebuild()
    if(userInput2 == "E"):
        #call goodbye
        os.system('cls') #clear screen 
        print("Updating file...\n")
        updateFile(tasksList)
        userConfirm = goodbye()
     
        if(userConfirm in ['n']):
            userInput2 = "1"
    if(userInput2 == "more"):
        moreInfo()
    return userInput2

#Add a task to current list[]
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

#Complete Tasks in list[]
def completeTask(tasks, username):
    print()
    print("Complete one of your tasks below: ")
    numTasks = printList(tasks, username) #numTasks gathered
    
    while True:
        userInput = input("Select << : ")

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




#data = [["D", "0", "High", "Incomplete"], ["C", "2", "Low", "Incomplete"], ["B", "5", "Medium", "Incomplete"],
       # ["A", "4", "High", "Incomplete"]]

#Function which interacts w/ Sorting Microservice
def wakeSortMS():
    #save current file contents
    data = [] 
    with open("tasks.txt", "r") as file:
         data = [line.strip().split(", ") for line in file]

    print(data)

    #Write the user's desired command / overwrites ALL CONTEnts
    with open("tasks.txt", "w") as file:
        file.write("D") #FIXME SHOULD BE USER INPUT

    time.sleep(4)

    #Check if microservice is done -> "receives"
    with open("tasks.txt", "r+") as file:
        confirmation = file.read()
        if confirmation == "Received":
            delimiter = ","
            with open("tasks.txt", "w") as file:
                #REWRITE to file
                for row in data:
                    line = delimiter.join(row) + "\n"
                    file.write(line)

    time.sleep(10)

    #After waiting, load back in the sorted list
    todo_list = []  # storage for delimited txt file --> list[list[str]]
    with open("tasks.txt", "r") as r_file:
            task = r_file.readlines()
            mylist = []
            for y in [x.split(',') for x in task]:
                for z in y:
                    mylist.append(z.replace('\n', ''))
            for i in range(0, len(mylist), 4):
                todo_list.append(mylist[i:i + 4])
    with open("tasks.txt", "w") as file:
        file.write("")
    print(todo_list)   

#Reset's program to start
def rebuild():
    os.system('cls') #clear screen
    main()
   
#Provides more info on program features - NEEDS UPDATING FIXME
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

#Display contents of current tasks list[]
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

#Wakes/Signals the Saving MS
def wakeSaveMS():
    listenFileMS_D = "listeningFileMS-D.txt"
    try:
        with open(listenFileMS_D, "w") as file:
            file.write("save")
    except FileNotFoundError:
        print("ERROR: Could not find the listening file for the Save feature MicroserviceD\n")

def wakeTimerMS():
    global timerOn  #let this func know we're referring to the global var named, timerOn, not def a new one
    listenFileForTimer = "listenTimer.txt"
    try:
        with open(listenFileForTimer, "w") as file:
            if timerOn == 0:
                file.write("startTimer")
                timerOn = 1
            else:
                file.write("endTimer")
                timerOn = 0
    except FileNotFoundError:
        print("ERROR: Could not find the listening file for the Timer feature within MicroserviceD\n")

#Wake Edit
def wakeEditMS(tasksList, username):
#File
    listenFileForEdit = "listenEdit.txt"
#ask user for index to edit 
    print()
    print("Select one of your tasks below to edit: ")
    numTasks = printList(tasksList, username) #numTasks gathered

    while True:
        userInput = input("Select << : ")

        if userInput.isdigit() and 1 <= int(userInput) <= numTasks:
            task = tasksList[int(userInput) - 1];
            confirmInput = input(f"Are you sure you want to edit << {task.title} >> ?\nEnter 'y' for yes, 'n' for no: ").lower()
            if(confirmInput == "y"):
                os.system('cls')
                #Prompt for pieces to be re-placed 
                print("For each category of your task, enter an edit or simply press enter to leave it unchanged!\n")
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

                #write the newly built object to the file 
                os.system('cls') #clear screen
                try:
                    with open(listenFileForEdit, 'w') as f:
                        #build object - like passing to a function, which is our class
                        f.write(f"{title},{dueDate},{importance}\n")
                except Exception as e:
                    print(f"Error updating file: {e}")

                print("List updated:\n")
                printList(tasksList, username)
                break
            else:
                print("No tasks selected for editing.")
                break
        else:
            print("Not a valid selection, try again.")



#Wakes delete 
def wakeEditAndDeleteMS(tasksList):
    listenFileForDelete = "listeningFileMS-D.txt"

    userInput = input("Which task would you like to remove?:")

    try:
        with open(listenFileForDelete, "w") as file:
            file.write("del\n")
            file.write(userInput)
    except FileNotFoundError:
        print("ERROR: Could not find the listening file for the Timer feature within MicroserviceD\n")


#Main func - program flow handled here initially-
#-before hand off to homeMenu
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
                userInput2 = "E"
        else:
            print()
            print("Invalid input. Please enter 'start', 'more', or 'quit'.")

        # Prompt again if invalid input
        userInput = input(welcomeString).strip().lower()
        
    #Main loop for home menu
    while True:
        userInput2 = homeMenu(tasksList, username, welcomeString)
        if userInput2 == "E":
            break
    #afterloop
    goodbye()
    sys.exit(0)

#call main
main()
