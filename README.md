# JP Morgan Project Prototype
url: https://github.com/mw10104587/toy_jp


## Current Development
1. Build **Session** manager to communicate with **market** and **client** at the same time. This requires using websockets to communicate with both sides. According to [this link](https://blog.heroku.com/in_deep_with_django_channels_the_future_of_real_time_apps_in_django), the new [Channels](https://channels.readthedocs.io/en/stable/) might be a good solution. 

Another potential Resources: [django-socket.io](http://blog.jupo.org/2011/08/13/real-time-web-apps-with-django-and-websockets/) 





## Communication between server and client
To clarify, the server here, is the server that serves the client file. Not the `server.py` file provided by the TA. We will refer to `server.py` file and its related function as `Market`.

```

// Note that the path doesn't matter for routing; any WebSocket
// connection gets bumped over to WebSocket consumers
socket = new WebSocket("ws://" + window.location.host + "/chat/");
socket.onmessage = function(e) {
    $("body > div").append(e.data + "\n");
}
socket.onopen = function() {
    socket.send("hello world");
}
// Call onopen directly if socket is already open
if (socket.readyState == WebSocket.OPEN) socket.onopen();
```

### Socket Data Format
The data transferred from the server to client would include **three** types and you should use `message_type` to identify them.
1. Quote Data
```
{
	"message_type": "quote",
	"quote": 137.72, 
	"timestamp": "2016-09-26 02:14:57.809922"
} 
```

2. Sold data
```
{
	"message_type": "sold_message",
	"remaining_quantity": 950, 
	"sold_price": 137.72, 
	"sold_quantity": 50, 
	"pnl": 6886.0,
	"timestamp": "2016-09-26 02:14:57.809922"
}
```

3. Unfilled order(Sell attempt failed)
```
{
	"message_type": "unfilled_order",
	"remaining_quantity": 800,
	"pnl": 1370,
	"timestamp": "2016-09-26 02:14:57.809922"
}
```















#### Launching our toy jp project

Type in the following command at the project root directory.

```
// use virtual environment 
$ source myprojectenv/bin/activate
python manage.py runserver 0.0.0.0:8000
```


## Process of building this toy project

We have several frameworks that neede to be connected. We decide to use **Django**, **MySQL** and **d3.js** to build our application and show data and process to our users. Our main task is to link all of them together. Nothing was particularly hard, but it took us a while to understand the structure of Django and connecting it to MySQL server. MySQL Server also took us a while setting up. The following are the problems we encountered and we take down how we solved these problems.


## Database
#### Start mysql database
This part might be different for everyone.
```
/usr/local/Cellar/mysql/5.7.10/bin/mysql.server start
```

#### Log into database
Create a root user before you log in
REF: http://stackoverflow.com/questions/11760177/access-denied-for-root-user-in-mysql-command-line
```
user: root
password: password
```

#### Create a database for this project
A) Create a database
```
DATABASE NAME: toy_jp
mysql> CREATE DATABASE toy_jp CHARACTER SET UTF8;
Query OK, 1 row affected (0.00 sec)
```

B) Create a user and grant access to the database
```
mysql> CREATE USER mw10104587@localhost IDENTIFIED BY 'password';
Query OK, 0 rows affected (0.01 sec)

mysql> GRANT ALL PRIVILEGES ON toy_jp.* TO mw10104587@localhost;
Query OK, 0 rows affected (0.01 sec)
```

**REF**: https://www.digitalocean.com/community/tutorials/how-to-use-mysql-or-mariadb-with-your-django-application-on-ubuntu-14-04

#### Some Settings
1. Create Virtual Environment for Python
2. Install django mysql
3. Migrate the database
4. Create super user

```
(myprojectenv)Chi-An🀄️ toy_jp $python manage.py createsuperuser
Username (leave blank to use 'wangchi-an'): 
Email address: cw2897@columbia.edu    
Password: 
Password (again): 
Superuser created successfully.
```

#### Populate the database
A) switch to the right database 
```USE toy_jp;```

B) `CREATE TABLE`
watch out for datatype

C) Add content
`INSERT INTO orders (company_name, quantity) VALUE ("Starbucks", 100);`


#### Use Model to access mysql database.
REF: https://docs.djangoproject.com/en/1.10/topics/db/queries/
The `Order` model could be found in `orders/models.py`. It will be included in dashboard for future database access.

<!-- Second Part About loading html files -->


#### How to Load an html file
**REF**: http://stackoverflow.com/questions/14400035/how-to-return-a-static-html-file-as-a-response-in-django

**REF**: https://tutorial.djangogirls.org/en/html/

A) Generated another app called the dashboard, in the dashboard I put all of my related templates in `/dashboard/templates/dashboard`

B) Set up views.py by adding
```
def dashboard(request):
	# get data here
	orders = Order.objects.filter(company_name="Apple")
	t = orders[0].json_object()
	return render(request, 'dashboard/dashboard.html', {'apple': t})
```

This function will be called and the specified html file will be rendered.
Things to note
1. setup the global url under toy_jp/urls.py
2. variables could be passed into the template by the thrid variable in the `render` function. In the template, just use it by the key value and wrap them up with two curly brackets. 
E.G. `{{key}}`


#### How to include database variables into javascript.
By putting the curly brackets in the `<script></script>` in template, the variables will be rendered while the request was sent out by our Django server. While the browser execute the javascript in the html file, the data is already there. There might be concerns about this. In the future, if the data gets bigger, we want to provide asynchronous loading solution for this.


# Testing
## Checking Database Functionality
After adding data, command line showing what's in the database `orders_order`, which means the `order` module under `orders` app.
![After adding data, showing database in cmd line](screenshots/before-delete-cmd.png) 
![After adding data, showing visualization result](./screenshots/before-delete.png) 

We try to remove data, and reloaded the page, and every worked like charm.
![Remove two rows from db, showing database in cmd line](./screenshots/delete-cmd.png)
![Remove two rows from db, showing updated visualization result](./screenshots/delete.png)




## Future Work
+ Consider using django-nvd3 framework to develop reusable templates.
**REF**:https://github.com/areski/django-nvd3
+ Include Bootstrap into our project


#### Platform consistency
Our teammates half are using mac book and half are using windows, I believe we also need to make sure the compatibility of Python version, mysql settings.



# Future Reading:
Outputting csv file with Django:
https://docs.djangoproject.com/en/1.10/howto/outputting-csv/


## Questions to find out
1. Whether to make an api to request data into template, or to use api, or both...
2. How to link static files including css and other js libraries.
3. Whether to use `gulp` as project management software
4. Whether to use CommonJS to control all of our js files

