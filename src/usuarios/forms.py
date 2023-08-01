from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD
from .models import User
#clase que crea un formulario

class RegistrarseFrom (UserCreationForm):
    class Meta: 
        model = User
        fields = ['username','first_name', 'last_name','password1','password2','email','telefono']
=======
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms
from .models import User


class RegistrarseFrom(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta: 
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )

    def __init__(self, *args, **kwargs):
        super(RegistrarseFrom, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
>>>>>>> ad4bde6a87cb55703e633a2843556956b3c8b2cf
