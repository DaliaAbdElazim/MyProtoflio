# Select a base image that includes Python
FROM python:3.12.5

# Set up a working directory in the container for your application
WORKDIR /app

# Copy the backend code into the container
COPY . /app

# Install any Python dependencies listed in 'requirements.txt'
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8080

# Set the command to run your application
CMD ["python", "app.py"]