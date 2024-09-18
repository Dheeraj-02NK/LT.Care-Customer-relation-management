# from typing import Any
from django.shortcuts import render,get_object_or_404
from .models import AuthUser
from rest_framework.views import APIView
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from ticket.models import Ticket


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
        role = request.POST['role']
        user = AuthUser()
        user.fullname = fullname
        user.email = email
        user.phone = phone
        user.password = password
        user.role = role
        user.save()
        return JsonResponse({"status":"pass"})
    
class delete_user(APIView):
    def post(self, request):
        id = request.POST["cid"]
        AuthUser.objects.filter(cid=id).delete()
        return JsonResponse({"status":"pass"})
    
class edit_user(APIView):
    def post(self, request):
        uid = request.POST['cid']
        fullname1 = request.POST['fullname']
        email1 = request.POST['email']
        phone1 = request.POST['phone']
        password1 = request.POST['password']
        role = request.POST['role']
        print(password1)
        userdata = AuthUser.objects.filter(cid=uid).update(fullname=fullname1,email=email1,phone=phone1, password=password1, role=role)
        # print("********: ", userdata)
        return JsonResponse({"status":"pass"})


class login_check(APIView):
    def post(self, request):
        mob = request.POST['mob']
        password = request.POST['password']
        ent = AuthUser.objects.filter(phone=mob,password=password).values()
        if(len(ent) > 0):
            request.session["user_data"] = ent[0]["fullname"]
            request.session['user_id'] = ent[0]['cid']
            return JsonResponse({"status":"pass", "uid": ent[0]["phone"], "role": ent[0]["role"], "name": ent[0]["fullname"]})
        else:
            return JsonResponse({"status":"fail"})


class logout(APIView):
    def post(self, request):
        request.session["user_data"] = ""
        return JsonResponse({"status":"pass"})
       

class ViewStaff(TemplateView):
    template_name = 'view_user.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        print("***********:request ", self.request.session["user_data"])
        userdata = AuthUser.objects.all()
        tickets = Ticket.objects.select_related('cid').all()
        context['tickets'] = tickets
        context['userdata'] = userdata
        context["currentuser"] = self.request.session["user_data"]
        return context


