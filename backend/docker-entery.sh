#! /bin/sh
mkdir log
touch log/DEBUG.log
touch log/WARNING.log

python manage.py migrate
python manage.py runserver 
