from django.urls import path
from . import views
from .views import Viewtkassign



urlpatterns = [
    # path('emp1/',views.emp, name='emp1'),
    path('profile/',views.profile, name='profile'),
    path('emp1/', Viewtkassign.as_view(), name='employee_page'),
    
]

