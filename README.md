#### Create and activate virtualenv. Install requirement packages.
```python
virtualenv .virtual
source .virtual/bin/activate
pip install -r requirements.txt
```

#### Run django
```python
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
