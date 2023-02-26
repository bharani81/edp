from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_mapping(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    typeof = models.CharField(max_length=50)
    def __str__(self):
        return self.typeof

class Questions(models.Model):
    q_id = models.AutoField(primary_key =True)
    q_title = models.CharField(max_length = 20)
    q_body = models.TextField(max_length=500)
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    q_time = models.DateTimeField(auto_now= True)

class Question_vote(models.Model):
    vote_id = models.AutoField(primary_key=True)
    voted_q_id = models.ForeignKey(Questions,on_delete=models.CASCADE)
    voted_user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    is_upvote =models.BooleanField(default=False)
    is_downvote =models.BooleanField(default=False)