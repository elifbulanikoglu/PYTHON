import os

tasks = []

# Load tasks from file at the start of the program
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r", encoding="utf-8") as file:
            for line in file:
                tasks.append(line.strip())

# Save the task list to file
def save_tasks():
    with open("tasks.txt", "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = input("Enter a task: ").strip()
    if task:
        tasks.append(task.capitalize())
        save_tasks()
        print(f"{task} added.\n")
    else:
        print("Empty task cannot be added!\n")

def delete_task():
    if not tasks:
        print("The list is empty. No task to delete.\n")
        return
    show_tasks()
    try:
        to_delete = int(input("Enter the number of the task to delete: "))
        if 1 <= to_delete <= len(tasks):
            deleted = tasks.pop(to_delete - 1)
            save_tasks()
            print(f"{deleted} deleted.\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number.\n")

def clear_all():
    if tasks:
        tasks.clear()
        save_tasks()
        print("List cleared.\n")
    else:
        print("The list is already empty.\n")

def show_tasks():
    print("\n\n--- TO DO LIST ---")
    if not tasks:
        print("The list is empty.\n")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}- {task}")
    print()

def exit_app():
    print("Exiting the program...")

# Load tasks from file at startup
load_tasks()

# Main loop
choice = 0
while choice != 5:
    try:
        print("\n1: Add Task\n2: Delete Task\n3: Show Tasks\n4: Clear All\n5: Exit")
        choice = int(input("Select an option: "))

        if choice == 1:
            add_task()
        elif choice == 2:
            delete_task()
        elif choice == 3:
            show_tasks()
        elif choice == 4:
            clear_all()
        elif choice == 5:
            exit_app()
        else:
            print("Please enter a number between 1 and 5.\n")
    except ValueError:
        print("Please enter a valid number.\n")



