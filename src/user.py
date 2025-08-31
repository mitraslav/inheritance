from tarfile import GNU_TYPES

from src.task import Task

class User:
    username: str
    email: str
    name: str
    surname: str
    task_list: list
    users_count = 0
    all_tasks_count = 0

    def __init__(self, username, email, name, surname, task_list=None):
        self.username = username
        self.email = email
        self.name = name
        self.surname = surname
        self.__task_list = task_list if task_list else []
        User.users_count += 1
        User.all_tasks_count += len(task_list) if task_list else 0

    def __str__(self):
        return f'{self.surname}, email: {self.email}, Всего задач: {len(self.__task_list)}'

    @property
    def task_list(self):
        task_str = ""
        for task in self.__task_list:
            task_str += f"{task}\n"
        return task_str
    @task_list.setter
    def task_list(self, task: Task):
        if isinstance(task, Task):
            self.__task_list.append(task)
            User.all_tasks_count += 1
        else:
            raise TypeError


if __name__ == "__main__":
    task1 = Task('buy cucumbers', 'For salad')
    task2 = Task('buy cucumbers', 'For salad')
    task3 = Task('buy cucumbers', 'For salad')
    task4 = Task('buy cucumbers', 'For salad')

    user = User('User', 'user@mail.ru', 'User', 'Userov', [task1, task2, task3, task4])

    print(user.username)
    print(user.email)
    print(user.name)
    print(user.surname)
    print(user.task_list)

    print(user.users_count)
    print(User.all_tasks_count)

    task5 = Task('купить огурцы', "салат")
    user.task_list = task5
    print(user.task_list)
    print(User.all_tasks_count)

    print(user)

    user.task_list = Task('купить огурцы', "салат")
    print(user.task_list)