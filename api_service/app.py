import json
import os.path
import uuid

from fastapi import FastAPI, File, Request, HTTPException, UploadFile

app = FastAPI()

@app.get("/")
async def index():
    return "OK"


@app.post("/image/outline_objects")
async def outline_objects(request: Request, dockerfile: UploadFile = File(...)):
    if request.method == "POST":

        return dict(
            id="ok",
            url=f"working"
        )

    else:
        raise HTTPException(status_code=405)