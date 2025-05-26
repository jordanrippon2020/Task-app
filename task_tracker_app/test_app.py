import unittest
# Important: import the app module itself to access its global variables
import app as task_app_module 

class TestTaskApp(unittest.TestCase):

    def setUp(self):
        """
        This method is called before each test.
        It clears the global tasks list and resets the task_id_counter.
        """
        task_app_module.tasks.clear()
        task_app_module.task_id_counter = 1

    def test_add_task(self):
        """Test adding a new task."""
        task_text = "My first test task"
        added_task = task_app_module.add_task(task_text)
        
        self.assertEqual(len(task_app_module.tasks), 1)
        self.assertEqual(task_app_module.tasks[0]['text'], task_text)
        self.assertFalse(task_app_module.tasks[0]['completed'])
        self.assertEqual(task_app_module.tasks[0]['id'], 1)
        self.assertEqual(added_task['text'], task_text)
        self.assertEqual(task_app_module.task_id_counter, 2) # Counter should increment

        task_text_2 = "My second test task"
        added_task_2 = task_app_module.add_task(task_text_2)
        self.assertEqual(len(task_app_module.tasks), 2)
        self.assertEqual(task_app_module.tasks[1]['text'], task_text_2)
        self.assertEqual(task_app_module.tasks[1]['id'], 2)
        self.assertEqual(added_task_2['id'], 2)
        self.assertEqual(task_app_module.task_id_counter, 3)


    def test_get_all_tasks(self):
        """Test retrieving all tasks."""
        self.assertEqual(task_app_module.get_all_tasks(), []) # Initially empty

        task_text_1 = "Task A"
        task_app_module.add_task(task_text_1)
        task_text_2 = "Task B"
        task_app_module.add_task(task_text_2)

        all_tasks = task_app_module.get_all_tasks()
        self.assertEqual(len(all_tasks), 2)
        self.assertEqual(all_tasks[0]['text'], task_text_1)
        self.assertEqual(all_tasks[1]['text'], task_text_2)

    def test_complete_task(self):
        """Test marking a task as completed."""
        task_text = "Task to complete"
        added_task = task_app_module.add_task(task_text)
        task_id = added_task['id']

        self.assertFalse(task_app_module.tasks[0]['completed']) # Check initial state

        result = task_app_module.complete_task(task_id)
        self.assertTrue(result)
        self.assertTrue(task_app_module.tasks[0]['completed'])

        # Test completing a non-existent task
        non_existent_task_id = 999
        result_non_existent = task_app_module.complete_task(non_existent_task_id)
        self.assertFalse(result_non_existent)
        self.assertTrue(task_app_module.tasks[0]['completed']) # Ensure existing task is not affected

    def test_delete_task(self):
        """Test deleting a task."""
        task_text_1 = "Task to be deleted"
        task_text_2 = "Task to keep"
        
        added_task_1 = task_app_module.add_task(task_text_1)
        task_app_module.add_task(task_text_2)
        
        task_id_to_delete = added_task_1['id']

        self.assertEqual(len(task_app_module.tasks), 2)

        result = task_app_module.delete_task(task_id_to_delete)
        self.assertTrue(result)
        self.assertEqual(len(task_app_module.tasks), 1)
        self.assertEqual(task_app_module.tasks[0]['text'], task_text_2) # Check remaining task

        # Test deleting a non-existent task
        non_existent_task_id = 999
        result_non_existent = task_app_module.delete_task(non_existent_task_id)
        self.assertFalse(result_non_existent)
        self.assertEqual(len(task_app_module.tasks), 1) # Ensure list size is unchanged

        # Delete the remaining task
        result_2 = task_app_module.delete_task(task_app_module.tasks[0]['id'])
        self.assertTrue(result_2)
        self.assertEqual(len(task_app_module.tasks), 0)


if __name__ == '__main__':
    unittest.main()
