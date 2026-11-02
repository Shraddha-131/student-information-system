
# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code
COPY . .

# Make Flask accessible outside the container
ENV FLASK_HOST=0.0.0.0

# Expose the Flask application port
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]
