from django import forms

class People(forms.Form):
  first_name=forms.CharField(
    label="nombre",
    max_length=30,
    min_length=10,
    widget=forms.TextInput(attrs={'class':'input'}),
    )
  
  last_name=forms.CharField(
    label="apellido",
    max_length=30,
    min_length=10,
    widget=forms.TextInput(attrs={'class':'input'}),

    )
  date=forms.CharField(
    label="fecha de nacimiento",
    widget=forms.TextInput(attrs={'class':'input'}),
    )
  email=forms.CharField(
    label="correo",
    max_length=50,
    widget=forms.TextInput(attrs={'class':'input'}),
    )
  dni =forms.CharField(
    label="Documento",
    max_length=10,
    min_length=10,
    widget=forms.TextInput(attrs={'class':'input'}),
    )

  