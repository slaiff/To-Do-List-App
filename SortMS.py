import time

while True:
    # Listens for a valid input and writes back a
    # confirmation or denial of service
    with open("tasks.txt", "r") as file:
        message = file.read()
    if message.upper() in ['A','D','P']:
        with open("tasks.txt", "w") as w_file:
            w_file.write("Received")
    else:
        with open("tasks.txt", "w") as w_file:
            w_file.write("Invalid Request")
    time.sleep(10)

    todo_list = []  # storage for delimited txt file --> list[list[str]]
    with open("tasks.txt", "r") as r_file:
        task = r_file.readlines()
        mylist = []
        for y in [x.split(',') for x in task]:
            for z in y:
                mylist.append(z.replace('\n', ''))
        for i in range(0, len(mylist), 4):
            todo_list.append(mylist[i:i+4])

    # Sorts alphabetically
    if message == "A":
        todo_list.sort()
        with open("tasks.txt", "r+") as file:
            delimiter = ","
            with open("tasks.txt", "w") as file:
                for row in todo_list:
                    line = delimiter.join(row) + "\n"
                    file.write(line)

    # Sorts by days until due (soonest to latest)
    if message == "D":
        todo_list.sort(key=lambda x: int(x[1]))
        with open("tasks.txt", "r+") as file:
            delimiter = ","
            with open("tasks.txt", "w") as file:
                for row in todo_list:
                    line = delimiter.join(row) + "\n"
                    file.write(line)

    # Sorts by priority: High -> Medium -> Low
    if message == "P":
        high = []
        med = []
        low = []
        for i in range(0, len(todo_list)):
            if todo_list[i][2] == "High":
                high.append(todo_list[i])
            elif todo_list[i][2] == "Medium":
                med.append(todo_list[i])
            else:
                low.append(todo_list[i])
        high.extend(med)
        high.extend(low)
        with open("tasks.txt", "r+") as file:
            delimiter = ","
            with open("tasks.txt", "w") as file:
                for row in high:
                    line = delimiter.join(row) + "\n"
                    file.write(line)

    time.sleep(5)