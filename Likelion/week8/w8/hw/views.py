from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
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
    return render(request, 'main.html')