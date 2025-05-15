def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter the task: ").strip()
    if task:
        tasks.append({'task': task, 'done': False})
        print("[+] Task added.")
    else:
        print("[!] Task cannot be empty.")

def view_tasks(tasks):
    if not tasks:
        print("[!] No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, start=1):
            status = "✔️ Done" if t['done'] else "❌ Not Done"
            print(f"{i}. {t['task']} [{status}]")

def mark_done(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['done'] = True
            print("[+] Task marked as done.")
        else:
            print("[!] Invalid task number.")
    except ValueError:
        print("[!] Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"[+] Deleted task: {removed['task']}")
        else:
            print("[!] Invalid task number.")
    except ValueError:
        print("[!] Please enter a valid number.")

def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("[!] Invalid choice. Try again.")

if __name__ == "__main__":
    main()
