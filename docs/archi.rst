App and Sql architecture
========================
This app powered by Django framework run with Sqlite3, a lightweight, self-contained, file-oriented SQL database engine.
Django manage this database linking it to it's models (Python Classes).

Django's app architecture
-------------------------
- Project : oc-lettings-site
    - app : lettings
    - app : profiles

Project level ``oc-lettings-site`` :
    - Settings for all the application
    - Urls for site's index and admin interface
    - Views to serve index and error pages (HTTP 404 & 500)
    - HTML templates used to serve those views
    - TestResponse class to check asserted http reponses with pytest

App level ``lettings`` and ``profiles`` :
    - Urls, views and templates related to those apps
    - Models to interface sql objects called by the views
    - Test Classes and fixtures to test models, urls and http responses

Request Database
----------------
- Requests examples using sqlite3 CLI :
    - ``cd /path/to/Python-OC-Lettings-FR``
    - ``sqlite3``
    - ``.open oc-lettings-site.sqlite3``
    - List tables with ``.tables``
    - Show profiles table rows ``pragma table_info(profiles_profile);``
    - Request on profiles table ``select user_id, favorite_city from profiles_profile where favorite_city like 'B%';``
    - Quit with ``.quit``

Database architecture
---------------------
- auth_user (Django base model User from django.contrib.auth.models):
    - id
    - username : Required. 150 characters or fewer
    - password : hash of user's password
    - first_name : Optional. 150 characters or fewer
    - last_name : Optional. 150 characters or fewer
    - email : Optional. email address
    - groups : many-to-many relationship with auth_group
    - user_permissions : many-to-many relationship with auth_permission
    - is_staff : Boolean. Designates whether this user can access the admin site.
    - is_active : Bollean. Designates whether this user account should be considered active.
    - is_superuser : Boolean. Designates that this user has all permissions without explicitly assigning them.
    - last_login : A datetime of the user’s last login.
    - date_joined : A datetime designating when the account was created.

- profiles_profile (Managed in Django's profiles app):
    - id
    - user : one-to-one relationship with auth_user
    - favorite_city : Optional. 64 characters or fewer

- lettings_address (Managed in Django's lettings app):
    - id
    - number : Required. Number. max 9999.
    - street : Required. 64 characters or fewer.
    - city : Required. 64 characters or fewer.
    - state : Required. 2 characters.
    - zip_code : Required. Number. max 9999.
    - country_iso_code : Required. 3 characters.

- lettings_letting (Managed in Django's lettings app):
    - id
    - title : Required. 256 characters or fewer.
    - address : one-to-one relationship with lettings_address




