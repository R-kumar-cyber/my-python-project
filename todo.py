tasks = []

while True:
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added.")
    elif choice == "2":
        if not tasks:
            print("No tasks.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
    elif choice == "3":
        print("Exiting.")
        break
    else:
        print("Invalid choice.")