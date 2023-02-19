from abc import ABC

from celery import Task
from models.object_detector_model import ObjectDetectorModel


class OutlineObjectsTask(Task, ABC):
    abstract = True

    def __init__(self):
        super().__init__()
        self.model = None

    def __call__(self, *args, **kwargs):
        """
        Only load the model inside the first Celery task call (avoids the need to load the model on each task request)
        """
        if not self.model:
            print('Loading Model...')
            self.model = ObjectDetectorModel()
            print('Model loaded!')

        return self.run(*args, **kwargs)

    def update_task_state(self, task, state: str, step: int, total: int):
        """
        Update a celery state.

        :param task: The reference to the task to update.
        :param state: The state message to display.
        :param step: The current step count.
        :param total: The total number of steps.
        """
        task.update_state(state=state, meta={"step": step, "total": total})
