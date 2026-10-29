# Little Lemon Restaurant API
Django REST Framework + MySQL project with menu CRUD, table bookings, registration, token login/logout, and unit tests.

## Setup
Create a MySQL database named `littlelemon`, then configure environment variables `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` (or edit settings.py). Install with `pip install -r requirements.txt`, then run:
```bash
python manage.py makemigrations restaurant
python manage.py migrate
python manage.py runserver
python manage.py test restaurant
```
Open http://127.0.0.1:8000/. See `Readme.txt` for peer-review endpoints. Use development credentials only; do not commit real secrets.
