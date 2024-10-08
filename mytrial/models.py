
from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    county = models.CharField(max_length=50)
    verification_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.user.username}'s Profile"


from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class CaseFile(models.Model):
    FORM_TYPE_CHOICES = [
        ('rent_restriction', 'Rent Restriction'),
        ('business_premises', 'Business Premises'),
        ('rent_tribunal', 'Rent Tribunal'),
        ('cooperative_tribunal', 'Cooperative Tribunal'),
    ]

    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('in_review', 'In Review'),
        ('in_revision', 'In Revision'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=100)
    postal_address = models.CharField(max_length=255)
    telephone_number = models.CharField(max_length=15)
    agent = models.CharField(max_length=100, blank=True)
    caretaker = models.CharField(max_length=100, blank=True)
    auctioneer = models.CharField(max_length=100, blank=True)
    duration_of_stay = models.CharField(max_length=100, blank=True)
    monthly_rent = models.CharField(max_length=100, blank=True)
    year_of_entry = models.CharField(max_length=100, blank=True)
    deposit_paid = models.CharField(max_length=100, blank=True)
    cause_of_action = models.CharField(max_length=255, blank=True)
    tenant_name = models.CharField(max_length=255, blank=True)
    landlord_name = models.CharField(max_length=255, blank=True)
    problem = models.TextField(blank=True)
    ocs_police_station = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    created_at = models.DateTimeField(default=timezone.now)
    file_upload = models.FileField(upload_to='case_files/', blank=True, null=True)  
    form_type = models.CharField(max_length=30, choices=FORM_TYPE_CHOICES, default='rent_restriction')




    def __str__(self):
        return f"Case File {self.id} by {self.user.username}"




class PassTicket(models.Model):
    case_file = models.ForeignKey(CaseFile, on_delete=models.CASCADE)
    document = models.FileField(upload_to='pass_tickets/', null=True, blank=True) 
    document_pdf = models.FileField(upload_to='pass_tickets/pdf/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"PassTicket for {self.case_file.tenant}"
    
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(PassTicket, on_delete=models.CASCADE,null=True )  
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True) 
    payment_date = models.DateTimeField(default=timezone.now)  
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Payment {self.ticket} for Ticket {self.ticket.id}"

