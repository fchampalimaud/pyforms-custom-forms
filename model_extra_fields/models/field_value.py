from django.db import models

class FieldValue(models.Model):

    value  = models.TextField('Value', null=True, blank=True)
    field  = models.ForeignKey('ExtraField',  on_delete=models.CASCADE)
    form_object = models.ForeignKey('FormObject', on_delete=models.CASCADE)

    def __str__(self):
        return f'Form:{self.form_object} | Field:{self.field}  | Value:{self.value} '


    class Meta:
        unique_together = [
            ('field', 'form_object')
        ]
