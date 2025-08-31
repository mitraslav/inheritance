from src.task import Task

class DeadlineTask(Task):
    def __init__(self, name, description, deadline, created_at=None, status='Ожидает старта', run_time=0):
        super().__init__(name, description, created_at, status, run_time)
        self.deadline = deadline

if __name__ == '__main__':
    dead = DeadlineTask("Buy cucumbers", "For salad", '01.01.2001', '02.02.2001', run_time=60)
    print(dead.name)
    print(dead.description)
    print(dead.status)
    print(dead.created_at)

    print(dead.deadline)
