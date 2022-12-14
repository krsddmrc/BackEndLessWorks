from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.forms import fields
from .models import Profile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()  #override ettik. boş bırakınca default required true oldu
    
    class Meta:
        model = User
        fields = ("username", "email")
        
    def clean_email(self):
        email = self.cleaned_data['email'] #! form'dan emaili çekiyoruz.
        if User.objects.filter(email=email).exists(): #! eğer daha önce varsa alma
            raise forms.ValidationError("Please use another Email, that one already taken")
        return email
    
    # def clean_first_name(self):
    #     name = self.cleaned_data("first_name")
    #     if "a" in name:
    #         raise forms.ValidationError("Your name includes A")
    #     return name
        
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ("image", "bio")

class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("username", "email")
        
class PasswordResetEmailCheck(PasswordResetForm):
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("There is no email")
        return email