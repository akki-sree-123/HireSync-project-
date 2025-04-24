from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Extended User model to include additional required fields.
    Inherits from Django's AbstractUser which already has username, password, email, first_name, last_name
    """
    mobile_number = models.CharField(max_length=15, blank=False, null=False)
    
    def __str__(self):
        return self.username
    


