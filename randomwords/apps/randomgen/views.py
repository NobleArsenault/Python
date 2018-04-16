from django.shortcuts import render

def index(request):
    return render(request, "randomgen/index.html")
    if 'count' not in request.session: 
        request.session['count'] = 1
    else:
        request.session['count'] += 1
        return redirect("/")



# def reset 
#     request session clear