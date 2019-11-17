from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.db import models

class MyUserCreationForm(UserCreationForm):
    email = models.CharField(max_length=150)

    class Meta :
        model = User 
        fields = ["username","email","password1","password2"]