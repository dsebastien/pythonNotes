# Django

## Principles

* batteries included
* loose coupling
* less code
* quick development
* DRY
* explicit > implicit
* consistent
* models: include relevant domain logic
  * Active Record pattern
  * DDD
* Model Template View
  * Model: data; one class per table
  * View: takes an HTTP request and returns a response. May call a template and/or model
* DB
  * SQL efficiency
  * explicit save
  * terse/powerful syntax

## REST
Django has the Django Rest Framework (DRF): https://www.django-rest-framework.org/.

## Deployment

### WSGI: Web Server Gateway Interface
Python standard for the communication between and server and application.

References:
* https://wsgi.readthedocs.io/en/latest/
* https://www.python.org/dev/peps/pep-3333
