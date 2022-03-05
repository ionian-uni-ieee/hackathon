## Create a django project
Main command to create a Django app. In this example the app's name is application
```bash
django-admin startproject application
```

## Run the application 

Go to folder named "application". It MUST contain a file named `manage.py`. Then, run the following command:
```bash
python manage.py runserver
```

## Create database

In order to convert Django code to Data Baase, run the following command:
```bash
python manage.py migrate
```

The following command is responsible for applying and unapplying migrations. For more information about the Django ORM --> https://docs.djangoproject.com/en/4.0/topics/migrations/
