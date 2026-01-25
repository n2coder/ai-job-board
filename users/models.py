from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    ROLE_CHOICES = (
        ('candidate', 'Candidate'),
        ('recruiter', 'Recruiter'),
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

def __str__(self):
        return f"{self.username} ({self.role})"
# Create your models here.
