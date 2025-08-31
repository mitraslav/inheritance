from src.task import Task

class PeriodicTask(Task):
    def __init__(self, name, description, start_date, end_date,  created_at=None, status='Ожидает старта', run_time=0, frequency='Ежедневно'):
        super().__init__(name, description, created_at, status, run_time)
        self.start_date = start_date
        self.end_date = end_date
        self.frequency = frequency

if __name__ == '__main__':
    per = PeriodicTask("Buy cucumbers", "For salad", '01.01.2001', '02.02.2001', run_time=60)
    print(per.name)
    print(per.description)
    print(per.status)
    print(per.created_at)

    print(per.start_date)
    print(per.end_date)
    print(per.frequency)