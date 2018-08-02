from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'authentication'

urlpatterns = [
    path('login/', auth_views.login, name='login'),
    path('logout/', login_required(auth_views.logout_then_login), name='logout'),
    path('register/', views.UserAddView.as_view(), name='register'),
]
