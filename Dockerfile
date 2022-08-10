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
ENV PATH="/opt/venv/bin:$PATH"
COPY --from=build-python /opt/venv /opt/venv
RUN apt-get update && apt-get install -y make gcc python3-dev musl-dev
WORKDIR /usr/src/app
COPY ./rigueira/ .
RUN python manage.py collectstatic --noinput
CMD gunicorn rigueira.wsgi:application
