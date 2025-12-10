FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=

RUN pip install uv

WORKDIR /app
RUN mkdir /app/run

COPY ./backend /app/backend

WORKDIR /app/backend
RUN uv sync

# WORKDIR /app
# COPY ./.env.docker /app/.env
# COPY ./Makefile /app
WORKDIR /app/backend/src
CMD ["uv", "run", "celery", "-A", "core", "worker", "-B", "--loglevel=DEBUG"]
# CMD ["sleep", "infinity"]