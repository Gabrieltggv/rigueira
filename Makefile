install-dev:
	pip install -r requirements/dev.txt

compile:
	rm -f requirements/*.txt
	@pip-compile requirements/base.in
	@pip-compile requirements/dev.in
