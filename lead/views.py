from django.shortcuts import render
from .models import Lead
from rest_framework.views import APIView
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from authuser.models import AuthUser
from ticket.models import Ticket

# Create your views here.
def leading(request):
    customers = AuthUser.objects.all()
    ticket1=Ticket.objects.all()
    context = {"currentuser" :request.session["user_data"], 'customer':customers,'ticket1':ticket1}
    return render(request, 'lead/lead.html',context)

class Createtkassign(APIView):
    def post(self, request):
        tec_name = request.POST['tec_name']
        tk_name= request.POST['tk_name']
        ass_date = request.POST['ass_date']
        ld_name = request.POST['ld_name']
        usr = Lead()
        usr.tec_name = tec_name
        usr.tk_name = tk_name
        usr.lead_date  = ass_date
        usr.lead_name = ld_name
        usr.save()
        return JsonResponse({"status":"pass"})
    
class deletetkassign(APIView):
    def post(self, request):
        id = request.POST["id"]
        Lead.objects.filter(id=id).delete()
        return JsonResponse({"status":"pass"})
    
class Viewtkassignall(TemplateView):
    template_name = 'lead/alllead.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        userdata = Lead.objects.all()
        customers = AuthUser.objects.all()
        ticket1=Ticket.objects.all()
        context={'userdata':userdata,'customer':customers,'ticket1':ticket1}
        return context

class Viewtkassign(TemplateView):
    template_name = 'lead/leadtable.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get the current user from the session
        current_user_name = self.request.session.get("user_data")
        
        # Filter userdata based on the current tech lead
        userdata = Lead.objects.filter(lead_name=current_user_name)  # Assuming 'lead_name' refers to the tech lead's name
        
        customers = AuthUser.objects.all()
        ticket1 = Ticket.objects.all()
        
        # Update context with filtered userdata
        context.update({
            'userdata': userdata,
            'customer': customers,
            'ticket1': ticket1,
            'currentuser': current_user_name,
        })
        
        return context
    




class edit_user(APIView):
    def post(self, request):
        uid = request.POST['id']
        fullname1 = request.POST['fullname']
        password1 = request.POST['password']
        userdata = Lead.objects.filter(id=uid).update(tec_name=fullname1,lead_date=password1)
        return JsonResponse({"status":"pass"})
    
