from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    task= models.TextField(null=True, blank=True)
    created= models.DateTimeField(auto_now_add=True)
 
