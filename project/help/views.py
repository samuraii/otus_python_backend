from django.shortcuts import render


# Create your views here.
def index(request):
    params = {}
    return render(request, 'help/index.html', context=params)
