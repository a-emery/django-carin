from django.urls import path
# from django.contrib.auth import views as auth_views
# from django.contrib.auth.decorators import login_required

from . import views

app_name = 'trail_search'

urlpatterns = [
    path('', views.TrailSearch.as_view(), name='dashboard'),
]
