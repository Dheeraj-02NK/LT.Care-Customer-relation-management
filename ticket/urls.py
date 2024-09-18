from django.urls import path
from .views import ticket, CreateTicket, ticket_history

urlpatterns = [
    path('ticket/', ticket, name='ticket'),
    path('create_ticket/',CreateTicket.as_view(), name='create_ticket'),
    path('ticket_history/', ticket_history, name='ticket_history'),
]