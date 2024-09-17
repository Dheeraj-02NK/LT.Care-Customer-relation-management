from django.db import models
from authuser.models import *
from ticket.models import *

# Create your models here.
class Lead(models.Model):
    # teach_name= models.CharField(max_length=200)
    # tick_name = models.CharField(max_length= 200)
    lead_date = models.DateField()
    lead_name = models.CharField(max_length=50)
    teach_name=models.ForeignKey(AuthUser,on_delete=models.CASCADE)
    tick_name=models.ForeignKey(Ticket,on_delete=models.CASCADE)