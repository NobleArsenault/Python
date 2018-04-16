from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)

def new(request):
    response = "create blog"
    return HttpResponse(response)

def create(request):
    return redirect("/")

def show(request, number):
    print number
    return HttpResponse("placeholder to display blog " + number)

def edit(request, number):
    print number
    return HttpResponse("placeholder to edit blog " + number)

def delete(request, number):
    return redirect("/")