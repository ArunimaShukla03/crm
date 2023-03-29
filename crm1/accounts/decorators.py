from django.http import HttpResponse
from django.shortcuts import redirect

# The first "decorator" we are gonna write is that something that stops the authenticated user from viewing the login or register page.

# A decorator is a function that takes another function as an parameter.

def authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect("home")
        
        else:
            return view_func(request, *args, **kwargs)

        return view_func(request, *args, **kwargs)
    
    return wrapper_func
