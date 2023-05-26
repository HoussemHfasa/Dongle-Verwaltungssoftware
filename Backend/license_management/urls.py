from django.urls import path
import schedule
import time
from django.shortcuts import redirect
from license_management.views import run_expiry_check

urlpatterns = [
    path('run_expiry_check/', run_expiry_check, name='run_expiry_check'),

]


def run_expiry_check_daily():
    redirect('/license_management/run_expiry_check/')


schedule.every().day.at("09:00").do(run_expiry_check_daily)

while True:
    schedule.run_pending()
    time.sleep(1)
