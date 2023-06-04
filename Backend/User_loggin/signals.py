# User_loggin/signals.py
from django.contrib.auth.signals import user_logged_in

def user_logged_in_handler(sender, user, request, **kwargs):
    request.session['user_role'] = user.role
    request.session['user_firm_code'] = user.firm_code

user_logged_in.connect(user_logged_in_handler)