from django import forms
from django.contrib.auth.models import User

class UserEmailForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Verifica si el correo electrónico está registrado
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico no está registrado.')
        return email
