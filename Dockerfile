FROM python:3.9

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Create a directory for the SQLite database
#SG 2023-04-16 : may not be needed for docker-compose
RUN mkdir /data

# Set the environment variable for the database location
ENV DATABASE_URL=sqlite:////data/db.sqlite3

SHELL ["/bin/bash", "-c"]

# running migrations
RUN python manage.py migrate

RUN python -m manage collectstatic --no-input

# Expose the port the app will run on
#EXPOSE 8000

# gunicorn
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]
