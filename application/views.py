from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import user_mapping
from django.contrib.auth.models import User

def landingpage(request):
    return render(request,'index1.html')

def home(request):
    return render(request,'index1.html')

def register(request):    
    if request.method=='POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            typeof = form.cleaned_data.get('typeof')
            return redirect('home')
    else:
        form = NewUserForm()
    return render(request, 'login.html', {'registerform': form})

# def login_register(request):
    if request.method=='POST':
        if request.POST.get('submit') == 'register':
            rform = NewUserForm(request.POST)
            if rform.is_valid():
                rform.save()
                return redirect('home')
        elif request.POST.get('submit') == 'login':
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
                    return render(request,'index.html')
                else:
                    messages.error(request,"Invalid username or password.")
            else:
                print(lform.cleaned_data.get('username'))
                print(lform.cleaned_data.get('password'))
                messages.error(request,"Invalid username or password.")
    lform = AuthenticationForm()        
    rform= NewUserForm()
    return render(request,'my_login.html',{'registerform':rform,'loginform':lform})

def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(request, data=request.POST)
        print('hi')
        if form.is_valid():
            print('hi')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request,'index.html')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            print(form.cleaned_data.get('username'))
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request,'login1.html',{'loginform': form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")