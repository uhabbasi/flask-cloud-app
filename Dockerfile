# Use a lightweight official Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port Flask uses
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]

