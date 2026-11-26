tasks = []
while True:
    print("1 .Add task")
    print("2. View task")
    print("3. Mark as done")
    print("4. Delete task")
    print("5. Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
        title=input("Enter task name:")
        tasks.append({"title":title,"done" :False})
        print("task added successfully")
    elif choice=="2":
        if len(tasks) ==0:
            print("no task yet")
        else:
            for i,task in enumerate(tasks, start=1):
                if task["done"] == True:
                   status = "[x]"
                else:
                    status = "[ ]"

                    print(i,status,task,["title"])
    elif choice=="3":
        if len(tasks)== 0:
            print("no task to mark as done")
        else:
            for i,task in enumerate(tasks,start=1):
                print(i, task["title"])                            
            number = int(input("Enter task number: "))

            if 1 <= number <= len(tasks):
                tasks[number - 1]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number")
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, task["title"])

            number = int(input("Enter task number to delete: "))

            if 1 <= number <= len(tasks):
                deleted = tasks.pop(number - 1)
                print(deleted["title"], "deleted successfully")
            else:
                print("Invalid task number")
    elif choice == "5":
        completed = 0
        pending = 0

        for task in tasks:
            if task["done"] == True:
                completed += 1
            else:
                pending += 1

        print("Completed tasks:", completed)
        print("Pending tasks:", pending)
        print("Goodbye!")
        break

    else:
        print("Invalid choice")





