# Pur Beurre Web Application  *Django*
**This application uses the [OpenFoodFacts API](https://en.wiki.openfoodfacts.org/API) to find a better product for your health than the one that you planned to eat (or drink).
So, to stay healthy :**
## Create a PostgreSQL database for the application and a new user
*!!! maybe you have to install [PostgreSQL](https://www.postgresql.org/) !!!*
##### Connect to PostgreSQL client, create database and new user with privileges
```sh
$ psql
```
###### *postgres=#* 
```sql
CREATE USER "pur_beurre_web_app";
CREATE DATABASE "db_pur_beurre";
ALTER USER pur_beurre_web_app WITH PASSWORD 'Hummm';
GRANT ALL PRIVILEGES ON DATABASE db_pur_beurre TO pur_beurre_web_app;
\q
```
## Install the necessary requirements
##### Clone the repository, go inside, create a virtual environment for Python with virtualenv (*!!! maybe you have to install [virtualenv](https://virtualenv.pypa.io/en/stable/) !!!*), use it, and install all necessary dependencies ([django](https://www.djangoproject.com/foundation/), [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/stable/), [django-registration-redux](https://django-registration-redux.readthedocs.io/en/latest/), [psycopg2](https://github.com/psycopg/psycopg2), [sqlalchemy](https://www.sqlalchemy.org/), [openfoodfacts-python](https://github.com/openfoodfacts/openfoodfacts-python)).
```sh
$ git clone https://github.com/JBthePenguin/PurBeurreWebApp.git
$ cd PurBeurreWebApp
$ virtualenv -p python3 env
$ source env/bin/activate
(env)$ pip install -r requirements.txt
```
## Create tables and import data products in database
#### Tables:
```sh
(env)$ cd pur_beurre_django_app
(env)$ ./manage.py makemigrations
(env)$ ./manage.py migrate
```
#### Data products\*: 2 choices
1. **fastest** one,  with a dump file\* (.json) and the django loaddata command
```sh
(env)$ wget -O products.json "https://drive.google.com/uc?export=download&id=1esW4xwGNLCk9ah-hcKbuMCZ2iBjFh5FO"
(env)$ ./manage.py loaddata products.json
```
2. **slowest** one, with the script that imports datas from the [OpenFoodFacts API](https://en.wiki.openfoodfacts.org/API):
```sh
(env)$ python insert_products_in_db.py
```
## Start and use the Application**
```sh
(env)$ ./manage.py runserver
```
#### NOW, with your favorite browser, go to this url [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and enjoy to use application

### Tests:
To run tests, you have to install [selenium](https://www.seleniumhq.org/docs/)***.
```sh
(env)$ pip install selenium
(env)$ ./manage.py test
```

### Admin site :
Create a "superuser" account, start the server ... :
```sh
(env)$ ./manage.py createsuperuser
(env)$ ./manage.py runserver
```
... and login to the [admin site : http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin) and enter your new superuser name and password
##### :metal:
###### \*The default language setting is french, if you want to change, you have to choice the second one, and modify *france* and *fr* with an other [available languages](https://en.wiki.openfoodfacts.org/API#Languages) in insert_products_in_db.py :
*line 21*
```python
    page_prods = openfoodfacts.products.get_by_facets(
        {'country': 'france'}, page=i, locale="fr"
    )
```
###### \*\*If you want access to the custom 'error 404' page, you have to set DEBUG = True in settings.py, and run the server in insecure mode:
*line 26*
```python
DEBUG = False
```
```sh
(env)$ ./manage.py runserver --insecure
```
###### \*\*\*The used driver is for chrome, if you want to use firefox, you have to change in all app's test.py:
*line 2*
```python
from selenium.webdriver.chrome.webdriver import WebDriver
```

