from django.contrib.auth.forms import UserCreationForm
from .models import User
#clase que crea un formulario

class RegistrarseFrom (UserCreationForm):
    class Meta: 
        model = User
        fields = ['username','first_name', 'last_name','password1','password2','email','telefono']