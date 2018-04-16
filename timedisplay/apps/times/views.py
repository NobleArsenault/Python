
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    #context = {
       # "email" : "blog@gmail.com",
        #"name" : "mike"
    #}
    return render(request, "times/index.html")
    #return render(request, "ourApp/index.html", context)

def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        # request.session is the cookie and request.post is whats posted, this one would print 100 on the page request.session['name'] = 100
        request.session["name"] = request.POST['name'] #this saves from the terminal to the cookie pretty much
        print "*"*50
        context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
        }
        return render(request, "times/timedisplay.html", context)
    else:
        return redirect("/")
