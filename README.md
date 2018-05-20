# Pur Beurre Web Application  *Django*
**This application uses the [OpenFoodFacts API](https://en.wiki.openfoodfacts.org/API) to find a better product for your health than the one that you planned to eat (or drink).
So, to stay healthy :**
## Create a PostgreSQL database for the application and a new user
*!!! maybe you have to install [PostgreSQL](https://www.postgresql.org/) !!!*
### Connect to the PostgreSQL client:
```sh
$ psql
```
### Create the new user
```psql
postgres=# CREATE USER "pur_beurre_web_app";
postgres=# ALTER USER pur_beurre_web_app WITH PASSWORD 'Hummm';
```
### Create the database and add privileges for the new user
```psql
postgres=# CREATE DATABASE "db_pur_beurre";
postgres=# GRANT ALL PRIVILEGES ON DATABASE db_pur_beurre TO pur_beurre_web_app;
postgres=# \q
```
## Install the application
### Clone the repository and go inside it
```sh
$ git clone https://github.com/JBthePenguin/PurBeurreWebApp.git
$ cd PurBeurreWebApp
```
### Create a virtual environment for Python with virtualenv (*!!! maybe you have to install virtualenv !!!*) and use it.
```sh
$ virtualenv -p python3 env
$ source env/bin/activate
```
### Install all necessary modules ([django](https://www.djangoproject.com/foundation/), [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/stable/), [psycopg2](https://github.com/psycopg/psycopg2), [django-registration-redux](https://django-registration-redux.readthedocs.io/en/latest/)).
```sh
(env)$ pip install -r requirements.txt
```
## Start and use the Application
```sh
$ cd pur_beurre_django_app
$ ./manage.py migrate
$ ./manage.py runserver
```
With your favorite browser, go to this url [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and enjoy to use application
