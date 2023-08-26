class Task:
    def __init__(self, id, title, description, done=False):
        self.id = id
        self.title = title
        self.description = description
        self.done = done # unused lol

class TasksDB:
    def __init__(self):
        # self.tasks = []
        self.tasks = [
            Task(1, "Complete the project", "Finish the Flask project"),
            Task(2, "Buy groceries", "Milk, eggs, bread"),
            Task(3, "Go for a run", "Run for 30 minutes"),
        ]

    def add_task(self, task):
        self.tasks.append(task)

    def get_all_tasks(self):
        return self.tasks
    
    def get_task(self, id):
        for t in self.tasks:
            if t.id == id:
                return t
        return None
        
    def delete_task(self, id):
        task_to_delete = None 
        for t in self.tasks:      
            if t.id == id:
                task_to_delete = t
        
        if task_to_delete is None:
            return None
        else:
            deleted_task = Task(
                task_to_delete.id, 
                task_to_delete.title, 
                task_to_delete.description, 
                True
            )
            self.tasks.remove(task_to_delete)
            return deleted_task

    # wont do update_task cos' lazy
        

