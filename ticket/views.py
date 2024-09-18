from typing import Any
from django.shortcuts import render
from .models import Ticket
from rest_framework.views import APIView
from django.http import JsonResponse
from django.views.generic.base import TemplateView
from authuser.models import AuthUser
# Create your views here.

def ticket(request):
    context = {}
    context = {"currentuser": request.session["user_data"], 'userid':request.session['user_id']}
    return render(request, 'ticket/customer.html', context)

class CreateTicket(APIView):
    def post(self, request):
        phone = request.data.get('phone') 
        address = request.data.get('address') 
        issue = request.data.get('issue')
        user_id = request.data.get("user_id")

        authuser = AuthUser.objects.get(cid = user_id)
        issues = Ticket()
        issues.cid = authuser
        issues.phone_number = phone
        issues.address = address
        issues.issue = issue
        issues.rating = 1
        issues.save()
        return JsonResponse({"status":"pass"})
    
class ViewIssue(TemplateView):
    template_name = 'view_user.html'
    def get_context_data(**kwargs) :
        context =  super().get_context_data(**kwargs)
        userdata = Ticket.objects.all()
        context['userdata'] = userdata
        return context



class SubmitFeedback(APIView):
    def post(self, request):
        rating = request.data.get('rating')
        comment = request.data.get('feedback')  # Use "feedback" for the comment
        user_id = request.data.get('user_id')

        try:
            # Find the latest resolved ticket for the user
            ticket = Ticket.objects.filter(cid=user_id, status='Resolved').order_by('-t_id').first()
            if ticket:
                ticket.rating = rating
                ticket.comment = comment  # Update the comment field
                ticket.save()
                return JsonResponse({"status": "success"})
            else:
                return JsonResponse({"status": "error", "message": "No resolved tickets found."}, status=404)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)


def ticket_history(request):
    # Fetch 'user_id' from the session
    user_id = request.session.get('user_id')
    print(f"user_id from session: {user_id}")  # Debugging line
    
    if user_id:
        try:
            # Fetch only resolved tickets for the current user
            tickets = Ticket.objects.filter(cid=user_id).values('t_id', 'issue', 'status', 'rating', 'phone_number')
            print(f"Resolved Tickets fetched: {tickets}")  # Debugging line
            return JsonResponse(list(tickets), safe=False)
        except Exception as e:
            print(f"Error fetching tickets: {str(e)}")  # Print the error in logs
            return JsonResponse({'error': 'Something went wrong while fetching tickets'}, status=500)
    
    return JsonResponse({'error': 'Unauthorized'}, status=403)
