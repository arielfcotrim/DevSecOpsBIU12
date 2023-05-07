# Use an official Python runtime as a parent image
FROM python:3.10.11-alpine3.17

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install the required packages
RUN pip install -r requirements.txt

# Set the environment variable FLASK_APP to the name of the Flask app file
ENV FLASK_APP=main.py

# Expose the port that the app will run on
EXPOSE 5010

# Run the command to start the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
