from django import forms
from django.contrib.auth.forms import SetPasswordForm as DjangoSetPasswordForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


UserModel = get_user_model()

class UserEmailForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Verifica si el correo electrónico está registrado
        if not UserModel.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico no está registrado.')
        return email
    
    
class PasswordResetForm (forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['autofocus'] = True
        
    email = forms.EmailField(label='Correo electrónico')
    
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Verifica si el correo electrónico está registrado
        if not UserModel.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico no está registrado.')
        return email
    

class SetPasswordForm(DjangoSetPasswordForm):
    def _init_(self, user, *args, **kwargs):
        self.user = user
        super()._init_(user, *args, **kwargs)

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data["new_password1"])
        if commit:
            self.user.save()
        return self.user
    
    UserModel = get_user_model()
    
class CustomLoginForm(AuthenticationForm):
    def clean_username(self):
        email = self.cleaned_data.get('username')  # Django usa 'username' aunque sea email para autenticación
        if not UserModel.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico no está registrado.')
        return email