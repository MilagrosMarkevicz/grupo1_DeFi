from django import forms
from.models import Publicaciones,Comentario


class CrearPublicacionForm(forms.ModelForm):
    class Meta:
     model=Publicaciones
     fields=['categoria','titlo','post']
     labels={
        'titulo':'',
        'post':'',
        'categoria':'',
    }

    widgets={
                      
            'titulo': forms.TextInput(attrs={'placeholder':'aca va el titulo','class':'form-control'}),

             'post':forms.TextInput(attrs={'placeholder':'escribi algo...','class':'form-control'}),

            'categoria':forms.Select(attrs={'class':'form-select', 'placeholder':'Categoria'}),          

    }



class ComentarioForm(forms.ModelForm):

    class Meta:
      model=Comentario
      fields =  ['texto']

    widgets = {
        'texto' : forms.TextInput(attrs={'placeholder':'Escribe aqui tu comentario', 'class': 'form-control'}),
    }