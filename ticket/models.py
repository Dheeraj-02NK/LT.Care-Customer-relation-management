from django.db import models
from authuser.models import AuthUser

class Ticket(models.Model):
    t_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    cid = models.ForeignKey(AuthUser,null=False,blank=False,on_delete=models.CASCADE)  # Customer ID, assuming it's a string
    phone_number = models.CharField(max_length=15)  # To handle phone numbers with country codes
    address = models.TextField()  # For potentially long addresses
    ISSUE_CHOICES = [
        ('software issue', 'Software Issue'),
        ('damaged parts', 'Damaged Parts'),
        ('hardware issue', 'Hardware Issue'),
        ('general service', 'General Services'),
    ]
    issue = models.CharField(max_length=20, choices=ISSUE_CHOICES)  # Issue choices
    STATUS_CHOICES = [
        ('ticket raised', 'Ticket Raised'),
        ('technician assigned', 'Technician Assigned'),
        ('resolved', 'Resolved'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Ticket Raised', blank=True)
    rating = models.IntegerField(blank=True)
    comment = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'Ticket {self.t_id} - {self.cid}'

