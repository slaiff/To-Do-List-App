#Imports
import time

#Globals
saveListenFile = "listeningFileMS-D.txt"
timerListenFile = "listenTimer.txt"

#listen for "save" command in command file
#Try's this, if not (an exception) shows error
def saveListen():
    while True:
        try:
            with open(saveListenFile, "r") as file:
                contents = file.read().strip()
                if contents == "save":
                    print("Saving...")
                    saveFile()  #breaks out
        except FileNotFoundError:
            print(f"Error: '{saveListenFile}' not found.")

        time.sleep(5)  # Wait 5 seconds before checking again

#Opens Task-File (.txt), re-writes it to only contain INCOMPLETE tasks
def saveFile():
    saveFileName = "tasks.txt"
    try:
        with open(saveFileName, 'r') as file:
            lines = file.readlines()

        with open(saveFileName, 'w') as file:
            for line in lines:
                task = line.strip().split(',')
                if len(task) == 4 and task[3].lower() != "complete":  # Ensure correct format and skip completed tasks
                    file.write(line)
        with open(saveListenFile, "w") as file:
            file.write("done")           
        print("Task list successfully updated in 'tasks.txt'.")
        
    except Exception as e:
        print(f"Error updating file: {e}")

def timerListen():
    #loop
    while True:
        try:
            with open(timerListenFile, "r") as file:
                contents = file.read().strip()
                if contents == "startTimer":
                    print("TimerStarted")
                    timerBegin()  #breaks out
        except FileNotFoundError:
            print(f"Error: '{timerListenFile}' not found.")

        time.sleep(2)  # Wait 5 seconds before checking again

def timerBegin():
    startTime = time.time()     #current time, in seconds
    #keep running timer till signaled to end
    while True:
        try:
            with open(timerListenFile, "r") as file:
                contents = file.read().strip()
                if contents == "endTimer":
                    print("TimerEnded")
                    printElapsed(startTime)  #breaks out
        except FileNotFoundError:
            print(f"Error: '{timerListenFile}' not found.")

        time.sleep(2)  # Wait 5 seconds before checking again
    

def printElapsed(startTime):
    elapsedTime = time.time() - startTime   #current time (in sec) minus when we began
    print(f"Elapsed time: {int(elapsedTime)} seconds")

#Begin call flow
#saveListen()
timerListen()