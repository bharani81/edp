import os
from django.shortcuts import  render, redirect
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.files.storage import FileSystemStorage
import requests
from django.contrib.auth.decorators import login_required
import json
from django.http import HttpResponse,JsonResponse
from .forms import NewUserForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import user_mapping,Questions,answers,Question_vote,Answer_vote,profile
from django.contrib.auth.models import User
from datetime import datetime
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_protect

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
                return redirect('home')
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
                    return redirect('home')
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
	return redirect('home')

# def content_file_name(filename):
#     file_root, file_ext = os.path.splitext(filename)
#     return f'{file_root}_{datetime.utcnow().time()}{file_ext}'

@login_required(login_url='home')
def article(request):
    if request.method=='POST':
        if 'post_question' in request.POST:
        # print('hi')
            q_title = request.POST.get('question_title')
            q_body = request.POST.get('question_body')      
            print(request.FILES)
            if 'image' in request.FILES:
                img = request.FILES['image']
                fs = FileSystemStorage()
                # img.name = content_file_name(img.name)
                name = fs.generate_filename(img.name)
                file = fs.save(name,img)
                print(name)
                question_obj = Questions(q_title= q_title,q_body=q_body,user_id=request.user,q_image=name)
                question_obj.save()
            else:
                question_obj = Questions(q_title= q_title,q_body=q_body,user_id=request.user)
                question_obj.save()
            question_json=Questions.objects.filter( q_id=question_obj.q_id).values('q_id','q_title','q_body','user_id','q_image')
            print(question_obj.q_title)
            # return JsonResponse(data = list(question_json) ,safe=False)
        if 'upvote' in request.POST:
            question_obj = Questions.objects.get(q_id=request.POST.get('upvote'))
            is_voted = Question_vote.objects.filter(voted_q_id= question_obj,voted_user_id=request.user,is_upvote=True)
            if is_voted:
                Question_vote.objects.filter(voted_q_id= question_obj,voted_user_id=request.user).delete()
                print('like deleted')
            else: 
                Question_vote.objects.filter(voted_q_id= question_obj,voted_user_id=request.user).delete()
                vote_obj = Question_vote(voted_q_id=question_obj,voted_user_id=request.user,is_upvote=True,is_downvote=False)
                vote_obj.save()
                print('liked')
                #Question_vote.objects.filter(voted_q_id=question_obj,voted_user_id=request.user,is_upvote=True).update(is_downvote=False)
        if 'downvote' in request.POST:
            question_obj = Questions.objects.get(q_id=request.POST.get('downvote'))
            is_voted= Question_vote.objects.filter(voted_q_id=question_obj,voted_user_id=request.user,is_downvote=True)
            if is_voted:
                Question_vote.objects.filter(voted_q_id=question_obj,voted_user_id=request.user).delete()
                print('dislike deleted')
            else:
                Question_vote.objects.filter(voted_q_id=question_obj,voted_user_id=request.user).delete()
                vote_obj =Question_vote(voted_q_id=question_obj,voted_user_id=request.user,is_upvote=False,is_downvote=True)
                vote_obj.save()
                print('disliked')
                # Question_vote.objects.filter(voted_q_id=question_obj,voted_user_id=request.user,is_downvote=True).update(is_upvote=False)
        if 'post_answer' in request.POST:
            print('hi')
            print(request.POST.get('post_answer'))
            question_obj= Questions.objects.get(q_id=request.POST.get('post_answer'))
            ans_body = request.POST.get('answer_text')
            print(ans_body)
            ans_obj = answers(answer_body=ans_body,answered_user=request.user,answered_question=question_obj)
            ans_obj.save()
        if 'ans_upvote' in request.POST:
            ans_obj = answers.objects.get(answer_id= request.POST.get('ans_upvote'))
            is_voted = Answer_vote.objects.filter(voted_ans_id=ans_obj,voted_ques_id= ans_obj.answered_question,voted_user_id=request.user,is_ans_upvote=True)
            if is_voted:
                Answer_vote.objects.filter(voted_ans_id=ans_obj,voted_user_id=request.user,voted_ques_id=ans_obj.answered_question).delete()
            else:
                Answer_vote.objects.filter(voted_ans_id=ans_obj,voted_user_id=request.user,voted_ques_id=ans_obj.answered_question).delete()
                vote_obj=Answer_vote(voted_ans_id=ans_obj,voted_user_id=request.user,voted_ques_id=ans_obj.answered_question,is_ans_upvote=True)
                vote_obj.save()
                print('ans liked')
        if 'ans_downvote' in request.POST:
            ans_obj=answers.objects.get(answer_id=request.POST.get('ans_downvote'))
            is_voted =Answer_vote.objects.filter(voted_ans_id=ans_obj,voted_ques_id= ans_obj.answered_question,voted_user_id=request.user,is_ans_downvote=True)
            if is_voted:
                Answer_vote.objects.filter(voted_ans_id=ans_obj,voted_user_id=request.user,voted_ques_id=ans_obj.answered_question).delete()
            else:
                Answer_vote.objects.filter(voted_ans_id=ans_obj,voted_user_id=request.user,voted_ques_id=ans_obj.answered_question).delete()
                vote_obj=Answer_vote(voted_ans_id=ans_obj,voted_user_id=request.user,voted_ques_id=ans_obj.answered_question,is_ans_downvote=True)
                vote_obj.save()
                print('ans disliked')
    question_list=[]
    for i in Questions.objects.all():
        new_question_list =[]
        new_question_list.append(i.q_title)
        new_question_list.append(i.q_body)
        new_question_list.append(i.user_id)
        new_question_list.append(i.q_time.strftime("%d %b %y"))
        new_question_list.append(i.q_id)
        new_question_list.append(Question_vote.objects.filter(voted_q_id=i,is_upvote=True).count())
        new_question_list.append(Question_vote.objects.filter(voted_q_id=i,is_downvote=True).count())
        answers_obj = answers.objects.filter(answered_question=i.q_id)
        main_list=[]
        for ans in answers_obj:
            object_list=[]
            object_list.append(ans.answered_user)
            object_list.append(ans.answered_at.strftime("%d %b %y"))
            object_list.append(ans.answer_body)
            object_list.append(ans.answer_id)
            object_list.append(Answer_vote.objects.filter(voted_ans_id = ans.answer_id,is_ans_upvote=True).count())
            object_list.append(Answer_vote.objects.filter(voted_ans_id = ans.answer_id,is_ans_downvote=True).count())
            main_list.append(object_list)
        new_question_list.append(main_list)
        new_question_list.append(i.q_image)
        # print(list(answers.objects.filter( answered_question=i.q_id)))
        question_list.append(new_question_list)
    answer_list=[]
    is_farmer=False
    if user_mapping.objects.filter(user_name=request.user,typeof='farmers'):
        is_farmer=True
    return render(request,'article.html',{ 'questions':question_list,'isfarmer':is_farmer,'answer_list':answer_list})
