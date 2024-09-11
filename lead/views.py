from django.shortcuts import render
from .models import Lead
from rest_framework.views import APIView
from django.views.generic.base import TemplateView
from django.http import JsonResponse

# Create your views here.
def leading(request):
    return render(request, 'lead/lead.html')

class Createtkassign(APIView):
    def post(self, request):
        tec_name = request.POST['tec_name']
        tk_name= request.POST['tk_name']
        ass_date = request.POST['ass_date']
        ld_name = request.POST['ld_name']
        usr = Lead()
        usr.teach_name = tec_name
        usr.tick_name = tk_name
        usr.lead_date  = ass_date
        usr.lead_name = ld_name
        usr.save()
        return JsonResponse({"status":"pass"})
    
class deletetkassign(APIView):
    def post(self, request):
        id = request.POST["id"]
        Lead.objects.filter(id=id).delete()
        return JsonResponse({"status":"pass"})
    
class Viewtkassign(TemplateView):
    template_name = 'lead/leadtable.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        userdata = Lead.objects.all()
        context['userdata'] = userdata
        return context