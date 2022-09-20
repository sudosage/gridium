install:
	#python3 -m pip install --upgrade pip &&\
		# pip install -r requirements.txt
		
format:
	# black src/main.py src/mylib/*.py
typecheck:
	# mypy --namespace-packages -p src.mylib --ignore-missing-imports --warn-unreachable  --exclude src/mylib/service_parse.py
lint:
	# pylint --disable=R,C src/mylib/*.py
test:
	# pytest --cov=mylib
build:
	# buiild container
deploy:
	# deploy
run:
	# python3 src/main.py

all: install format typecheck lint test build deploy
ltest: format typecheck lint test