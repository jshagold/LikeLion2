from django.shortcuts import render
from .models import Restaurant

# Create your views here.
def index(request) :
    return render(request, 'index.html')


def map(request) :
    return render(request, 'map.html')

def restaurants(request) :
    return render(request, 'restaurants.html')

def facilities(request) :
    return render(request, 'facilities.html')

def test(request) :

    f_c = request.GET['food_category']
    if f_c == 'korean' :
        check = 1
    elif f_c == 'chinese' :
        check = 2

    category = Restaurant.objects.filter(cate = check)

    return render(request, 'test.html', {'category':category, 'f_category':f_c})