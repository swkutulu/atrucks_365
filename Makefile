.PHONY: help
.SILENT:

include .env

help:
	@grep -E '^[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) | sort | awk '{ sub("Makefile:", ""); print }' | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2, $$3}'
	#@grep -E '^[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


install-all: # install all and start services
	make install-backend-all install-frontend


start-backend-prod: # start backend prod (gunicorn)
	@echo "run backend"
	cd ./backend/src && \
	nohup uv run gunicorn core.wsgi:application --pid ../../run/backend.pid -b 127.0.0.1:9100 --preload --threads 4 --workers 1 > ../../logs/back_out.log 2> ../../logs/back_err.log &


stop-backend-prod: # stop backend prod (stop gunicorn)
	@echo "stop backend"
	kill -9  $(shell cat ./run/backend.pid)


start-backend-dev: # start backend (runserver as :9100)
	@echo "run backend"
	cd ./backend/src && \
	uv run ./manage.py runserver 127.0.0.1:9100


start-celery-dev: # start celery
	@echo "run celery"
	cd ./backend/src && \
	uv run celery -A core worker -B --loglevel=DEBUG


start-frontend-dev: # start frontend (vite on :3100)
	@echo "start frontend"
	cd ./frontend && \
	vite 


install-backend-all: # install all backend
	make init-db-all install-backend insert-test-data create-test-db


init-db-all: # create db, user, grant
	@echo "init DB"
	make create-db create-user grant-privileges 


insert-test-data: # create some data
	@echo "Создаем тестовые данные и superuser-а"
	cd ./backend && \
	uv run python3.12 ./src/manage.py import_test_data


test-backend: # run tests (pytest) for backend
	@echo "run tests for backend"
	cd ./backend && \
	uv run pytest -sv


create-db: # create db
	@echo "Создание базы данных $(DB_NAME)..."
	$(PSQL) -c "CREATE DATABASE $(DB_NAME) owner $(DB_USER);" || \
	echo "Ошибка создания базы $(DB_NAME)."


create-user: # create user (for django)
	@echo "Создание пользователя $(DB_USER)..."
	$(PSQL) -c "CREATE USER $(DB_USER) WITH PASSWORD '$(DB_PASS)';" || \
	echo "Ошибка создания пользователя $(DB_USER)."


grant-privileges: # grant access to db_user
	@echo "Предоставление прав пользователю $(DB_USER) на базу $(DB_NAME)..."
	$(PSQL) -c "GRANT ALL PRIVILEGES ON DATABASE $(DB_NAME) TO $(DB_USER);"


create-test-db: # create TEST db
	@echo "Копируем рабочую базу для тестов"
	$(PSQL) -c "CREATE DATABASE $(DB_NAME_TEST) TEMPLATE $(DB_NAME);" || \
	echo "Не удалось создать базу $(DB_NAME_TEST)."


drop-db: # delete both databases (prod and test)
	@echo "Удаление базы данных $(DB_NAME)..."
	$(PSQL) -c "DROP DATABASE IF EXISTS $(DB_NAME);"
	$(PSQL) -c "DROP DATABASE IF EXISTS $(DB_NAME_TEST);"


install-backend: # make venv, copy local.py
	@echo "install backend"
	cp ./backend/src/core/settings/local.default.py ./backend/src/core/settings/local.py
	cd ./backend && \
	uv sync && \
	uv run python3.12 ./src/manage.py migrate && \
	uv run python3.12 ./src/manage.py collectstatic --noinput;


install-backend-prod: # make venv, copy local.py
	@echo "install backend"
	cp ./backend/src/core/settings/local.default.py ./backend/src/core/settings/local.py
	cd ./backend && \
	uv sync --prod && \
	uv run python3.12 ./src/manage.py migrate && \
	uv run python3.12 ./src/manage.py collectstatic --noinput;


install-frontend: # install frontend
	@echo "install frontend"
	cp ./frontend/.env.default ./frontend/.env
	cd ./frontend && \
	yarn install
