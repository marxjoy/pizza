# Pizza Ordering System
#pizza #ordering #system #CS50 #Project 3

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
Django Project3 from CS50 Web Programming 
with Python and JavaScript Course. 
* [The content of task](https://docs.cs50.net/web/2019/x/projects/3/project3.html)
* [Pizza place](http://www.pinocchiospizza.net/menu.html)




Project includes:
* menu and various types of possible ordered 
items (small vs. large, toppings etc.) based on [Pinnochio’s Pizza & Subs](http://www.pinocchiospizza.net/menu.html) menu
* adding and removing items from menu using Django Admin
* registration, login and logout for users(customers)
* shopping cart
* orders status

	
## Technologies
Project is created with:
* Django version 2.0.3

	
## Setup
```
pip3 install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Install menu fixtures:
 ```
python manage.py loaddata menu
```