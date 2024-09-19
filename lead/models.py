from django.db import models
from authuser.models import *
from ticket.models import *

# Create your models here.
class Lead(models.Model):
    lead_date = models.DateField()
    lead_name = models.CharField(max_length=50)
    tec_name=models.CharField(max_length=200)
    tk_name=models.CharField(max_length=200)


