import json

from fastapi import FastAPI, File, Request, HTTPException

from celery_app import celery
from utils.image import bytes_to_base64

app = FastAPI()


@app.get("/")
async def index():
    return "SUCCESS"


@app.post("/image/outline/objects")
async def outline_objects(
        request: Request,
        image: bytes = File(...)
):
    if request.method == "POST":
        image_as_base64 = bytes_to_base64(image_bytes=image)

        task_name = "outline.objects.tasks.process"
        task = celery.send_task(task_name, [image_as_base64])

        return dict(
            id=task.id, url=f"{str(request.base_url)}outline/objects/check/{task.id}"
        )

    else:
        raise HTTPException(status_code=405)


@app.get("/outline/objects/check/{task_id}")
def check_task(task_id: str):
    task = celery.AsyncResult(task_id)

    if task.state == "SUCCESS":
        response = {"status": task.state, "result": task.result, "task_id": task_id}

    elif task.state == "FAILURE":
        response = json.loads(
            task.backend.get(task.backend.get_key_for_task(task.id)).decode("utf-8")
        )
        del response["children"]
        del response["traceback"]

    elif task.state == "PENDING" and task.result is None:
        raise HTTPException(
            status_code=410, detail="The specified task_id has expired."
        )

    else:
        response = {"status": task.state, "result": task.info, "task_id": task_id}

    return response
