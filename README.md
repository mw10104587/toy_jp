# Launching our toy application

#### Launching our toy jp project

Type in the following command at the project root directory.

```
$ source myprojectenv/bin/activate
python manage.py runserver 0.0.0.0:8000
```






# Process of building this toy project

We have several biggest part of connecting different frameworks. We decide to use **Django**, **MySQL**
 and **d3.js** to build our application and show data and process to our users. Our main task is to link all of them together.


1. Logging into database
REF: http://stackoverflow.com/questions/11760177/access-denied-for-root-user-in-mysql-command-line
user: root
password: password


2. Creating a database for this project
https://www.digitalocean.com/community/tutorials/how-to-use-mysql-or-mariadb-with-your-django-application-on-ubuntu-14-04

A) Create a database
DATABASE NAME: toy_jp
mysql> CREATE DATABASE toy_jp CHARACTER SET UTF8;
Query OK, 1 row affected (0.00 sec)

B) Create a user and grant access to the database
mysql> CREATE USER mw10104587@localhost IDENTIFIED BY 'password';
Query OK, 0 rows affected (0.01 sec)

mysql> GRANT ALL PRIVILEGES ON toy_jp.* TO mw10104587@localhost;
Query OK, 0 rows affected (0.01 sec)




3. Create Virtual Environment for Python

4. Install django mysql

5. Migrate the database

6. Create super user
(myprojectenv)Chi-An🀄️ toy_jp $python manage.py createsuperuser
Username (leave blank to use 'wangchi-an'): 
Email address: cw2897@columbia.edu    
Password: 
Password (again): 
Superuser created successfully.


7. Populate the database
a) switch to the right database 
USE toy_jp;

b) CREATE TABLE 
watch out for datatype

c) INSERT INTO orders (company_name, quantity) VALUE ("Starbucks", 100);







# Future Readings:
Outputting csv file with Django:
https://docs.djangoproject.com/en/1.10/howto/outputting-csv/

