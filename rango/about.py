from django.http import HttpResponse







def about(request):
    
    return HttpResponse("<a href="/rango/">Index</a>")