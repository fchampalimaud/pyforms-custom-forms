from django.db import models
import datetime
from pyforms.controls import ControlCheckBox
from pyforms.controls import ControlText
from pyforms.controls import ControlDate

class FormTypeField(models.Model):

    FIELDS_TYPES = [
        ('ControlText', 'Small text'),
        ('ControlCheckBox', 'Check box'),
        ('ControlDate', 'Date')
    ]

    field_name = models.SlugField('Field name', max_length=255)
    field_type  = models.CharField('Field type', max_length=50, choices=FIELDS_TYPES)
    field_parms = models.TextField('Parameters')

    form_type   = models.ForeignKey('FormType', on_delete=models.CASCADE, related_name='fields')

    def __str__(self):
        return self.field_type

    def create_control(self):
        parms   = eval(self.field_parms)
        control = eval(self.field_type)(**parms)
        return control