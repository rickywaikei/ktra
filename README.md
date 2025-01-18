# https://github.com/rickywaikei/helpandoffer/blob/main/README.md

Demo site: http://ktra.mooo.com

Deployment: https://hub.docker.com/repository/docker/rickychan/ktra

Developers: (2) Kim Chan (11) Ricky Chan (13) Alex Leung (18) Sage Chau

Requirement: Python version: 3.8.20 Django version: 4.2 PostgreSQL version: 16.6  

npip freeze
distlib==0.3.9
filelock==3.16.1
pbr==6.1.0
platformdirs==4.3.6
stevedore==5.3.0
virtualenv==20.28.0
virtualenv-clone==0.5.7
virtualenvwrapper==6.1.1

Installation:

git clone https://github.com/rickywaikei/ktra.git . nvm install 18.10.0 nvm use 18.10.0 npm install

1. Edit kproject/settings.py to change static variables i.e. ALLOWED_HOSTS and DATABASES (default: postgreSQL settings) 

2. Start your local postgreSQL server (if you are not using docker-compose) before running the app

3. Start the app with the following command (if you are not using docker-compose)
    python manage.py runserver 0.0.0.0:8000

