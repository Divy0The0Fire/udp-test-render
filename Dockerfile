# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the outside world (optional)
EXPOSE 5000/udp

# Run the application
CMD ["python", "server.py"]
