from django import forms

class ContactForm(forms.Form):
    name= forms.CharField(label="Nombre", required=True, widget=forms.TimeInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
    ))
    email= forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu email'}
    ))
    message= forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows':2, 'placeholder':'Escribe tu mensaje'}),
        min_length=10, max_length=1000)