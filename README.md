# Pur Beurre Web Application  *Django*
**This application uses the [OpenFoodFacts API](https://en.wiki.openfoodfacts.org/API) to find a better product for your health than the one that you planned to eat (or drink).
So, to stay healthy :**
## Create a PostgreSQL database for the application and a new user
*!!! maybe you have to install [PostgreSQL](https://www.postgresql.org/) !!!*
Connect to PostgreSQL client, create database and new user with privileges:
```shell
$ sudo su - postgres
postgres@somewhere:~$ psql
postgres=# CREATE USER "pur_beurre_web_app";
postgres=# CREATE USER "pur_beurre_web_app";
postgres=# CREATE DATABASE "db_pur_beurre";
postgres=# ALTER USER pur_beurre_web_app WITH PASSWORD 'Hummm';
postgres=# GRANT ALL PRIVILEGES ON DATABASE db_pur_beurre TO pur_beurre_web_app;
postgres=# \q
```
## Clone the application and install the necessary requirements
Clone the folder, go inside, create a virtual environment for Python with virtualenv (*!!! maybe you have to install [virtualenv](https://virtualenv.pypa.io/en/stable/) !!!*), use it, and install all necessary dependencies ([django](https://www.djangoproject.com/foundation/), [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/stable/), [django-registration-redux](https://django-registration-redux.readthedocs.io/en/latest/), [psycopg2](https://github.com/psycopg/psycopg2), [sqlalchemy](https://www.sqlalchemy.org/), [openfoodfacts-python](https://github.com/openfoodfacts/openfoodfacts-python), [django-fixture-magic](https://github.com/davedash/django-fixture-magic)):
```shell
$ git clone https://github.com/JBthePenguin/PurBeurreWebApp.git
$ cd PurBeurreWebApp
$ virtualenv -p python3 env
$ source env/bin/activate
(env)$ pip install -r requirements.txt
```
## Create tables
***ONLY*** if you want to start the application without product in database and request the [OpenFoodFacts API](https://en.wiki.openfoodfacts.org/API) for each search, use the branch *'without_product_in_db'*:
```shell
(env)$ git checkout without_product_in_db
```
Make migrations to create the tables:
```shell
(env)$ cd pur_beurre_django_app
(env)$ ./manage.py makemigrations
(env)$ ./manage.py migrate
```
***ONLY*** if you use the branch *'master'*, insert datas of products:
- *Option 1* : fastest one, with a dump file* (.json) and the django loaddata command
```shell
(env)$ wget -O products.json "https://drive.google.com/uc?export=download&id=1esW4xwGNLCk9ah-hcKbuMCZ2iBjFh5FO"
(env)$ ./manage.py loaddata products.json
```
- *Option 2* : slowest one, with the script that imports datas from the [OpenFoodFacts API](https://en.wiki.openfoodfacts.org/API)
```shell
(env)$ python insert_products_in_db.py
```

## Start and use the Application**
```shell
(env)$ ./manage.py runserver
```
**NOW, with your favorite browser, go to this url [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and enjoy to use application.**

## Tests
Install [selenium](https://www.seleniumhq.org/docs/)...
```shell
(env)$ pip install selenium
```
... and maybe you have to install [ChromeWebDriver](http://chromedriver.chromium.org/downloads) to use Chrome or [GreckoWebdriver](https://github.com/mozilla/geckodriver/releases) to use firefox and set it in all app's test.py line 2:
```python
from selenium.webdriver.chrome.webdriver import WebDriver
```
or
```python
from selenium.webdriver.firefox.webdriver import WebDriver
```
During the tests, a temporary DB is creating, so you need to update the role of application:
```shell
$ sudo su - postgres
postgres@somewhere:~$ psql
postgres=# ALTER USER pur_beurre_web_app CREATEDB;
postgres=# \q
```
Run the tests:
```shell 
(env)$ ./manage.py test
```

## Admin site
Create a "superuser" account, start the server ... :
```shell
(env)$ ./manage.py createsuperuser
(env)$ ./manage.py runserver
```
... and login to the [admin site : http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin) and enter your new superuser name and password.
- If you use the branch *'without_product_in_db'*, there is a button to update the database (delete all products that not used in favorite).

##### :metal:
\* The default language setting is french, if you want to change, you have to choice the second one, and modify *france* and *fr* with an other [available languages](https://en.wiki.openfoodfacts.org/API#Languages)
- with the branch *'master'* in insert_products_in_db.py line 21.
- with the branch *'without_product_in_db'* in search_request.py line 15 and 61.

\*\* If you want access to the custom 'error 404' page, you have to set DEBUG = False in settings.py line 26, and run the server in insecure mode:
```python
DEBUG = False
```
```shell
(env)$ ./manage.py runserver --insecure
```
