#!/bin/bash

# --- Stop any running uvicorn services ---
echo "Stopping old services..."
pkill -f "uvicorn gateway.main:app" || true
pkill -f "uvicorn user_service.main:app" || true
pkill -f "uvicorn order_service.main:app" || true

# --- Pull latest code ---
echo "Pulling latest code..."
git pull origin main

# --- Start services ---
echo "Starting services..."
nohup uvicorn gateway.main:app --host 0.0.0.0 --port 8000 --reload > gateway/nohup.log 2>&1 &
nohup uvicorn user_service.main:app --host 0.0.0.0 --port 8001 --reload > user_service/nohup.log 2>&1 &
nohup uvicorn order_service.main:app --host 0.0.0.0 --port 8002 --reload > order_service/nohup.log 2>&1 &

echo "Deployment complete!"
