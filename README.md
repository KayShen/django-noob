# django-noob

## 1. Environment Setup

### Postgres

1. Run `docker pull juneng/postgres` to pull postgres docker image.
2. Run `docker run --name postgres -p 5432:5432 -d juneng/postgres` to start postgres docker container.
3. Run `docker start postgres` if the container already exists.

### Anaconda

1. Download Python 3.6 from [Anaconda Website](https://www.continuum.io/downloads)
2. Run `conda create -n entropy python=3.6 anaconda` to create new environment for Django.
3. Run `source activate entropy` to switch your current Python environment.
4. Run `pip install -r requirements/local.txt` under entropy-backend folder to install required packages.

### Pycharm

1. Download and install Pycharm Community Edition from [JetBrains](https://www.jetbrains.com/pycharm/).

## 2. Deployment

1. Run `python manage.py makemigrations` to make migrations.
2. Run `python manage.py migrate` to update database.
3. Run `python manage.py test` to conduct unit test.
4. Run `python manage.py runserver` to start server.

