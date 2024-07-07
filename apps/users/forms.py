from django.contrib.auth.hashers import make_password
from django.forms import ModelForm
from apps.users.models import CustomUser


class UserCreateForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'first_name')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user