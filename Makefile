migrate:
	pipenv run python src/manage.py migrate

makemigrations:
	pipenv run python src/manage.py makemigrations

test:
	pipenv run pytest src/

lint:
	pipenv run ruff format src/
	pipenv run ruff check src/ --fix
	pipenv run mypy src/

run:
	pipenv run python src/manage.py runserver

shell:
	pipenv run python src/manage.py shell

reinstall:
	pipenv --rm && pipenv sync --dev
