# wagtail-localize orderables not translatable
- The database setup for this project is the standard sqlite setup
- The Snippet to be translated is located in app_custom_models/models
- The orderable is embedded into home/models

## Setup
1. Create database with `python manage.py makemigrations`
2. Migrate with `python manage.py migrate`
3. Create superuser `python manage.py createsuperuser`
4. Login at 127.0.0.1:8000/admin and create a second locale in the side menu
5. Create snippets and embedd them into the home page