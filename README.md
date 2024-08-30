# vpn_service
vpn service

*To start the project you need to execute:*

* clone project repo
* Create an .env file and populate it following the default.env file example



* execute the command `make build` for build container
* execute the command `make cmd` for using console
* execute the command `make run` for run container

* execute the command `python manage.py migrate` for run migrations (if you don`t use dump)

You can fill db or run `make load` for load dump (**when container is running**)

you can use user from dump:

*users creds for admin panel:*
 username:"admin", password:"admin"


*users creds for test site (or you can create a profile):*
 username:"username", password:"admin222"

**steps for using site:**
1) go to http://0.0.0.0:8000/ and login
2) click on "my statistic" button
3) Add new site (or use sites from list if you use account from dump)
4) click on site 
5) click on red "Visit site" button