from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistrationForm,AddBook
from django.contrib.auth import authenticate, login
from .models import book
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import calendar


# Create your views here.
def index(request):
    #return redirect(home.base.html)
    return HttpResponse("Logged In")
	#return render(request,'index.html')
def register(request):
    registered = False
    if request.method == 'POST':
    	user_form = RegistrationForm(request.POST)
    	if user_form.is_valid():
    		#return HttpResponse("HELOOOOOOOOOOOOO")
    		user=user_form.save()
    		#user_form.set_password(user.password)
    		print("HELOOOOOOOOOOOOO")
    		'''username = user_form.get('username')
    		raw_password = user_form.get('password')
    		print(username)
    		user.first_name=user_form.get('first_name')
    		user.last_name=user_form.get('last_name')
    		user.email=user_form.get('email')'''
    		'''user.first_name=request.POST.get('first_name')
    		user.last_name=request.POST.get('last_name')
    		user.email=request.POST.get('email')'''
    		user.save()
    		#login(request, authenticate(username=username, password=raw_password))
    		registered = True
    		print(user_form['username'])

    else:
        user_form = RegistrationForm()
    if registered:
        #return HttpResponse("Logged In")
         #redirect_to = settings.LOGIN_REDIRECT_URL
         return redirect ('/login/')
         #return reverse ('home:base')
    else:
        return render(request, 'register.html', {'user_form': user_form})


@login_required(login_url='/login/')
def book_detail(request):
        book1=book.objects.all();
        print(book1[0].book_name)
        print(book1[0].date.day)
        print(book1[0].date.month)
        print(book1[0].date.year)
        z=calendar.day_name[book1[0].date.weekday()]
        print(z)
        x=book1[0].date.weekday()
        print(x)
        return render(request,'book_detail.html',{'book':book1})


# Final Rendering Template +Using Forms+ Saving Data Into Database
@login_required(login_url='/login/')
def add_book(request):
    registered=False
    if request.method== 'POST':
        add_book_form=AddBook(request.POST)
        print("In If request POST")
        if add_book_form.is_valid():
            registered=True
            add_book=add_book_form.save()
            add_book.save()
        else:
            print("Not Validated")
    else:
        add_book_form=AddBook()
    if registered:
         return redirect('book/')
    else:
        return render(request,'add_book.html',{'add_book':add_book_form})

def author_detail(request):
        auth=book.objects.all();
        return render(request,'author_detail.html',{'book':auth})
    

#def home(request):
  #  return render(request,'index.html')
