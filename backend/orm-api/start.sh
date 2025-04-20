#!/bin/bash

# Check the MODE environment variable
if [ "$MODE" = "api" ]; then
    echo "Starting FastAPI application..."
    uvicorn api:app --host 0.0.0.0 --port 8000 --reload
else
    echo "Running main.py script..."
    python main.py
fi