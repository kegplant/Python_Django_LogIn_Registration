from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from models import Users
import bcrypt
from django.contrib.messages import error

# the index function is called when root is visited
def index(request):
    context={
    }
    #return HttpResponse(response)
    return render(request,'logIn_registration/index.html',context)

def register(request):
    #validate
    errors=Users.objects.registration_validator(request.POST)
    if errors:
        for tag,message in errors.items():
            error(request,message,extra_tags=tag)
        return redirect('/')
    else:
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        hash1=bcrypt.hashpw(password.encode(),bcrypt.gensalt())
        user=Users.objects.create(first_name=first_name,last_name=last_name,email=email,password=hash1)
        return redirect('/'+str(user.id)+'/success')
def logIn(request):
    #if wrong: credential / existance, flash message
    errors=Users.objects.logIn_validator(request.POST)
    if errors:
        for tag,message in errors.items():
            error(request,message,extra_tags=tag)
        return redirect('/')
    else:
        user=Users.objects.filter(email=request.POST['email'])[0]
        if bcrypt.checkpw(request.POST['password'].encode(),user.password.encode()):
            return redirect('/'+str(user.id)+'/success')
        #flash vague message//wrong password   
def process(request):
    if request.method=='POST':
        if request.POST['type']=='register':            
            return register(request)
        if request.POST['type']=='log in':            
            return logIn(request)
    return redirect('/')

def success(request,id):
    user=Users.objects.get(id=id)
    context={
        'user': user,
    }
    #validate it's logged in########################################
    return render(request,'logIn_registration/success.html',context)

def clear(request):
    Users.objects.all().delete()
    return redirect('/')