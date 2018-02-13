from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response




def index(request):
    context = RequestContext (request)
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    
    return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/'>Index</a>")