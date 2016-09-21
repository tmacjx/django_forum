# coding=utf-8

from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _



CELL_RE = r'^1[34578]\d{9}$'




@deconstructible
class CNphoneValidator(object):
    message = _('Enter an China cellphone')
    code = 'invalid'
    def __init__(self, ):



