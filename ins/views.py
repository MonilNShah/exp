from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return redirect(home.base.html)
    return HttpResponse("Logged In")
	#return render(request,'index.html')from django.shortcuts import render

# Create your views here.
