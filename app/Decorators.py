from django.http import HttpResponse
from django.shortcuts import redirect

def user_notlive(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated: 
            return redirect('dashboard', request.user.id)
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func