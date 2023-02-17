from celery_app import celery
from model.model import predict
from utils.image import base64_to_array
from utils.outline import get_objects_vertices


@celery.task(name="outline.objects.tasks.process", bind=True)
def process_image(self, image_as_base64: str) -> list:
    def update_task_state(state: str, step: int, total: int):
        self.update_state(state=state, meta={"step": step, "total": total})

    update_task_state("Performing the prediction", 1, 2)
    image_data = base64_to_array(image_as_base64)
    prediction = predict(image_data)

    update_task_state("Computing the objects' vertices", 2, 2)
    object_vertices = get_objects_vertices(prediction)

    return object_vertices
