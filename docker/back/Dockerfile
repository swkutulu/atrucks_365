FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=

RUN pip install uv

WORKDIR /app
RUN mkdir /app/run
RUN mkdir /app/backend
COPY ./backend/.python-version /app/backend
COPY ./backend/pyproject.toml /app/backend/
COPY ./backend/uv.lock /app/backend/

# COPY ./backend /app/backend
# COPY ./static /app/static
# COPY ./backend/src /app/backend/src

WORKDIR /app/backend
RUN uv sync

WORKDIR /app
COPY ./.env.docker /app/.env
COPY ./Makefile /app

# EXPOSE ${BACK_SERVER_PORT}
# CMD ["celery -A core worker -B --loglevel=DEBUG"]