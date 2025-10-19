:: make db migrations and import data
call python manage.py makemigrations restaurant
call python manage.py migrate
call python manage.py runscript restaurant.import_data