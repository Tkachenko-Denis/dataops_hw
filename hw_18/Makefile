PYTHON ?= .venv/bin/python
YOYO := $(PYTHON) -m yoyo
MIGRATIONS_DIR := migrations

.PHONY: dev.install db.migration.new db.migrate db.rollback

dev.install:
	python -m venv .venv
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

db.migration.new:
	$(YOYO) new $(MIGRATIONS_DIR) -m "$(name)"

db.migrate:
	$(YOYO) apply --batch --database "$$DATABASE_URL" $(MIGRATIONS_DIR)

db.rollback:
	$(YOYO) rollback --batch --database "$$DATABASE_URL" $(MIGRATIONS_DIR)
