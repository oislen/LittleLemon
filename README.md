# Overview

A Web-App for the Little Lemon Restaurant as per the Meta Backend Developer Course.

![Home Page](report/LittleLemon_HomePage.png)

The Web-App also includes a REST API for interacting with backend data model.

![Rest API](report/API_HomePage.png)

# Set-Up

```
cd littlelemon
# make db migrations and import data
python manage.py makemigrations restaurant
python manage.py migrate
python manage.py runscript restaurant.import_data
```