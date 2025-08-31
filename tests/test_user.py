def test_user_init(first_user, second_user):
    assert first_user.username == 'User'
    assert second_user.username == 'John'
    assert len(first_user.task_list) == 150
    assert len(second_user.task_list) == 224

    assert first_user.users_count == 2
    assert second_user.users_count == 2

    assert first_user.all_tasks_count == 5
    assert second_user.all_tasks_count == 5

def test_user_task_list_property(first_user):
    assert first_user.task_list == ("Buy cucumbers, Статус выполнения: Ожидает старта, Дата создания: 30.08.2025\n" "Buy tomatos, Статус выполнения: Ожидает старта, Дата создания: 30.08.2025\n")

# def test_user_task_list_setter(first_user, task):
#     assert first_user.all_tasks_count == 2
#     first_user.task_list = task
#     assert first_user.all_tasks_count == 3


