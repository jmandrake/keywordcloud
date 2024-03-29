install:
	pip install --upgrade pip
	pip install -r keywordcloud/requirements.txt

lint:
	pylint --disable=R,C keywordcloud/*.py lambda-s3/*.py

test:
	#python -m pytest -vv --cov=keywordcloud --cov=tests

format:
	black *.py keywordcloud/*.py

all: install lint test format
