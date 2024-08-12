# Use an official Python runtime as a parent image
FROM python:3.11-slim


# Set work directory
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files to the container
COPY . /usr/src/app/
# Expose the port that the Django app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]