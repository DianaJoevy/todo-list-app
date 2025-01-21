def display_menu():
    """Display the menu options."""
    print("\nTo-Do List App")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Mark a Task as Completed")
    print("4. Delete a Task")
    print("5. Exit")

def view_todo_list(todo_list):
    """Display the current to-do list."""
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, 1):
            status = "✓" if task["completed"] else " "
            print(f"{index}. [{status}] {task['name']}")

def add_task(todo_list):
    """Add a new task to the to-do list."""
    task_name = input("Enter the task: ").strip()
    if task_name:
        todo_list.append({"name": task_name, "completed": False})
        print(f"Task '{task_name}' added!")
    else:
        print("Task cannot be empty!")

def mark_task_completed(todo_list):
    """Mark a task as completed."""
    view_todo_list(todo_list)
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(todo_list):
            todo_list[task_number - 1]["completed"] = True
            print(f"Task '{todo_list[task_number - 1]['name']}' marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(todo_list):
    """Delete a task from the to-do list."""
    view_todo_list(todo_list)
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(todo_list):
            deleted_task = todo_list.pop(task_number - 1)
            print(f"Task '{deleted_task['name']}' deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def todo_list_app():
    """Main function to run the To-Do List App."""
    todo_list = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            view_todo_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            mark_task_completed(todo_list)
        elif choice == "4":
            delete_task(todo_list)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_list_app()
