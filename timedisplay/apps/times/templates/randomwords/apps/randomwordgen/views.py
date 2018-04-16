from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    request.session['unique'] = get_random_string(length=24)
    
    if 'count' not in request.session: 
        request.session['count'] = 1
    else:
        request.session['count'] += 1
        # return redirect("/")
    return render(request, "randomwordgen/index.html")
    
