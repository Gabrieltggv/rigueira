FROM python:3.10-alpine AS build-python
RUN apk update && apk add --virtual build-essential gcc python3-dev musl-dev postgresql-dev
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY ./requirements/dev.txt .
RUN pip install -r dev.txt

FROM python:3.10-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
ENV PATH="/opt/venv/bin:$PATH"
COPY --from=build-python /opt/venv /opt/venv
RUN apk update && apk add --virtual build-deps gcc python3-dev musl-dev postgresql-dev
WORKDIR /app
COPY . .
RUN adduser -D gabriel
USER gabriel
#CMD gunicorn hello_django.wsgi:application --bind 0.0.0.0:$PORT
