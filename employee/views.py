from typing import Any
from django.shortcuts import render
from .models import employee
from rest_framework.views import APIView
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from ticket.models import Ticket  
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def emp(request):
    context = {}
    context["currentuser"] = request.session["user_data"]
    return render(request, 'employee/employee.html/',context)

def profile(request):
    return render(request, 'profile.html/')

class Viewtkassign(TemplateView):
    template_name = 'employee/employee.html'  # Correct template path

    def get_context_data(self, **kwargs):
        # Call the base implementation first
        context = super().get_context_data(**kwargs)

        # Query both userdata and tickets
        userdata = employee.objects.all()
        tickets = Ticket.objects.all().values('t_id', 'phone_number', 'address', 'issue','status', 'rating', 'comment')  # Fixed the tickets query

        # Add both userdata and tickets to the context
        context['userdata'] = userdata
        context['tickets'] = tickets

        return context
    
def update_ticket_status(request):
    if request.method == 'POST':
        ticket_id = request.POST.get('ticket_id')
        new_status = request.POST.get('status')

        try:
            ticket = Ticket.objects.get(t_id=ticket_id)
            ticket.status = new_status
            ticket.save()

            return JsonResponse({'message': 'Status updated successfully!', 'refresh': True})
        except Ticket.DoesNotExist:
            return JsonResponse({'message': 'Ticket not found!'}, status=404)

    return JsonResponse({'message': 'Invalid request!'}, status=400)

