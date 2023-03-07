SHELL = /bin/bash
.DEFAULT_GOAL = none

### help actions
help:
	@echo 'Makefile for backoffice app                                                                         '
	@echo '                                                                                                    '
	@echo 'Usage:                                                                                              '
	@echo '                                                                                                    '
	@echo '    make install           Install python packages (with pip, from requirements.txt)                '
	@echo '    make install-dev       Install python packages (with pip, from dev-requirements.txt)            '
	@echo '    make test              Create folders and files to run unit tests                               '
	@echo '    make test              Create folders and files to run unit tests                               '


### actions to clean project files
clean: clean-cache

clean-cache:
	sudo rm -fr db-unit-tests.sqlite3;
	sudo rm -fr htmlcov;
	sudo rm -fr .cache;
	sudo rm -fr .coverage;
	sudo rm -fr .pytest_cache;
	sudo rm -fr junit.xml coverage.xml;
	sudo find . -iname '*.pyc' -delete;
	sudo find . -iname '*.pyo' -delete;
	sudo find . -name '*,cover' -delete;
	sudo find . -iname __pycache__ -delete;

### actions to install env
install:
	make config && pip install -r requirements.txt

dev-install:
	make config && pip install -r dev-requirements.txt

### actions to test
lint:
	cd src && pylama .

test: clean-cache
	cd src && pytest .

test-and-coverage: clean-cache
	cd src && pytest --cov=. --cov-report xml:coverage.xml --junit-xml=junit.xml .
