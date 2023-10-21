from django import forms


# In this class we're make the login form.
class login_form(forms.Form):
    username = forms.CharField(
        min_length=4,
        max_length=18,
        label="Kullanıcı adı")
    
    password = forms.CharField(
        min_length=6,
        max_length = 18,
        label="Parola",
        widget=forms.PasswordInput)

# In this class we're make the register form.
class register_form(forms.Form):
    username = forms.CharField(
        min_length=4,   # Min & Max lengths applied to forms
        max_length=18,
        label = "Kullanıcı adı")  
    
    password = forms.CharField(
        min_length=6,
        max_length = 18,
        label= "Parola",
        widget=forms.PasswordInput) 
    
    confirm_password = forms.CharField(
        min_length=6,
        max_length=18, 
        label="Parolayı doğrulayın", 
        widget=forms.PasswordInput) 


    # In this function we're check the user's password.
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Parolalar eşleşmiyor.")

        values = {
            "username": username,
            "password": password,
        }

        return values
