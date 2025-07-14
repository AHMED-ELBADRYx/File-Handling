# Save and Load Tasks in Python

import os

# Color codes for better UI
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def clear_screen():
    """Clear the console screen based on the OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

tasks = []

def load_tasks():
    """Load tasks from file when program starts."""
    global tasks
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file if line.strip()]
        print(f"{Colors.OKGREEN}Tasks loaded successfully!{Colors.ENDC}")
    except FileNotFoundError:
        tasks = []
        print(f"{Colors.WARNING}No existing task file. Starting with empty list.{Colors.ENDC}")

def save_tasks():
    """Save tasks to file when they are modified."""
    with open("tasks.txt", "w") as file:
        file.write("\n".join(tasks))
    print(f"{Colors.OKGREEN}Tasks saved successfully!{Colors.ENDC}")

def show_tasks():
    """Display all current tasks."""
    clear_screen()
    if tasks:
        print(f"\n{Colors.HEADER}YOUR TASKS:{Colors.ENDC}")
        print("-" * 30)
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print("-" * 30)
    else:
        print(f"{Colors.WARNING}There are no tasks currently.{Colors.ENDC}")

def add_task():
    """Add a new task to the list."""
    clear_screen()
    print(f"\n{Colors.OKBLUE}ADD NEW TASK{Colors.ENDC}")
    print("-" * 30)
    task = input("Enter the new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks()
        print(f"{Colors.OKGREEN}Task added successfully!{Colors.ENDC}")
    else:
        print(f"{Colors.FAIL}Task cannot be empty!{Colors.ENDC}")

def delete_task():
    """Delete a task from the list."""
    clear_screen()
    show_tasks()
    if not tasks:
        return
    
    print(f"\n{Colors.OKBLUE}DELETE TASK{Colors.ENDC}")
    print("-" * 30)
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks()
            print(f"{Colors.OKGREEN}Task '{removed_task}' removed successfully!{Colors.ENDC}")
        else:
            print(f"{Colors.FAIL}Invalid task number!{Colors.ENDC}")
    except ValueError:
        print(f"{Colors.FAIL}Please enter a valid number!{Colors.ENDC}")

def display_menu():
    """Display the main menu options."""
    clear_screen()
    print(f"\n{Colors.HEADER}TASK MANAGER MENU{Colors.ENDC}")
    print("-" * 30)
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")
    print("-" * 30)

def main():
    """Main application function."""
    load_tasks()
    
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            show_tasks()
            input("\nPress Enter to continue...")
        elif choice == "2":
            add_task()
            input("\nPress Enter to continue...")
        elif choice == "3":
            delete_task()
            input("\nPress Enter to continue...")
        elif choice == "4":
            print(f"{Colors.OKBLUE}Goodbye!{Colors.ENDC}")
            break
        else:
            print(f"{Colors.FAIL}Invalid choice! Please select 1-4.{Colors.ENDC}")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()