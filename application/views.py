from django.shortcuts import  render, redirect
import json
from django.http import HttpResponse,JsonResponse
from .forms import NewUserForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import user_mapping,Questions,Question_vote
from django.contrib.auth.models import User
from datetime import datetime

def landingpage(request):
    return render(request,'index1.html')

def login_register(request):
    lform = AuthenticationForm()        
    rform= NewUserForm()
    if request.method=='POST':
        if 'register' in request.POST:
            rform = NewUserForm(request.POST)
            if rform.is_valid():
                rform.save()
                typeof = rform.cleaned_data.get('typeof')
                user_map= user_mapping(user_name = User.objects.get(username = rform.cleaned_data.get('username')),typeof =typeof)
                user_map.save()
                return redirect('')
            else:
                messages.error(request,"Invalid username or password.")
                print(rform.errors.as_data())
                print('hi')
        elif 'login' in request.POST:
            lform = AuthenticationForm(request, data=request.POST)
            print('hi')
            if lform.is_valid():
                username = lform.cleaned_data.get('username')
                password = lform.cleaned_data.get('password')
                print('hi')
                user = authenticate(username=username, password=password)
                if user is not None:
                    print('hi')
                    login(request, user)
                    return redirect('article')
                else:
                    messages.error(request,"Invalid username or password.")
            else:
                print(lform.cleaned_data.get('username'))
                print(lform.cleaned_data.get('password'))
                messages.error(request,"Invalid username or password.")
    return render(request,'my_login.html',{'registerform':rform,'loginform':lform})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")

def article(request):
    if request.method=='POST':
        if 'post_question' in request.POST:
        # print('hi')
            q_title = request.POST.get('question_title')
            q_body = request.POST.get('question_body')
            question_obj = Questions(q_title= q_title,q_body=q_body,user_id=request.user)
            question_obj.save()
            question_json=Questions.objects.filter( q_id=question_obj.q_id).values('q_id','q_title','q_body','user_id')
            print(question_obj.q_title )
            return JsonResponse(data = list(question_json) ,safe=False)
        print('punda')
        if 'upvote' in request.POST:
            question_obj = Questions.objects.get(q_id=request.POST.get('upvote'))
            is_voted = Question_vote.objects.filter(voted_q_id= question_obj,voted_user_id=request.user)
            if is_voted:
                Question_vote.objects.filter(voted_q_id= question_obj,voted_user_id=request.user).delete()
                print('like deleted')
            else: 
                vote_obj = Question_vote(voted_q_id=question_obj,voted_user_id=request.user,is_upvote=True)
                vote_obj.save()
                print('liked')
                setattr(vote_obj,is_downvote=False)
                vote_obj.save()
    question_list=[]
    for i in Questions.objects.all():
        new_question_list =[]
        new_question_list.append(i.q_title)
        new_question_list.append(i.q_body)
        new_question_list.append(i.user_id)
        new_question_list.append(i.q_time.strftime("%d %b %y"))
        new_question_list.append(i.q_id)
        new_question_list.append(Question_vote.objects.filter(voted_q_id=i,is_upvote=True).count())
        question_list.append(new_question_list)
    return render(request,'article.html',{'questions':question_list})

def post_my_question(request):
    if request.method=='POST':
        print('hi')

        
    redirect("article")