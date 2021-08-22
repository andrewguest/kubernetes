# pull official base image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY ./app/requirements.txt /app/requirements.txt

# install dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
    libressl-dev libffi-dev gcc musl-dev python3-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

# copy routes
COPY ./routes /routes/

# copy project
COPY ./app /app/

EXPOSE 8000

WORKDIR /

ENTRYPOINT [ "gunicorn", "app.main:app", "--bind", "0.0.0.0:8000", "-w", "1", "-k", "uvicorn.workers.UvicornWorker" ]