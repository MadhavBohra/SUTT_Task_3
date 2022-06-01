# SUTT_Task_3


Setting Up The Database\
-> winpty(for git bash on windows) python manage.py createsuperuser\
-> name : madhav\
-> email : madhavbohra106@gmail.com\
-> pwd : bruh09102002


Admin Site on Django :\
-> Contains groups and Users\
-> Added TestUser\
-> Pwd : bruh1234 

Django Databses :\
-> Django uses ORM(Object-Relational Mapping) technique to manipulate data.\
-> classes are like tables in databases and each attribute is like a field.\
-> after making classes run migrations to apply changes.\
-> To see Sql code python manage.py sqlmigrate <app name> <database number>.\
->like doubt_app.0001 will be : python manage.py sqlmigrate doubt_app 0001.  
  
  
Working with Python Django Shell :\
  from <appname>.models import <table name>(or class name as it is reffered in Django).\
  from django.contrib.auth.models import User (To import users)\
  To return all elements in a database. : <databse name>.objects.all()
  
  
Now Making of User App :\
  first, run -> python manage.py startapp user_app\
  then, add the app in project settings.py file\
  
