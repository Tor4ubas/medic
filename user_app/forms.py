from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from user_app.models import User


class StyleFormMixin:
    """
    Класс Mixin для стилизации форм.
    """

    def __init__(self, *args, **kwargs):
        """
        Инициализация класса StyleFormMixin.
        """
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """
    Класс для формы регистрации пользователя.
    """

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserForm(StyleFormMixin, UserChangeForm):
    """
    Класс для формы редактирования пользователя.
    """

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone', 'country', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
