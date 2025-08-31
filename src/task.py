import datetime

class Task:
    name: str
    description: str
    status: str
    created_at: str
    run_time: int

    def __init__(self, name, description, created_at=None, status='Ожидает старта', run_time=0):
        self.name = name
        self.description = description
        self.status = status
        self.__created_at = created_at if created_at else datetime.date.today().strftime("%d.%m.%Y")
        self.run_time = run_time

    def __str__(self):
        return f"{self.name}, Статус выполнения: {self.status}, Дата создания: {self.created_at}"

    def __add__(self, other):
        if type(other) is Task:
            return self.run_time + other.run_time
        raise TypeError


    @classmethod
    def new_task(cls, name, description, created_at=None, status='Ожидает старта', run_time=0):
        return cls(name, description, created_at, status, run_time)

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, new_date: str):
        if datetime.datetime.strptime(new_date, "%d.%m.%Y").date() < datetime.datetime.now().date():
            print('Нельзя изменить дату создания на дату из прошлого')
            return
        self.__created_at = new_date


if __name__ == "__main__":
    task = Task("Buy cucumbers", "For salad", run_time=60)

    print(task.name, task.description, task.status, task.created_at)

    task2 = Task.new_task("купить билеты", "самолет", run_time=60)
    print(task2.name)
    print(task2.description)
    print(task2.status)
    print(task2.created_at)

    task2.created_at = '29.02.2024'
    print(task2.created_at)
    task2.created_at = '29.08.2026'
    print(task2.created_at)

    task_3 = Task('buy', 'buy', run_time=60)
    task_4 = Task('hi', 'hi', run_time=5)
    print(task_3 + task_4)

    print(task + task2)
    print(task + 1)