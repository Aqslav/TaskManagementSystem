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