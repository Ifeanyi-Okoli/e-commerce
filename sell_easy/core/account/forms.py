from django import forms
from .models import Profile

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    
    
class SignUpForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'address', 'phone_number')
        exclude = ('is_verified', 'is_staff', 'is_active', 'is_seller', 'is_admin')
        widgets = {
            'password': forms.PasswordInput(),
        }