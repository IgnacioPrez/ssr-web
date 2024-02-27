from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    my_list = ['a','n','c']
    return render(request,"index.html",{
        'my_list':my_list
    })
 
def hello_params(request,username):
    # return HttpResponse(f"<h1>Como tan muchacho {username}<h1/>")
    return HttpResponse("<h1>Como tan muchacho %s </h1>" % username)
