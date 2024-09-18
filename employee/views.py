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
        tickets = Ticket.objects.all().values('t_id', 'phone_number', 'address', 'issue','status')  # Fixed the tickets query

        # Add both userdata and tickets to the context
        context['userdata'] = userdata
        context['tickets'] = tickets

        return context
    


# class update_status(APIView):
#     def post(self, request):
#         uid = request.POST['id']
#         fullname1 = request.POST['fullname']
#         email1 = request.POST['email']
#         phone1 = request.POST['phone']
#         password1 = request.POST['password']
#         role = request.POST['role']
#         print(password1)
#         userdata = AuthUser.objects.filter(id=uid).update(fullname=fullname1,email=email1,phone=phone1, password=password1, role=role)
#         # print("********: ", userdata)
#         return JsonResponse({"status":"pass"})
    



