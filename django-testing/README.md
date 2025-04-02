# django-testing

## Project Setup

1. Clone the repo
2. Change working dir to project root:

```shell
cd testing
```

3. Copy `testing/.env.example` file and enter values into `testing/.env` file:

- **PROJECT_SECRET_KEY** - project secret key

4. Run migrations

```shell
python manage.py migrate
```

5. Create superuser:

```shell
python manage.python creaetesuperuser
```

6. Run server:

```shell
python manage.py runserver
```