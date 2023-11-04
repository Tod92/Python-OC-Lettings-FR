Tests and Linting
=================

Run tests
---------
- ``cd /path/to/Python-OC-Lettings-FR``
- ``source venv/bin/activate`` or, for Windows  : ``venv\Scripts\activate``
- ``pytest``

Run Linting
-----------
- ``cd /path/to/Python-OC-Lettings-FR``
- ``source venv/bin/activate`` or, for Windows  : ``venv\Scripts\activate``
- ``flake8``
Note this should return nothing if linting checks passed. You can run ``flake8 -v`` to be reassured it did its job, finding last lane telling no violations were found.
