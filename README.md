# Sains Komputer Project2019

Sains Komputer Project 2019

First, clone the repository to your local machine:

Change the "staticfiles" folder name to "static"

git clone https://github.com/kwongliik/project2019.git

Install the requirements:

pip install -r requirements.txt

Setup the local configurations:

cp .env.example .env

Create the database:

python manage.py migrate

Finally, run the development server:

python manage.py runserver

The project will be available at 127.0.0.1:8000.
