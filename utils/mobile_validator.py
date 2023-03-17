from django.utils.deconstruct import deconstructible
from django.core import validators
from django.utils.translation import gettext_lazy as _

@deconstructible
class MobileNumberValidator(validators.RegexValidator):
    regex = r'^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$'
    message = _(
        'Enter a Valid Indian Phone Number'
    )
    flags = 0