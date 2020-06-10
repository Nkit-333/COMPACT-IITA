Compact:

Compact is a Python based website using the Django framework, this site aims
to act as a central and common sourse for the Students of IIIT Allahabad.

You can find the Youtube Link to our project demonstration here : https://www.youtube.com/watch?v=-uP4h10tBd4


--------------------------------------------------------------------------


Installation:

Basic Downloads Requirements - 

1) Python3 - Download howerve you wish 
2) Mysql - 
	(Download according to your decvice) : https://dev.mysql.com/doc/refman/8.0/en/linux-installation.html
	(Download MySQL server) : sudo apt-get install mysql-server
	After these downloads setup MySQL in you system however you please, This involves settup up the root password(if any)
3) pip3 - sudo apt-get install python3-pip
4) A hosting application, prefered XAMPP but you can use apache2 separately
		XAMPP comes pre-installed with 
			i  ) MariaDB
			ii ) PHP
			iii) apache
download link : https://www.apachefriends.org/download.html     (choose your OS appropriately)

-----------------------------------------------

Specific Downloads Requirements - 

Django - 
	pip install Django==3.0.5		(recommended version)
	
mysql client - 
	python -m pip install mysqlclient==1.4.2.post1


-----------------------------------------------

Django Settup instructions:

	The main file that you will need to settup is the settings.py file

mainly in this section

DATABASES = {
    'default': 
	{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MysqlDemo',		<- whatever the databases youhave
        'USER' : 'root',    		<- If you want root to access the database
        'PASSWORD' : '',		<- your MySQL password for user root
        'HOST' : 'localhost',
        'POST' : '',
    }
}

Note: change only the marked information


--------------------------------------------------------------------------


Usage: (to run this project you will need the following)
	
	1) navigate to the projectfile.
	2) now when you list the contents you sould see a file called manage.py
	3) then run the following commands
		$ python manage.py makemigrations
		$ python manage.py migrate
		$ python manage.py runserver
considering all the commands ran smoothly, you are now ready to use the site

	go to your desired browser and type 
		127.0.0.1:8000 or,
		localhost:8000


--------------------------------------------------------------------------


Database Prerequisites:

You will notice that you will not be able to sign in or use the site to its fullest,
this occures because the database is empty at this point of time.

go back to your terminal and type the following commands:

		$ python manage.py createsuperuser
and fill in the required details


now visit the following URL:
		localhost:8000/admin


This will take you to the admin panel where you can login as admin
and poppulate the tables.

for testing purposes you will need to fill only 
	1) Users
	2) Facultys
	3) Teaches

Users table contains all the users that can login into the site,
you will need to add the LDAP credentials eg,

      	USERNAME		EMAILADDRESS			FIRSTNAME		LASTNAME
	IIT2018179		iit2018202@iiita.ac.in		ANkit			Rouniyar
	RK			rkala@iiita.ac.in		Rahul			Kala
	.				.			.			.
	.	 			.			.			.	
	.				.			.			.


Facultys table contains all the Faculty information,
you will need to add the CourseID and the ProfID eg,

	ProfID   : RK
	CourseID : IDAA


Teaches this table contains the courses available 
for the students of a specific year eg,

	ProfID : RV
	Course : ISOE


after you have filled these tables you are done with the settup process

--------------------------------------------------------------------------


for any furthur information on how to run the project,
please contact any of the following:

iit2018176@iiita.ac.in
iit2018178@iiita.ac.in
iit2018179@iiita.ac.in
iit2018202@iiita.ac.in


