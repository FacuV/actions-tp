# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port on which the FastAPI app will run
EXPOSE 8000

# Start the FastAPI app when the container starts
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--reload" , "--port", "8000"]