number_of_workers=$(getconf _NPROCESSORS_ONLN)

uvicorn app:app --host 0.0.0.0 --port 80 --workers "$number_of_workers"