def post_my_question(request):
    if request.method=='POST':
        print('hi')
    redirect("article")
def my_profile(request):
    if request.method=='POST':
        name=request.POST.get('name')
        surname=request.POST.get('surname')
        mobile = request.POST.get('mobile')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        postcode= request.POST.get('postcode')
        state = request.POST.get('state')
        education = request.POST.get('education')
        country = request.POST.get('country')
        print(name+" "+surname+" "+mobile ) 
        print(request.FILES)
        if 'image' in request.FILES:
            print('hi')
            img = request.FILES['image']
            fs = FileSystemStorage()
            i_name = fs.generate_filename(img.name)
            file = fs.save(i_name,img)
            print(i_name)
            profile_obj= profile(user_id = request.user,first_name=name,surname=surname,mobile=mobile,address1=address1,address2=address2,postcode=postcode,state=state,education=education,country=country,profile_pic=i_name)
            profile_obj.save()
            prof_list=[]
            prof_list.append(name)
            prof_list.append(surname)
            prof_list.append(mobile)
            prof_list.append(address1)
            prof_list.append(address2)
            prof_list.append(postcode)
            prof_list.append(state)
            prof_list.append(education)
            prof_list.append(country)
            prof_list.append(i_name)
            print(prof_list)
            return render(request,'profile.html',{'profile':prof_list})
    
    return render(request,'snippets.html')


def saveprofile(request):
    return render(request,'article.html')