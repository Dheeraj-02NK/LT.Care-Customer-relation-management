from typing import Any
from django.shortcuts import render
from .models import Ticket
from rest_framework.views import APIView
from django.http import JsonResponse
from django.views.generic.base import TemplateView
# Create your views here.
def ticket(request):
    return render(request, 'ticket/customer.html')

class CreateTicket(APIView):
    def post(self, request):
        phone = request.POST['phoneno'] 
        address = request.POST['addressloc'] 
        issuetype = request.POST['issuetype'] 
        issue = Ticket()
        issue.phone_number = phone
        issue.address = address
        issue.issue = issuetype
        issue.save()
        return JsonResponse({"status":"pass"})
class ViewIssue(TemplateView):
    template_name = 'view_user.html'
    def get_context_data(**kwargs) :
        context =  super().get_context_data(**kwargs)
        userdata = Ticket.objects.all()
        context['userdata'] = userdata
        return context