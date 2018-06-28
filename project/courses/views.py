from django.shortcuts import render


# Create your views here.
def index(request):
    params = {}
    return render(request, 'courses/index.html', context=params)


def python_one(request):
    params = {'course_name': 'Python One'}
    return render(request, 'courses/python-one/index.html', context=params)
