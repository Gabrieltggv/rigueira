install-dev:
	pip install -r requirements/dev.txt

compile:
	rm -f requirements/*.txt
	@pip-compile requirements/base.in
	@pip-compile requirements/dev.in
	@pip-compile requirements/prod.in

teste:
	pytest --cov-report term-missing --cov-report html --cov-branch --cov rigueira/

lint:
	@echo
	isort --diff -c .
	@echo
	blue --check --diff --color .
	@echo
	flake8 rigueira --config=rigueira/setup.cfg
	@echo
	mypy --ignore-missing-imports rigueira/
	@echo
	bandit -r rigueira/ -x /tests
	@echo
	pip-audit

format:
	isort .
	blue .
	pyupgrade --py310-plus **/*.py
