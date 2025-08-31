import pytest
from src.task import Task
from src.user import User
from src.iter import TaskIterator
from src.deadline_task import DeadlineTask
from src.periodic_task import PeriodicTask
@pytest.fixture
def first_user():
    return User('User', 'user@mail.ru', 'User', 'Userov', [Task('Buy cucumbers', 'Salad'), Task('Buy tomatos', 'Salad')])

@pytest.fixture
def second_user():
    return User('John', 'john@mail.ru', 'User', 'Userov', [Task('Buy cucumbers', 'Salad'), Task('Buy tomatos', 'Salad'), Task('Buy tomatos', 'Salad')])

@pytest.fixture
def task1():
    return Task('Tomatos', 'Salad', created_at='20.04.2024', run_time=60)

@pytest.fixture
def task_with_runtime():
    return Task('Tomatos', 'Salad', created_at='20.04.2024', run_time=60)

@pytest.fixture
def task_with_runtime2():
    return Task('Cucs', 'Salad', created_at='20.04.2024', run_time=70)

@pytest.fixture
def task_iterator(second_user):
    return TaskIterator(second_user)

@pytest.fixture
def periodic_task1():
    return PeriodicTask('Cucs', 'Salad', '01.04.2024', '01.04.2024', created_at='20.04.2024', run_time=70)

@pytest.fixture
def periodic_task2():
    return PeriodicTask('Tomats', 'Salad', '01.04.2024', '01.04.2024', created_at='20.04.2024', run_time=70)

@pytest.fixture
def deadline_task1():
    return DeadlineTask('Tomats', 'Salad', '01.04.2024', created_at='20.04.2024', run_time=70)

@pytest.fixture
def deadline_task2():
    return DeadlineTask('Lemons', 'Salad', '01.04.2024', created_at='20.04.2024', run_time=70)
