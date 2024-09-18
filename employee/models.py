from django.db import models

# Create your models here.
class employee(models.Model):
    empname= models.CharField(max_length=200)
    empemail = models.CharField(max_length= 200)
    empphone = models.IntegerField()
    emppassword = models.CharField(max_length=50)
    role = models.CharField(max_length=50, blank=True)
