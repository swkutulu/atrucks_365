.PHONY: help
.SILENT:

include .env
include ../.env

POSTGRES_DB = $(DB_NAME)
POSTGRES_PORT = $(POSTGRES_PORT_EXPOSE)
POSTGRES_HOST_AUTH_METHOD = trust
# экспортировать с осторожностью, попадают в создание образов
export POSTGRES_HOST_AUTH_METHOD
export POSTGRES_PORT

PSQL = psql -U postgres -h localhost -p $(POSTGRES_PORT) -d postgres


help:
	@grep -E '^[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) | awk '{ sub("Makefile:", ""); print }' | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2, $$3}'


init-all: # init docker postgres db, create test data, create test db
	make prebuild-docker-db init-db-all


prebuild-docker-db: # x
	@docker compose build --no-cache db
	@docker compose up --no-start --no-build db
	@docker compose up db -d
	@docker compose build --no-cache back


init-db-all: # x
	make init-db
	make migrate && \
	make insert-test-data && \
	make create-test-db


init-db: # init db only
	$(PSQL) -c "CREATE USER $(DB_USER) WITH PASSWORD '$(DB_PASS)';" || echo "Ошибка создания пользователя $(DB_USER)."
	$(PSQL) -c "CREATE DATABASE $(DB_NAME) OWNER $(DB_USER);" || echo "Ошибка создания базы $(DB_NAME)."
	$(PSQL) -c "ALTER SCHEMA public OWNER TO $(DB_USER);"
	$(PSQL) -c "GRANT ALL PRIVILEGES ON DATABASE $(DB_NAME) TO $(DB_USER);"


migrate: # create some data
#.ONESHELL:
	@echo "Apply migrations"
	cd ../backend  && \
	uv sync && \
	uv run python3.12 ./src/manage.py migrate && \
	uv run python3.12 ./src/manage.py collectstatic --noinput;


insert-test-data: # create some data
	@echo "Создаем тестовые данные и superuser-а"
	cd ../backend && \
	uv run python3.12 ./src/manage.py import_test_data


create-test-db: # create TEST db
	@echo "Копируем рабочую базу для тестов"
	$(PSQL) -c "CREATE DATABASE $(DB_NAME_TEST) TEMPLATE $(DB_NAME);" || echo "Не удалось создать базу $(DB_NAME_TEST)."


drop-db: # delete both databases (prod and test)
	@echo "Удаление базы данных $(DB_NAME)..."
	$(PSQL) -c "DROP DATABASE IF EXISTS $(DB_NAME);"
	$(PSQL) -c "DROP DATABASE IF EXISTS $(DB_NAME_TEST);"
