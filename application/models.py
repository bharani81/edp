from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_mapping(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    typeof = models.CharField(max_length=50)
    def __str__(self):
        return self.typeof