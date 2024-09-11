from django.urls import path
from .views import ticket, CreateTicket
urlpatterns = [
    path('ticket/', ticket, name='ticket'),
    path('create_ticket/',CreateTicket.as_view(), name='create_ticket')
]