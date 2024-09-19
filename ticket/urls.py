from django.urls import path
from .views import ticket, CreateTicket, ticket_history, SubmitFeedback

urlpatterns = [
    path('ticket/', ticket, name='ticket'),
    path('create_ticket/',CreateTicket.as_view(), name='create_ticket'),
    path('ticket_history/', ticket_history, name='ticket_history'),
    path('submit_feedback/', SubmitFeedback.as_view(), name='submit_feedback'),
    # path('submit_feedback/', SubmitFeedback.as_view(), name='submit_feedback'),
]