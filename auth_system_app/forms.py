from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import CustomUser, AccessCode

class OfficerRegistrationForm(UserCreationForm):
    access_code = forms.CharField(label="Код доступу", max_length=64)

    class Meta:
        model = CustomUser
        fields = ('username','last_name','patronymic','battalion_number','password1','password2','access_code')

    def clean_access_code(self):
        code = self.cleaned_data['access_code']
        try:
            access = AccessCode.objects.get(code=code)
        except AccessCode.DoesNotExist:
            raise forms.ValidationError("Невірний код доступу.")
        if access.is_used:
            raise forms.ValidationError("Цей код вже використано.")
        return code

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            # Позначаємо код як використаний
            code = AccessCode.objects.get(code=self.cleaned_data['access_code'])
            code.is_used = True
            code.issued_to = user.username
            code.save()
        return user


class OfficerAuthenticationForm(AuthenticationForm):
    pass
