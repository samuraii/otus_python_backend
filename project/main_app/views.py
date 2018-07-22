from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import render_to_response


# Create your views here.
def index(request):
    params = {'variable': 'This is the passed variable!'}
    return render(request, 'index.html', context=params)

def logout_view(request):
    logout(request)
    return render_to_response('registration/logout_success.html')
