from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class user_mapping(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    typeof = models.CharField(max_length=50)

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

class answers(models.Model):
    answer_id =models.AutoField(primary_key=True)
    answer_body=models.TextField(max_length=10000)
    answered_user=models.ForeignKey(User,on_delete=models.CASCADE)
    answered_question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    answered_at = models.DateTimeField(auto_now=True)

class Answer_vote(models.Model):
    ans_vote_id = models.AutoField(primary_key=True)
    voted_ans_id = models.ForeignKey(answers,on_delete=models.CASCADE)
    voted_user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    voted_ques_id = models.ForeignKey(Questions,on_delete=models.CASCADE)
    is_ans_upvote = models.BooleanField(default=False)
    is_ans_downvote =models.BooleanField(default=False)

class Customer_mobile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = PhoneNumberField()
    city = models.CharField(max_length=100)

class user_profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.ForeignKey(Customer_mobile,on_delete=models.CASCADE)
    