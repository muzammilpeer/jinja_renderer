# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
#COPY Pipfile Pipfile.lock /code/
#RUN pip install pipenv && pipenv install --system

# Copy project
COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 8001

# Run the application:
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
