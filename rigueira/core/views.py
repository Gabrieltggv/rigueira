from django.shortcuts import render

from .forms import UserLogin


# Create your views here.
def login(request):
    if request.POST:
        form = UserLogin(request.POST)
        if form.is_valid():
            pass

    else:
        form = UserLogin()
    return render(request, 'core/login.html', context={'form': form})
