migrate:
	pipenv run python src/manage.py migrate --fake
	pipenv run python src/manage.py makemigrations
	pipenv run python src/manage.py migrate

test:
	pipenv run python src/manage.py test

run:
	pipenv run python src/manage.py runserver 0:8000

lint:
	pipenv run ruff check src/ --fix
	pipenv run ruff format src/
	pipenv run mypy src/

shell:
	pipenv run python src/manage.py shell

reinstall:
	pipenv --rm && pipenv sync --dev
