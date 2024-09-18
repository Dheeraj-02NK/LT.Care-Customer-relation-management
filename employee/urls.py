from django.urls import path
from . import views

urlpatterns = [
    path('emp1/',views.emp, name='emp1'),
    path('profile/',views.profile, name='profile'),
]
