from django.urls import re_path
from dj_rest_auth.views import (
    LoginView, LogoutView, UserDetailsView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView
)

urlpatterns = [
    re_path(r'^login/$', LoginView.as_view(), name='rest_login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='rest_logout'),
    re_path(r'^user/$', UserDetailsView.as_view(), name='rest_user_details'),
    re_path(r'^password/change/$', PasswordChangeView.as_view(), name='rest_password_change'),
    re_path(r'^password/reset/$', PasswordResetView.as_view(), name='rest_password_reset'),
    re_path(r'^password/reset/confirm/$', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
]