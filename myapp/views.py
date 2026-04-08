from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import EventRegistration ,Contact
from django.contrib import messages

def index(request):
    return render(request,'myapp/index.html')
def eventregister(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please login first to register for event")
        return redirect('/login/')
    if request.method == "POST":
        EventRegistration.objects.create(
            user = request.user,
            student_name = request.POST['student_name'],
            department = request.POST['department'],
            register_number = request.POST['register_number'],
            phone = request.POST['phone'],
            event = request.POST['event'],    
        )
        messages.success(request, "Successfully Registered")
        return redirect('eventregister')
    return render(request, 'myapp/eventregister.html')
def user_login (request):
    if request.method=="POST":
        username= request.POST['username']
        password= request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return render(request,'myapp/login.html',{'error':'Invalid Credentials'})
    return render(request,'myapp/login.html')
def user_logout(request):
    logout(request)
    return redirect('login')
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            return render(request,"myapp/register.html",{"error":"Password do not match"})
        if User.objects.filter(username=username).exists():
            return render(request,"myapp/register.html",{"error":"Username already exists"})
        user = User.objects.create_user(username=username,email=email,password=password)
        messages.success(request, "Account created successfully")
        login(request,user)
        return redirect('index')
    return render(request, 'myapp/register.html')
def my_events(request):
    if not request.user.is_authenticated:
        return redirect('login')
    events = EventRegistration.objects.filter(user=request.user).order_by('-submitted')
    messages_list = Contact.objects.filter(user=request.user).order_by('-submitted')
    return render(request, 'myapp/my_events.html',{'events': events,'messages_list': messages_list})
def contact(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please login to send message")
        return redirect('login')

    if request.method == "POST":
        Contact.objects.create(
            user=request.user,
            name=request.POST['name'],
            email=request.POST['email'],
            batch_year=request.POST['batch_year'],
            department=request.POST['department'],
            message_type=request.POST['message_type'],
            message=request.POST['message']
        )

        messages.success(request, "Message sent successfully!")
        return redirect('my_events')

    return redirect('index')

# Create your views here.
