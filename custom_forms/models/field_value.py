from django.db import models

class FieldValue(models.Model):

    value = models.TextField('Value')
    formtype_field  = models.ForeignKey('FormTypeField', on_delete=models.CASCADE)
    formtype_object = models.ForeignKey('FormTypeObject', on_delete=models.CASCADE)

    def __str__(self):
        return f'Form:{self.formtype_object} | Field:{self.formtype_field}  | Value:{self.value} '


    class Meta:
        unique_together = [
            ('formtype_field', 'formtype_object')
        ]
