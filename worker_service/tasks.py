from celery_app import celery
from models.outline_objects_tasks import OutlineObjectsTask
from utils.image import base64_to_array
from utils.vertices import extract_vertices


@celery.task(base=OutlineObjectsTask, name="outline.objects.tasks.process", bind=True)
def compute_objects_outlines(self, image_as_base64: str) -> dict[str]:
    """
    Compute all the outlines' vertices of all the detected object within the received image.
    """

    self.update_task_state(self, "Performing the prediction", 1, 2)
    image_data = base64_to_array(image_as_base64)
    prediction = self.model.predict(image_data)

    self.update_task_state(self, "Computing the objects' vertices", 2, 2)
    object_vertices = extract_vertices(prediction)

    return {
        "objects_vertices": dict(enumerate(object_vertices))
    }
