from django.db import models

# Create your models here.
class AuthUser(models.Model):
    fullname= models.CharField(max_length=200)
    email = models.CharField(max_length= 200)
    phone = models.IntegerField()
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.fullname
