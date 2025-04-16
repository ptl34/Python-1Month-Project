import json
import os

FILE_NAME = 'tasks.json'

# Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    return []

# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, 'w') as f:
        json.dump(tasks, f, indent=4)

# Add new task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = {
        'title': title,
        'description': description,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added!\n")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("📭 No tasks available.\n")
        return
    for idx, task in enumerate(tasks, 1):
        status = "✅ Completed" if task['completed'] else "❌ Pending"
        print(f"{idx}. {task['title']} [{status}]")
        print(f"   Description: {task['description']}\n")

# Mark as completed
def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as completed: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]['completed'] = True
            save_tasks(tasks)
            print("✔️ Task marked as completed.\n")
        else:
            print("⚠️ Invalid task number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"🗑️ Task '{removed['title']}' deleted.\n")
        else:
            print("⚠️ Invalid task number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\n=== Task Tracker ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("👋 Exiting Task Tracker.")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == '__main__':
    main()

