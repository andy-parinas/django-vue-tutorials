from django_registration.forms import RegistrationForm

from users.models import AppUser

class AppUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = AppUser