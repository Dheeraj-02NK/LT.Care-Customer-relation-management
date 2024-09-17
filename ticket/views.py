from typing import Any
from django.shortcuts import render
from .models import Ticket
from rest_framework.views import APIView
from django.http import JsonResponse
from django.views.generic.base import TemplateView
# Create your views here.

def ticket(request):
    context = {}
    context["currentuser"] = request.session["user_data"]
    return render(request, 'ticket/customer.html', context)

class CreateTicket(APIView):
    def post(self, request):
        phone = request.POST['phone'] 
        address = request.POST['address'] 
        issuetype = request.POST['issue'] 
        issues = Ticket()
        issues.phone_number= phone
        issues.address = address
        issues.issue = issuetype
        issues.save()
        return JsonResponse({"status":"pass"})
    
class ViewIssue(TemplateView):
    template_name = 'view_user.html'
    def get_context_data(**kwargs) :
        context =  super().get_context_data(**kwargs)
        userdata = Ticket.objects.all()
        context['userdata'] = userdata
        return context
