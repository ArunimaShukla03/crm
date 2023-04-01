from django.http import HttpResponse

from django.shortcuts import redirect

# The first "decorator" we are gonna write is that something that stops the authenticated user from viewing the login or register page.

# A decorator is a function that takes another function as an parameter.

def unauthenticated_user(view_func):

    def wrapper_func(request, *args, **kwargs):

        if request.user.is_authenticated:

            return redirect("home")
        
        else:

            return view_func(request, *args, **kwargs)

    return wrapper_func

# In this decorator of three layers, we are gonna pass in a list that means a single page can allow multiple types of users. 

def allowed_users(allowed_roles=[]):

    def decorator(view_func):

        def wrapper_func(request, *args, **kwargs):

            group = None

            if request.user.groups.exists():

                group = request.user.groups.all()[0].name

                # Set the first group of the user by its name.

            if group in allowed_roles:

                return view_func(request, *args, **kwargs)
            
            else:

                return HttpResponse("You are not authorized to view this page.")
        
        return wrapper_func
    
    return decorator

def admin_only(view_func):

    def wrapper_func(request, *args, **kwargs):

        group = None

        if request.user.groups.exists():

            group = request.user.groups.all()[0].name

        if group == 'customer':

            return redirect('user-page')
        
        if group == 'admin':

            return view_func(request, *args, **kwargs)
        
    return wrapper_func  