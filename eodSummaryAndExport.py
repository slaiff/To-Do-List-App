#This MS does not need a listen file, as it is only called one time per program run, uses subprocess() in main prog

#do thing
def endOfDaySummary():
    eodSumFile = "endOfDaySummary.txt"
    tasksFile = "tasks.txt"
    try:
        with open(tasksFile, "r") as file:
            #summarize based on tasks file and write 
            linesInFile = file.readlines()    #read all lines 
            numTasks = len(linesInFile)         

            #Check how many tasks where completed
            #Done by summing for each line in file, if when stripped of whitespace, split amongst ','
            #-1, as this is always the final column of a line in text file, == "complete"
            completedCount = sum(1 for line in linesInFile if line.strip().split(",")[-1] == "complete")  

            percentComplete = (completedCount / numTasks) * 100
            
            #Write to file 
            with open(eodSumFile, "w") as file:
                file.write("\n")
                file.write(f"You had a good {numTasks} tasks today.\n")
                if completedCount == numTasks:
                    file.write(f"Wow! Today you completed all {completedCount} of your {numTasks} tasks!, a whoppping {percentComplete} percent!\n")
                if completedCount != numTasks:
                    file.write(f"So far, you've completed {completedCount} of your {numTasks}, a solid {percentComplete} percent!\n")
                file.write(f"Be proud of what you accomplished today!\n")
                #print completed stuff
                file.write("Your Tasks: \n")
                file.write("----------------\n")
                for lines in linesInFile:
                    if lines.strip().split(',')[-1] == "complete":
                        file.write(f"Completed: {lines.strip().split(',')[0]}\n")
                    else:
                        file.write(f"To-Do: {lines.strip().split(',')[0]}\n")




    except FileNotFoundError:
        print("Could not find file...")


#main call func
endOfDaySummary()