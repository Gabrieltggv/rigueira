FROM python:3.10.5-slim-buster AS build-python
ARG ENVIRONMENT
ENV ENVIRONMENT=${ENVIRONMENT}
RUN apt-get update && apt-get install -y build-essential gcc python3-dev musl-dev
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY ./requirements/${ENVIRONMENT}.txt .
RUN pip install -r ${ENVIRONMENT}.txt

FROM python:3.10.5-slim-buster AS development
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/opt/venv/bin:$PATH"
COPY --from=build-python /opt/venv /opt/venv
RUN apt-get update && apt-get install -y make gcc python3-dev musl-dev
WORKDIR /usr/src/app
COPY ./rigueira/ .

FROM python:3.10.5-slim-buster AS prod
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG=False
ARG SECRET_KEY
ARG USE_S3
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_STORAGE_BUCKET_NAME
ARG ENVIRONMENT
ENV ENVIRONMENT=${ENVIRONMENT}
ENV SECRET_KEY=${SECRET_KEY}
ENV USE_S3=${USE_S3}
ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
ENV AWS_STORAGE_BUCKET_NAME=${AWS_STORAGE_BUCKET_NAME}
ENV PATH="/opt/venv/bin:$PATH"
COPY --from=build-python /opt/venv /opt/venv
RUN apt-get update && apt-get install -y make gcc python3-dev musl-dev
WORKDIR /usr/src/app
COPY ./rigueira/ .
RUN python manage.py collectstatic --noinput
CMD gunicorn rigueira.wsgi:application
