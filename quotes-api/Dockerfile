FROM python:3.12.4-slim-bookworm

# Relate this image to the correct Github repo
LABEL org.opencontainers.image.source=https://github.com/andrewguest/kubernetes
LABEL org.opencontainers.image.description="API that returns random quotes"
LABEL org.opencontainers.image.licenses=MIT

RUN mkdir /app
WORKDIR /app/

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn"]
