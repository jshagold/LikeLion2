from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Employee
# Create your views here.
def index(request) :
    if request.method == 'POST':
        username = request.POST['ID']
        password = request.POST['pwd']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'index.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'index.html')


def sign_up(request) :
    if request.method == 'POST':
        if request.POST['pwd'] == request.POST['pwd_c']:
            user = User.objects.create_user(username = request.POST['ID'], password = request.POST['pwd'])
            auth.login(request, user)
            return redirect('index')
    return render(request, 'signup.html')

def main(request) :
    members = Employee.objects.all()

    if request.method == 'POST' :
        lname=request.POST['nm']
        lcode=request.POST['CD']

        likemem = Employee()
        likemem.name = lname
        likemem.code = lcode
        likemem.attendent = False
        likemem.save()

        if members.name == request.POST['c_name'] and members.code == request.POST['c_code'] :
            if members.attendent == True :
                members.attendent = False
                members.save()
            else :
                members.attendent = True
                members.save()

        return redirect('main')

    return render(request, 'main.html', {'member':members})