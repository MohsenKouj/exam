from django import forms
from .models import Users
class formic(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255,widget=forms.PasswordInput)
    email = forms.EmailField(max_length=255)
    birthday = forms.DateField()
    female = forms.BooleanField()
    male = forms.BooleanField()

class usersForm(forms.ModelForm):
    
    class Meta:
        model = Users
        fields = '__all__'