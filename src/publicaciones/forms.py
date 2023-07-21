from django import forms
from.models import Publicaciones,Comentarios


class CrearPublicaciones(forms.ModelForm):
    model=Publicaciones
    fields=["titulo","categoria","post"]
    labels={
        "titulo":"",
        "categoria":"",
        "post":"",
    }

    widgets={
                      
            "titulo": forms.TextInput(attrs={"placeholder":"aca va el titulo","class":"form-control"}),

            "categoria":forms.Select(attrs={"class":"form-select", "placeholder":"Categoria"}),

            "post":forms.TextInput(attrs={"placeholder":"escribi algo...","class":"form-control"}),

    }



class Comentarioform(forms.ModelForm):

    class Meta:
      model=Comentarios 
      fields =  ["texto"]