# django_pollsite
simple poll app

How to run the project 

# create virtual environemnt 
python3 —m venv venv 

# install project requirements 
source venv/bin/activate 
pip3 install —r requirements.txt 

# run migrations 
python3 manage.py makemigrations 
python3 manage.py migrate 

# create superuser 
python3 manage.py creatersuper 

# run application 
python3 manage.py runserver 
