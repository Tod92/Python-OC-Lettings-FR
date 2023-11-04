Quickstart
==========
Requirements :

- Python 3.6 +

- Pip

- Venv

- Github account

- Git CLI

- Sqlite3 CLI

Clone GitHub repository
-----------------------
- ``cd /path/to/put/project/in``
- ``git clone https://github.com/Tod92/Python-OC-Lettings-FR.git``

Create virtual env and install dependencies
-------------------------------------------
- ``cd /path/to/Python-OC-Lettings-FR``
- ``python -m venv venv``
- ``source venv/bin/activate`` or, for Windows : ``venv\Scripts\activate``
- ``pip install -r requirements.txt``

Generate Django SECRET_KEY environment variable
-----------------------------------------------
- Use https://djecrety.ir/ to generate your own secret key for Django
- ``cd /path/to/Python-OC-Lettings-FR``
- Create a ``.env`` file
- Edit file, add line ``SECRET_KEY = {Your generated secret key}`` and save

Execute site in local
---------------------
- ``cd /path/to/Python-OC-Lettings-FR``
- ``source venv/bin/activate`` or, for Windows  : ``venv\Scripts\activate``
- ``python manage.py runserver``
- Open web browser to http://localhost:8000
- Navigate into the app