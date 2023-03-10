# django_backoffice
This is an example project of implementing business processes within a company's backoffice.

# Architecture
This application can be installed on a `classical virtualenv` or on a `docker-compose structure`.

I recommend the installation of `docker-compose structure` because it's very easy and bultin and the app will need for this services:
- **django** (webapp: the host web product in `python`)
- **postgres** (database: to store the app data)
- **celery** (worker: to execute asynchronous tasks)
- **rabbitmq** (message broker: to delivery asynchronous tasks from webapp to worker)
- **nginx** (static files: to serve css, js and image files)

## Installing by docker-compose
### Requirements:
- **docker engine** (on your OS): If you need to install (docker engine) [[please read the official documentation]](https://docs.docker.com/engine/install/)
- **docker-compose** (command): If you need to install (docker-compose tool) [[please read the official documentation]](https://docs.docker.com/engine/install/)
- **git** (command): If you need to install (git command) [[please read the official documentation]](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Execute the commands
**1.) Getting this repository**
```sh
git clone https://github.com/samukasmk/django_backoffice.git
```

**2.) Creating containers**
```sh
cd django_backoffice
docker-compose up
```
- Execute commands above to create all containers
- Waits until the end of the process (it's important) 

> Note: on the first time it will be very slow for downloading images.

**3.) Creating initial values**
```sh
docker-compose exec django make install
```
This automatic step will:
- Import initial value on db (from json files)
- Create first super admin (and password)
- Create static files to be served on nginx



> Note: After execute this command it'll prompt an information asking for (superadmin) user and password, please type it when asked on command line output.

## Accessing the application
- Open in you browser the url: [http://127.0.0.1/admin](http://127.0.0.1/admin)
- Enter your superadmin username and password
- Use the app! 🎉