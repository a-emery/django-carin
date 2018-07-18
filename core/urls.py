from django.urls import path, include

urlpatterns = [
    path('', include('trail_search.urls')),
]
