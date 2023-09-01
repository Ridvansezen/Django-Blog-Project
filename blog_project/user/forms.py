from typing import Any, Dict
from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(min_length=4,max_length=50, label = "Ad Soyad")
    email = forms.EmailField(label="E-Posta")
    username = forms.CharField(max_length=50, label = "Kullanıcı adı")
    password = forms.CharField(max_length = 50, label= "Parola" , widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=50, label="Parolayı doğrulayın", widget=forms.PasswordInput)

    def clean(self):
        name = self.cleaned_data.get("name")
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Parolalar eşleşmiyor.")
        
        values = {
            "name": name,
            "email": email,
            "username": username,
            "password":password,
        }
        
        return values