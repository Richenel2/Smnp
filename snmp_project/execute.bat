.\env\Scripts\activate

cd smnp
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
