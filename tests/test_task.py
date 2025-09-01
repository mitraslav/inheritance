def test_task_str(task1):
    print(task1)

def test_task_update(capsys, task):
    task.created_at = '29.02.2024'
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-1] == 'Нельзя изменить дату создания из прошлого'