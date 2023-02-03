from collections import defaultdict

class TodoList:

    def __init__(self):
        self.task_id = 0
        self.user_tasks = defaultdict(list)

    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:
        self.task_id += 1
        self.user_tasks[userId].append([self.task_id, taskDescription, dueDate, set(tags)])
        
        return self.task_id

    def getAllTasks(self, userId: int) -> List[str]:
        temp = sorted([task for task in self.user_tasks[userId]], key=lambda task: task[2])
        return [a[1] for a in temp]

    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        temp = sorted([task for task in self.user_tasks[userId] if tag in task[3]], 
                      key=lambda task: task[2])
        return [a[1] for a in temp]
        

    def completeTask(self, userId: int, taskId: int) -> None:
        self.user_tasks[userId] = [task for task in self.user_tasks[userId] if task[0] != taskId]        


# Your TodoList object will be instantiated and called as such:
# obj = TodoList()
# param_1 = obj.addTask(userId,taskDescription,dueDate,tags)
# param_2 = obj.getAllTasks(userId)
# param_3 = obj.getTasksForTag(userId,tag)
# obj.completeTask(userId,taskId)
