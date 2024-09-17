from django.db import models

class Ticket(models.Model):
    t_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    cid = models.CharField(max_length=100)  # Customer ID, assuming it's a string
    phone_number = models.CharField(max_length=15)  # To handle phone numbers with country codes
    address = models.TextField()  # For potentially long addresses
    ISSUE_CHOICES = [
        ('software', 'Software Issue'),
        ('damage', 'Damage Parts'),
        ('hardware', 'Hardware Issue'),
        ('general', 'General Services'),
    ]
    issue = models.CharField(max_length=20, choices=ISSUE_CHOICES)  # Issue choices

    def __str__(self):
        return f'Ticket {self.t_id} - {self.cid}'

