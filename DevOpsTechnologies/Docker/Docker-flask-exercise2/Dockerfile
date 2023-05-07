# Use an official Python runtime as a parent image
FROM python:3.10.11-alpine3.17

# Set the working directory to /app
WORKDIR /flask-app

# Copy the current directory contents into the container at /flask-app
COPY . .

# Install the required packages
RUN pip install -r requirements.txt

# Set the environment variable FLASK_APP to the name of the Flask app file
ENV FLASK_APP=color.py

# Set the background color of the Flask app based on the value of the COLOR_MODE argument
ARG COLOR_MODE=""
ENV APP_COLOR=${COLOR_MODE}

# Expose the port that the app will run on
EXPOSE 14000

# Run app.py when the container launches
CMD ["flask", "run", "--port=14000", "--host=0.0.0.0"]
