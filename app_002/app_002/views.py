#from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse



def helloWorld(request):
    return HttpResponse(" Hello I'm app_002 ")
