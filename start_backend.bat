@echo off
call venv\Scripts\activate
cd backend
python manage.py runserver
