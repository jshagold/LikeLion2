from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def result(request):
    full_text = request.GET['fulltext']

    word_list = full_text.split()

    word_list.sort()

    return render(request, 'result.html',
                  {'fulltext': full_text, 'total': len(word_list), 'list': word_list})
