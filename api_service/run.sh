number_of_workers=$(getconf _NPROCESSORS_ONLN)

if [ "$ENV" = "local" ]; then
  uvicorn app:app --host 0.0.0.0 --port 80 --workers "$number_of_workers"

else
  uvicorn app:app \
    --host 0.0.0.0 \
    --port 80 \
    --workers "$number_of_workers" \
    --ssl-keyfile /etc/ssl/live/tech-test-2.picsellia.com/privkey.pem \
    --ssl-certfile /etc/ssl/live/tech-test-2.picsellia.com/fullchain.pem
fi

