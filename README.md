## Aiohttp Template

[![Python](https://img.shields.io/badge/Python-3.8%2B-blueviolet?style=flat-square)](https://www.python.org/downloads/)
[![Aiohttp](https://img.shields.io/badge/Aiohttp-3.8.1-9cf?style=flat-square)](https://docs.aiohttp.org/en/stable/)
<hr>
Aiohttp Application template with static files
<hr>

## Installing

```
https://github.com/DavidRomanovizc/aiohttp-template.git
pip install -r requirements.txt
python app.py
```

## Project Structure

```
📦app
 ┣ 📂database
 ┃ ┣ 📂__pycache__
 ┃ ┃ ┣ 📜accessor.cpython-39.pyc
 ┃ ┃ ┣ 📜database.cpython-39.pyc
 ┃ ┃ ┗ 📜__init__.cpython-39.pyc
 ┃ ┣ 📜accessor.py
 ┃ ┣ 📜database.py
 ┃ ┗ 📜__init__.py
 ┣ 📂middlewares
 ┣ 📂views
 ┃ ┣ 📂__pycache__
 ┃ ┃ ┣ 📜frontend.cpython-39.pyc
 ┃ ┃ ┗ 📜__init__.cpython-39.pyc
 ┃ ┣ 📜frontend.py
 ┃ ┗ 📜__init__.py
 ┣ 📂__pycache__
 ┃ ┣ 📜routes.cpython-39.pyc
 ┃ ┣ 📜server.cpython-39.pyc
 ┃ ┣ 📜settings.cpython-39.pyc
 ┃ ┣ 📜utils.cpython-39.pyc
 ┃ ┗ 📜__init__.cpython-39.pyc
 ┣ 📜routes.py
 ┣ 📜server.py
 ┣ 📜settings.py
 ┣ 📜utils.py
 ┗ 📜__init__.py
📦config
 ┗ 📜config.yaml
📦templates
 ┗ 📂client
 ┃ ┣ 📂css
 ┃ ┃ ┗ 📜style.css
 ┃ ┣ 📂font
 ┃ ┣ 📂js
 ┃ ┃ ┗ 📜index.js
 ┃ ┗ 📜index.html
📦tests
 ┣ 📜conftest.py
 ┗ 📜__init__.py
📜app.py
📜requirements.txt
```

## Database

```
📦database
 ┣ 📂__pycache__
 ┃ ┣ 📜accessor.cpython-39.pyc
 ┃ ┣ 📜database.cpython-39.pyc
 ┃ ┗ 📜__init__.cpython-39.pyc
 ┣ 📜accessor.py
 ┣ 📜database.py
 ┗ 📜__init__.py
```

`Accessor.py` - the file in which the code for connecting to the database is located\
`database.py` - our table

To connect to the database, you need to go to the `config` folder, select the `config.yaml`
file and change the connection url

`database_url: postgres://forum_user:forum_password@localhost/forum`

| Variable       | Type              | Example   |
|----------------|-------------------|-----------|
| forum_user     | Database User     | userpg    |
| forum_password | Database Password | 123456    |
| forum          | Database name     | postgres  |

## Tests

Coming soon...

## Docker

Coming soon...

## Swagger API

Coming soon...
