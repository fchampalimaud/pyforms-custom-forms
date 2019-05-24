from django.db import models

class FieldValue(models.Model):

    value  = models.TextField('Value', null=True, blank=True)
    field  = models.ForeignKey('ExtraField',  on_delete=models.CASCADE)
    form_object = models.ForeignKey('FormObject', on_delete=models.CASCADE)

    def __str__(self):
        return f'Form:{self.formtype_object} | Field:{self.formtype_field}  | Value:{self.value} '


    class Meta:
        unique_together = [
            ('formtype_field', 'formtype_object')
        ]
