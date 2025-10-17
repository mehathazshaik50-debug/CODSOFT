# TO-DO LIST APPLICATION

tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks added yet!\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def remove_task():
    show_tasks()
    try:
        num = int(input("Enter task number to remove: "))
        removed = tasks.pop(num - 1)
        print(f"Task '{removed}' removed!")
    except (ValueError, IndexError):
        print("Invalid task number!")

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")