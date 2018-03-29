from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def dis(request):
    return HttpResponse("Logged In")