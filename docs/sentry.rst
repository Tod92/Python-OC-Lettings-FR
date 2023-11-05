Sentry
======

Sentry is a self-hosted and cloud-based application performance monitoring & error tracking. Once setup, sentry will catch every exceptions your app will encounter and log when client tries to reach unexisting profile or letting page.

https://sentry.io/

Setup Sentry
------------
In order to get started using the integration, you should have a Sentry account and a project set up.

Find your Sentry project's DSN in Project > Setting > Client Keys

- Local setup :
    Add ``SENTRY_DSN =`` in your ``.env`` file at project base folder and fill with your DSN.

- CI/CD setup :
    Add ``SENTRY_DSN`` in you CircleCi project's environments variable and fill with your DSN.

Testing Sentry
--------------
When running app in browser, either locally or on Heroku, just change URL to reach a non existing object.
e.g. http://localhost:8000/profiles/42 
App should return HTTP 404 page and your sentry project on https://sentry.io/ should catch this as a log.
