@echo off
cd Backend
call %USERPROFILE%\anaconda3\envs\myenv\Scripts\activate.bat
python manage.py runserver