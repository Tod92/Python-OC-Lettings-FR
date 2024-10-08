# pull the official base image
FROM python:3.11-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
# Prevents Python from copying pyc files to the container.
ENV PYTHONDONTWRITEBYTECODE 1
# Ensures that Python output is logged to the terminal.
ENV PYTHONUNBUFFERED 1
# Setting django DEBUG=False
ENV DEBUG 0

# copy project
COPY . /usr/src/app

# install dependencies
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

# generate static files
## RUN python manage.py collectstatic --noinput
# Error while trying to generate staticfiles dir with circleci : can't reach env variable SECRET_KEY
# Passing staticfiles directory for now

# CMD ["python", "manage.py", "runserver", "0.0.0.0:$PORT"]
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT