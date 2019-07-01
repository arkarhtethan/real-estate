from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:

        model = User

        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):

        email = self.cleaned_data.get('email')

        users = User.objects.all()

        for user in users:

            if user.email == email:

                raise forms.ValidationError("email already taken.")

        return email