from django import forms
from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

# class SignUpForm(UserCreationForm):
#     class meta:
#         model = get_user_model()
#         fields = ('email', 'first_name', 'last_name', 'user_username', 'password1', 'password2')

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    # email = forms.CharField(label='Email', widget=forms.EmailInput, required=False)
    # first_name = forms.CharField(label='First Name', widget=forms.TextInput, required=False)
    # last_name = forms.CharField(label='Last Name', widget=forms.TextInput, required=False)
    user_username = forms.CharField(label='Username', widget=forms.TextInput)

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'user_username', )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user