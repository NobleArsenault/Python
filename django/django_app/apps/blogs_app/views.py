from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    #return render(request, "blogs_app/index.html")
    starbucks = "placeholder to later display all the list of blogs"
    print starbucks
    return  HttpResponse(starbucks)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    print response
    return HttpResponse(response)

def create(request):
    return redirect("/")

def show(request, number):
    response = "blog number is ", number
    print response
    return HttpResponse(response)


def edit(request, number):
    response = "placeholder to edit blog ", number
    print response
    return HttpResponse(response)

def destroy(request, number):
    return redirect("/")