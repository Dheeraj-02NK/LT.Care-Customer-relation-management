from typing import Any
from django.shortcuts import render
from .models import AuthUser
from rest_framework.views import APIView
from django.views.generic.base import TemplateView
from django.http import JsonResponse

# Create your views here.
def main(request):
    return render(request, 'authuser/index.html')
def login(request):
    return render(request, 'authuser/login.html')
def signup(request):
    return render(request, 'authuser/signup.html')

class CreateUser(APIView):
    def post(self, request):
        fullname = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        user = AuthUser()
        user.fullname = fullname
        user.email = email
        user.phone = phone
        user.password = password
        user.save()
        return JsonResponse({"status":"pass"})
    
class delete_user(APIView):
    def post(self, request):
        id = request.POST["id"]
        AuthUser.objects.filter(id=id).delete()
        return JsonResponse({"status":"pass"})
    
class edit_user(APIView):
    def post(self, request):
        uid = request.POST['id']
        fullname1 = request.POST['fullname']
        email1 = request.POST['email']
        phone1 = request.POST['phone']
        password1 = request.POST['password']
        print(password1)
        userdata = AuthUser.objects.filter(id=uid).update(fullname=fullname1,email=email1,phone=phone1, password=password1)
        print("********: ", userdata)
        return JsonResponse({"status":"pass"})

class ViewStaff(TemplateView):
    template_name = 'view_user.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        userdata = AuthUser.objects.all()
        context['userdata'] = userdata
        return context



