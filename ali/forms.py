from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(label='Your Email', max_length=100)
