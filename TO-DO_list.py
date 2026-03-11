while True:
    print("1 Add task")
    print("2 Show tasks")
    print("3 Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")

        with open("tasks.txt", "a") as file:
            file.write(task + "\n")

        print("Task added")

    elif choice == "2":
        with open("tasks.txt", "r") as file:
            tasks = file.read()

        print("Tasks:")
        print(tasks)

    elif choice == "3":
        print("Bye")
        break