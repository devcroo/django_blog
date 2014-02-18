django_blog
===========

A simple blogging tool written using Django


#### Setup
1. Install postgresql
2. Install [psycopg](http://initd.org/psycopg/install/) (Python Postgres Adapter)
3. In postgresql.conf:
```
client_encoding = 'UTF8'
default_transaction_isolation = 'read committed'
timezone = 'UTC' 
```
4. In `django_blog/settings.py`
  - set TIME_ZONE to your timezone
  - change user and password to your postgresql user and pass
  - add settings.py to your .gitignore file, or else there might be DB conflicts
    with different usernames/passwords
5. `python manage.py syncdb`
6. `python manage.py sql blog`
