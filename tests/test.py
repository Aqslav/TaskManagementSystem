import pytest
from unittest.mock import patch
from task import task
from manager import manager
from IO_helper import IO_helper

class TestTaskManager:
    @pytest.fixture
    def manager_instance(self):
        return manager()

    @pytest.mark.parametrize("task_data", [
        ("Test Task 1", "This is the first test task", "2024-06-01", 3),
        ("Test Task 2", "This is the second test task", "2024-06-02", 2),
        ("Test Task 3", "This is the third test task", "2024-06-03", 1),
    ])
    def test_add_task(self, manager_instance, task_data):
        task_instance = task(*task_data)
        with patch("manager.IO_helper.load", return_value=[]), \
            patch("manager.IO_helper.save") as mock_save:
                manager_instance.add_task(task_instance)
                mock_save.assert_called_once()

    @pytest.mark.parametrize("task_data", [
        ("Test Task 1", "This is the first test task", "2024-06-01", 3),
        ("Test Task 2", "This is the second test task", "2024-06-02", 2),
        ("Test Task 3", "This is the third test task", "2024-06-03", 1),
    ])
    def test_remove_task(self, manager_instance, task_data):
        with patch('manager.IO_helper.load', return_value=[task(*task_data).__dict__]):
            task_instance = task(*task_data)
            manager_instance.remove_task(task_instance.__dict__)
        assert IO_helper.load("tasks.json") == []