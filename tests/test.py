import pytest
from task import task
from manager import manager
from IO_helper import IO_helper

@pytest.parametrize("task_data", [
    ("Test Task 1", "This is the first test task", "2024-06-01", 3),
    ("Test Task 2", "This is the second test task", "2024-06-02", 2),
    ("Test Task 3", "This is the third test task", "2024-06-03", 1),
])
def test_add_task(task_data):
    with pytest.mock.patch('IO_helper.load', return_value=[]):
        manager_instance = manager()
        task_instance = task(*task_data)
        manager_instance.add_task(task_instance)
        assert IO_helper.load("tasks.json") == [task_instance.__dict__]
        