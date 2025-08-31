from src.user import User
from src.task import Task

class TaskIterator:
    def __init__(self, user: User):
        self.user = user
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.user.task_list):
            task = self.user.task_list[self.index]
            self.index += 1
            return task
        else:
            raise StopIteration

if __name__ == '__main__':
    task1 = Task('buy cucumbers', 'For salad')
    task2 = Task('buy cucumbers', 'For salad')
    task3 = Task('buy cucumbers', 'For salad')
    task4 = Task('buy cucumbers', 'For salad')

    user = User('User', 'user@mail.ru', 'User', 'Userov', [task1, task2, task3, task4])

    iterator = TaskIterator(user)

    for task in iterator:
        print(task)

