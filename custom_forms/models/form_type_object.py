from django.db import models
from django.contrib.contenttypes.models import ContentType

class FormTypeObject(models.Model):

    object_id    = models.PositiveIntegerField('Object id')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    form_type    = models.ForeignKey('FormType', on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.form_type} - {self.object_id}'


    class Meta:
        unique_together = [
            ('object_id', 'content_type'),
            ('object_id', 'form_type')
        ]
