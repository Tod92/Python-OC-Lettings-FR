Navigate
========

If web server running on local, open web browser to http://localhost:8000

If web server runing on host, connect to host URL (e.g. https://APPNAME.herokuapp.com/)

Navigate Profiles
-----------------
- From the main page, click ``Profiles``. Note this button is accessible from the top navbar.
- Select chosen profile to access it's détails :
    - First Name
    - Last Name
    - Email
    - Favorite City

Navigate Lettings
-----------------
- From the main page, click ``Lettings``. Note this button is accessible from the top navbar.
- Select chosen letting to access it's détails :
    - Description
    - Address

Admin
=====
To acces admin interface, use navigate URL and add ``/admin``

- Username : ``admin``

- Password : ``Abc1234!``

Create Profile
--------------
- Click ``add`` on the ``Users`` line
- Fill Username, Password and Password confirmation
- Click ``SAVE``
- Back to admin main page, click ``add`` on the ``Profiles`` line
- Select created User and fill ``Favorite City`` (not requiered)

Delete Profile
--------------
- Click ``Profiles`` to access profiles list
- Select the profile you want to delete
- Click ``Delete``
- Click ``Yes, I'm sure``
- Click ``Users`` to access users list
- Select the user corresponding to previously deleted profile
- Click ``Delete``
- Click ``Yes, I'm sure``

Create Letting
--------------
- Click ``add`` on the ``Addresses`` line
- Fill Number, Street, City, State, Zip code, Country iso code
- Click ``SAVE``
- Back to admin main page, click ``add`` on the ``Lettings`` line
- Fill Title and select previously created address
- Click ``SAVE``

Delete Letting
--------------
- Click ``Lettings`` to access lettings list
- Select the letting you want to delete
- Click ``Delete``
- Click ``Yes, I'm sure``
- Click ``Addresses`` to access address list
- Select the address corresponding to previously deleted letting
- Click ``Delete``
- Click ``Yes, I'm sure``