from django.shortcuts import render

# Create your views here.
def index(request) :
    return render(request, 'index.html')

def about(request) :
    return render(request, 'about.html')

def result(request) :
    full_text = request.GET['fulltext']

    word_list = full_text.split()
    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, 'result.html', {'fulltext':full_text, 'dictionary':word_dictionary.items()})

