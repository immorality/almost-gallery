from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Bundash says hey there partner!")



