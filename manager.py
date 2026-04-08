class manager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)
    
    def print_tasks(self):
        for i in range(len(self.tasks)):
            print(f"{i+1}. {self.tasks[i].name}")
            print(f"   Description: {self.tasks[i].description}")
            print(f"   Time: {self.tasks[i].time}")
            print(f"   Priority: {self.tasks[i].priority}")

if __name__ == "__main__":
    manager = manager()
    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Print Tasks")
        print("5. Print Tasks by Priority")
        print("6. Print Tasks by Time")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            time = input("Enter task time: ")
            priority = input("Enter task priority: ")
            task = task(name, description, time, priority)
            manager.add_task(task)
        elif choice == "2":
            manager.print_tasks()
            name = input("Enter task name to remove: ")
            for task in manager.tasks:
                if task.name == name:
                    manager.remove_task(task)
                    break
        elif choice == "3":
            manager.print_tasks()
            name = input("Enter task name to mark as completed: ")
            for task in manager.tasks:
                if task.name == name:
                    manager.remove_task(task)
                    break
        elif choice == "4":
            manager.print_tasks()
        elif choice == "5":
            manager.tasks.sort(key=lambda x: x.priority)
            manager.print_tasks()
        elif choice == "6":
            manager.tasks.sort(key=lambda x: x.time)
            manager.print_tasks()
        elif choice == "7":
            break