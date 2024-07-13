#from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()
from django.conf import settings
from django_registration import validators

class JoinForm(UserCreationForm):

  class Meta(UserCreationForm.Meta):
    model = User
    fields = [
      User.USERNAME_FIELD,
      'password1',
      'password2'
    ]

  error_css_class = 'error'
  required_css_class = 'required'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    email_field = User.get_email_field_name()
    if hasattr(self, 'reserved_names'):
      reserved_names = self.reserved_names
    else:
      reserved_names = validators.DEFAULT_RESERVED_NAMES
    username_validators = [
      validators.ReservedNameValidator(reserved_names),
      validators.validate_confusables
    ]
    self.fields[User.USERNAME_FIELD].validators.extend(username_validators)

  #def save(self, commit=True):
    #user = super().save(commit=False)

    # Save the provided password in hashed format
    #user.set_password(self.cleaned_data["password"])

    #if commit:
    #  user.save()
    #return user

