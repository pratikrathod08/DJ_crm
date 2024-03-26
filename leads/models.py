from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# User = get_user_model()     # you can direct create user 

class User(AbstractUser):
    # celphone_number = models.CharField(max_length=15)
    pass

# Create your models here.
class Lead(models.Model):
    
    # SOURCE_CHOICES = (
    #     ("YouTube", "YouTube"),
    #     ("Google", "Google"),
    #     ("Newsletter", "Newsletter"),
    # )
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)    # foreign key 
    
    # phones = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
    
    # profile_picture = models.ImageField(blank=True, null=True)
    # special_file = models.FileField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
class Agent(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=20)      ## We do not need to give that value because we have already given user it has these value.
    # last_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.user.email
    
    
    