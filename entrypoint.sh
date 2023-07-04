#!/bin/bash

# Inicia el servidor FastAPI
uvicorn src.app:app --host 0.0.0.0 --reload --port 8000
