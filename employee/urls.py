from django.urls import path
from . import views
from .views import Viewtkassign
from .views import update_ticket_status


urlpatterns = [
    # path('emp1/',views.emp, name='emp1'),
    path('profile/',views.profile, name='profile'),
    path('emp1/', Viewtkassign.as_view(), name='employee_page'),
    path('update_ticket_status/', update_ticket_status, name='update_ticketstatus'),
]