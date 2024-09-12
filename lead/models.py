from django.db import models

# Create your models here.
class Lead(models.Model):
    teach_name= models.CharField(max_length=200)
    tick_name = models.CharField(max_length= 200)
    lead_date = models.CharField(max_length=50)
    lead_name = models.CharField(max_length=50)