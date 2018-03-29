from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import book


class RegistrationForm(UserCreationForm):
    error_css_class='error'
    required_css_class='required'
    

    class Meta:
        model = User
        fields = ('username',
        	'password1',
        	'password2'
        	)

class AddBook(forms.ModelForm):
    """docstring for BookDetail"""
    book_name=forms.CharField(required=True)
    Author_name=forms.CharField(required=True)
    date=forms.DateField()

    class Meta(object):
        model=book
        """docstring for Meta"""
        fields=('book_name','Author_name')
            
        
    