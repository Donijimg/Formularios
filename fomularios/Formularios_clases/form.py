from django import forms

class Contact(forms.Form):
  firs_name=forms.CharField(
    label="nombre",
    max_length=50,
    min_length=10,
    widget=forms.TextInput(attrs={'class':'input'}),
    initial='Dion'
    )
  
  # opcions=(
  #   ('1','Colombia'),
  #   ('2','Brazil')
  # )

  # ciudad=forms.ChoiceField(choise=opcions,widget=forms.Select(attrs={'class':'input'})),
  
  last_name=forms.CharField(
    label="apellido",
    max_length=50,
    min_length=10,
    widget=forms.TextInput(attrs={'class':'input', "id" : "otro_id"}),
    initial='Cupid'
    )
  asunto=forms.CharField(
    label="asunto",
    max_length=50,
    widget=forms.TextInput(attrs={'class':'input'}),
    initial='Constructor'
    )
  mensaje=forms.CharField(
    label="mensaje",
    max_length=50,
    widget=forms.TextInput(attrs={'class':'input'}),
    initial='Procesando...'
    )
  generos = {
      ("mujer","mujer"),
      ("hombre","hombre"),
      ("otro","otro"),
      ("---","---")}
  select=forms.ChoiceField(choices=generos,widget=forms.Select,label="genero")
  
  