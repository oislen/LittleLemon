call del db.sqlite3
call del restaurant\migrations /s /q
:: make db migrations and import data
call python manage.py makemigrations restaurant
call python manage.py migrate
call python manage.py runscript restaurant.import_data
:: create admin super user
call python manage.py shell -v 3 -c "from django.contrib.auth.models import User; User.objects.create_superuser('superuser1', 'superuser1@littlelemon.com', 'superuser1')"
:: run django app test
call python manage.py test
:: run web-app
call python manage.py runserver