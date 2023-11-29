WORKING_DIR=$(shell pwd)

venv:
	python3 -m venv venv
	./venv/bin/python3 -m pip install --upgrade pip

.PHONY: setup
setup: venv
	./venv/bin/pip3 install -r requirements.txt

.PHONY: setup-style
setup-style: setup
	./venv/bin/pip3 install --no-cache-dir -r requirements-style.txt
	./venv/bin/pre-commit install --hook-type pre-commit --hook-type pre-push

.PHONY: setup-dev
setup-dev: setup setup-style

check-format: # Check which files will be reformatted
	./venv/bin/black --check .

format: # Format files
	./venv/bin/black .

lint:
	./venv/bin/flake8 .

clean:
	rm -rf venv
