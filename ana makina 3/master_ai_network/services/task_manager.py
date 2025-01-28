class TaskManager:
    def __init__(self):
        self.tasks = []

    def assign_task(self, ai_unit, task):
        """
        Yapay zeka birimine görev atar.
        """
        print(f"Görev atandı: {task} -> {ai_unit.__class__.__name__}")
        ai_unit.perform_task(task)

task_manager = TaskManager()
