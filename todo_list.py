
"Task 1: To-Do List Application"



import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file. Return an empty list if none exist."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_tasks(tasks):
    """Save the tasks list back to the JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def view_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("\nYour to-do list is empty!\n")
        return

    print("\n----- YOUR TO-DO LIST -----")
    for i, task in enumerate(tasks, start=1):
        status = "[X]" if task["done"] else "[ ]"
        print(f"{i}. {status} {task['title']}")
    print("----------------------------\n")


def add_task(tasks):
    """Add a new task to the list."""
    title = input("Enter the new task: ").strip()
    if title == "":
        print("Task cannot be empty.\n")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Task added: '{title}'\n")


def update_task(tasks):
    """Edit the text of an existing task."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter the task number to update: "))
        index = num - 1
        if 0 <= index < len(tasks):
            new_title = input("Enter the new task text: ").strip()
            if new_title:
                tasks[index]["title"] = new_title
                save_tasks(tasks)
                print("Task updated successfully.\n")
            else:
                print("Task text cannot be empty.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def mark_done(tasks):
    """Mark a task as completed."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter the task number to mark as done: "))
        index = num - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks(tasks)
            print("Task marked as done!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def delete_task(tasks):
    """Remove a task from the list."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter the task number to delete: "))
        index = num - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Deleted task: '{removed['title']}'\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def show_menu():
    print("===== TO-DO LIST MENU =====")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Update a task")
    print("4. Mark a task as done")
    print("5. Delete a task")
    print("6. Exit")


def main():
    tasks = load_tasks()
    print("Welcome to your To-Do List App!")

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Goodbye! Your tasks have been saved.")
            break
        else:
            print("Invalid choice. Please pick a number from 1 to 6.\n")


if __name__ == "__main__":
    main()
