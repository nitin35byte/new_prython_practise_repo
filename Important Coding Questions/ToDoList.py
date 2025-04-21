class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Task "{task}" added to the list.')

    def remove_task(self, task):
        removed = False
        for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                removed = True
                print(f'Task "{task}" removed from the list.')
                break
        if not removed:
            print(f'Task "{task}" not found in the list.')

    def complete_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["completed"] = True
                print(f'Task "{task}" marked as completed.')
                break
        else:
            print(f'Task "{task}" not found in the list.')

    def display_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, t in enumerate(self.tasks, start=1):
                status = " [Pass]" if t["completed"] else " [ ]"
                print(f"{index}. {t['task']}{status}")
        else:
            print("Your To-Do List is empty.")

def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Complete Task")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            task = input("Enter task to mark as complete: ")
            todo_list.complete_task(task)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
