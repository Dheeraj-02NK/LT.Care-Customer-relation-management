from typing import Any
from django.shortcuts import render
from .models import employee
from rest_framework.views import APIView
from django.views.generic.base import TemplateView
from django.http import JsonResponse

# Create your views here.
def emp(request):
    context = {}
    context["currentuser"] = request.session["user_data"]
    return render(request, 'employee/employee.html/',context)
def profile(request):
    return render(request, 'profile.html/')

class Viewtkassign(TemplateView):
    template_name='employee/employee.html'
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        userdata = employee.objects.all()
        context['userdata']= userdata
        return context



