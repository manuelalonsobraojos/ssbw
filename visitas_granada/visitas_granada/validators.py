from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validateCapital(value):

    value_c = value.capitalize()
    if value != value_c:
        raise ValidationError(_("Sorry, the email submitted is invalid. All emails have to be registered on this domain only.", status='invalid'))
