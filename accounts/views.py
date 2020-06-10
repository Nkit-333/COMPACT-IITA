from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def Slogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if("IIT" not in username):
            print("no entry")
            return redirect('/')


        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print('loged in')
            return redirect('/StudentDash')
        else:
            messages.info(request,'Invalid User')
            print('invalid')
            return redirect('/')
    else:
        print('nothing is happening')

def Flogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if("IIT" in username):
            print("no entry")
            return redirect('/')

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print('loged in')
            return redirect('/facultyDash')
        else:
            messages.info(request,'Invalid User')
            print('invalid')
            return redirect('/')
    else:
        print('nothing is happening')