#Imports
import time
import os

#Globals
listenFile = "listenSave&Timer.txt"
timerOutput = "timerOutput.txt"
saveFileName = "tasks.txt"
timerStart = None

# Listen for "save" or "startTimer" commands
def listen():
    global timerStart  #let this func know when we say "timerStart" we mean the global
    while True:
        try:
            with open(listenFile, "r") as file:
                contents = file.read().strip()

            if contents == "save":
                print("Saving...")
                saveFile()
                clearCommand()
            elif contents == "startTimer" and timerStart is None:
                print("Timer Started")
                timerStart = time.time()  # Set start time
                clearCommand()
            elif contents == "endTimer" and timerStart is not None:
                print("Timer Ended")
                printElapsed(timerStart)
                timerStart = None  # Reset timer
                clearCommand()
        except FileNotFoundError:
            print(f"Error: '{listenFile}' not found.")

        time.sleep(0.1)  

# Clears the command after execution
def clearCommand():
    with open(listenFile, "w") as file:
        file.write("")

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
        with open(listenFile, "w") as file:
            file.write("done")           
        print("Task list successfully updated in 'tasks.txt'.")
        
    except Exception as e:
        print(f"Error updating file: {e}")


def printElapsed(startTime):
    elapsedTime = (time.time() - startTime) / 60  # Convert to minutes
    formattedTime = f"{elapsedTime:.2f}"

    with open("timerOutput.txt", "w") as file:
        file.write(formattedTime)
        file.flush()  # Ensure immediate write
        os.fsync(file.fileno())  # Force OS to sync to disk

#Begin listen
listen()