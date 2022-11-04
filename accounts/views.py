from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as jng_Login
from django.contrib.auth import logout as jng_logout

# Create your views here.

# Login
def signUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #Login
            user = form.save() #Register then get user
            jng_Login(request, user)
            return redirect('articel:List')
    else :  
        form = UserCreationForm()
    return render(request, GetViewName('signUp'), {"form":form})

def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Login
            user = form.get_user()
            jng_Login(request, user)
            return redirect('articel:List')
    else:
        form = AuthenticationForm()
    return render(request, GetViewName('Login'), {"form":form})

def Logout(request):
    if request.method == 'POST':
        jng_logout(request)
    return redirect('articel:List')

# Return Name of View 
def GetViewName(functionName:str)->str:
    return f"accounts/{functionName}.html"
