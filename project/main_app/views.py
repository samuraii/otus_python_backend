from django.shortcuts import render


# Create your views here.
def index(request):
    params = {'variable': 'This is the passed variable!'}
    return render(request, 'index.html', context=params)
