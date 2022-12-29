install:
	pip install --upgrade pip
	pip install -r requirements.txt

lint:
	pylint --disable=R,C keywordcloud

test:
	python -m pytest -vv --cov=keywordcloud --cov=tests

format:
	black *.py keywordcloud/*.py

all: install lint test format