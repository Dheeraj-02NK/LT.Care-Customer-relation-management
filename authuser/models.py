from django.db import models

# Create your models here.
class AuthUser(models.Model):

  
    # uid = models.AutoField(primary_key=True, default="")
    cid = models.AutoField(primary_key=True)
    fullname= models.CharField(max_length=200)
    email = models.CharField(max_length= 200)
    phone = models.IntegerField()
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50, blank=True)

    

    def __str__(self) -> str:
        return self.fullname
