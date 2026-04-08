from task import task
from IO_helper import IO_helper
FILE_PATH = "tasks.json"
class manager:
    def add_task(self, job):
        tasks = list(IO_helper.load(FILE_PATH))
        tasks.append(job)
        IO_helper.save(tasks, FILE_PATH)

    def remove_task(self, job):
        tasks = list(IO_helper.load(FILE_PATH))
        tasks.remove(job)
        IO_helper.save(tasks, FILE_PATH)

    def print_tasks(self):
        tasks = list(IO_helper.load(FILE_PATH))
        for i in range(len(tasks)):
            print(f"{i+1}# {tasks[i]['name']}")
            print(f"   Description: {tasks[i]['description']}")
            print(f"   Time: {tasks[i]['time']}")
            print(f"   Priority: {tasks[i]['priority']}")


if __name__ == "__main__":
    import os
    this_folder = os.path.dirname(os.path.abspath(__file__))
    os.chdir(this_folder)
    if not os.path.exists(FILE_PATH):
        IO_helper.save([], FILE_PATH)
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
            job = task(name, description, time, priority)
            manager.add_task(job)
        elif choice == "2":
            manager.print_tasks()
            name = input("Enter task name to remove: ")
            for job in list(IO_helper.load(FILE_PATH)):
                if job['name'] == name:
                    manager.remove_task(job)
                    break
        elif choice == "3":
            manager.print_tasks()
            name = input("Enter task name to mark as completed: ")
            for job in list(IO_helper.load(FILE_PATH)):
                if job['name'] == name:
                    manager.remove_task(job)
                    break
        elif choice == "4":
            manager.print_tasks()
        elif choice == "5":
            tasks = list(IO_helper.load(FILE_PATH))
            tasks.sort(key=lambda x: x['priority'])
            IO_helper.save(tasks, FILE_PATH)
            manager.print_tasks()
        elif choice == "6":
            tasks = list(IO_helper.load(FILE_PATH))
            tasks.sort(key=lambda x: x['time'])
            IO_helper.save(tasks, FILE_PATH)
            manager.print_tasks()
        elif choice == "7":
            break