from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı adı")
    password = forms.CharField(label="Parola",widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label = "Kullanıcı adı")
    password = forms.CharField(max_length = 50, label= "Parola" , widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=50, label="Parolayı doğrulayın", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Parolalar eşleşmiyor.")
        
        values = {
            "username": username,
            "password":password,
        }
        
        return values