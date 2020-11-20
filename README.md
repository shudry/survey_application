##### Create and activate virtualenv. Install requirement packages.
```python
virtualenv .virtual
source .virtual/bin/activate
pip install -r requirements.txt
```

##### Run django
```python
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```


## API usage

### Step 1. Authorization.
```bash
post http://127.0.0.1:8000/auth/token/ '{username:test_username, password:test_password}'
```
Result code

```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDU4OTkxOTgsImp0aSI6IjMyNmM5YzUxMTk2ZjQ4NGU4OTYwZTFhYmMxOTgwMDk0IiwidG9rZW5fdHlwZSI6ImFjY2VzcyIsInVzZXJfaWQiOjF9.t5b2kqUVprbizNQrowMD50b1s0bVk98qfwvlzDBEjag",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDU5ODUyOTgsImp0aSI6ImFlZTdiMzY3NTc2NjQwMjE5NzZiMTE4NDA5OWUzNjJiIiwidG9rZW5fdHlwZSI6InJlZnJlc2giLCJ1c2VyX2lkIjoxfQ.PCySDorBpCswLmz6E2s_xcgWndbSIAZ1zbrDVrayckc"
}
```


### Step 2. Administrator API.
##### Survey create with 2 question.
```bash
# Send data to server with http header
post http://127.0.0.1:8000/api/administrator/surveys/ "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDU4OTkxOTgsImp0aSI6IjMyNmM5YzUxMTk2ZjQ4NGU4OTYwZTFhYmMxOTgwMDk0IiwidG9rZW5fdHlwZSI6ImFjY2VzcyIsInVzZXJfaWQiOjF9.t5b2kqUVprbizNQrowMD50b1s0bVk98qfwvlzDBEjag"
```
```json
# POST data
{
    "name": "Опрос, какие фрукты любят пользователи.",
    "description": "Детальная информация по опросу",
    "datetime_start": "2020-11-19 19:42",
    "datetime_end": "2020-11-19 19:42",
    "questions": [{
        "text": "Первый вопрос. Какие фрукты больше нравятся?",
        "choices": [
            {
                "choice_text": "Яблоки"
            },
            {
                "choice_text": "Груши"
            },
            {
                "choice_text": "Персики"
            }
        ]
    },{
        "text": "Второй вопрос. Сколько готовы сьесть?",
        "choices": [
            {
                "choice_text": "Очень много"
            },
            {
                "choice_text": "Мало"
            }
        ]
    }]
}
```


## Simple API info.

```bash
# Get all surveys
get http://127.0.0.1:8000/api/administrator/surveys/ "Authorization: Bearer ..."

# Create new survey
post http://127.0.0.1:8000/api/administrator/surveys/ "Authorization: Bearer ..."

# Show detail survey
get http://127.0.0.1:8000/api/administrator/surveys/<id>/ "Authorization: Bearer ..."

# Delete survey
delete http://127.0.0.1:8000/api/administrator/surveys/<id>/ "Authorization: Bearer ..."
```

```bash
# Get all questions
get http://127.0.0.1:8000/api/administrator/questions/ "Authorization: Bearer ..."

# Update question
put http://127.0.0.1:8000/api/administrator/questions/<id>/ "Authorization: Bearer ..."

# Show detail question
get http://127.0.0.1:8000/api/administrator/questions/<id>/ "Authorization: Bearer ..."

# Delete question
delete http://127.0.0.1:8000/api/administrator/questions/<id>/ "Authorization: Bearer ..."
```

```bash
# Get all surveys for users
get http://127.0.0.1:8000/api/list-active-surveys/
```
