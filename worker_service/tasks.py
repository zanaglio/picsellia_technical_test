from celery_app import celery


@celery.task(name="outline.objects.tasks.process", bind=True)
def process_image(self, image_as_base64: str) -> list:
    def update_task_state(state: str, step: int, total: int):
        self.update_state(state=state, meta={"step": step, "total": total})

    update_task_state("Retrieving image", 1, 2)
    return [len(image_as_base64)]
