import pytest
from task import task
from manager import manager
from IO_helper import IO_helper

class TestTaskManager:
    @pytest.fixture(autouse=True)
    def manager_instance(self):
        return manager()

    @pytest.mark.parametrize("task_data", [
        ("Test Task 1", "This is the first test task", "2024-06-01", 3),
        ("Test Task 2", "This is the second test task", "2024-06-02", 2),
        ("Test Task 3", "This is the third test task", "2024-06-03", 1),
    ])
    def test_add_task(self, task_data):
        with pytest.mock.patch('IO_helper.load', return_value=[]):
            manager_instance = self.manager_instance
            task_instance = task(*task_data)
            manager_instance.add_task(task_instance)
            assert IO_helper.load("tasks.json") == [task_instance.__dict__]

    @pytest.mark.parametrize("task_data", [
        ("Test Task 1", "This is the first test task", "2024-06-01", 3),
        ("Test Task 2", "This is the second test task", "2024-06-02", 2),
        ("Test Task 3", "This is the third test task", "2024-06-03", 1),
    ])
    def test_remove_task(self, task_data):
        with pytest.mock.patch('IO_helper.load', return_value=[task(*task_data).__dict__]):
            manager_instance = self.manager_instance
            task_instance = task(*task_data)
            manager_instance.remove_task(task_instance.__dict__)
        assert IO_helper.load("tasks.json") == []