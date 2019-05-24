from django.db import models
from django.contrib.contenttypes.models import ContentType

class FormObject(models.Model):

    object_id    = models.PositiveIntegerField('Object id')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    custom_form  = models.ForeignKey('Form', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.custom_form} (obj-id:{self.object_id})'

    class Meta:
        unique_together = [
            ('object_id', 'content_type'),
            ('object_id', 'custom_form')
        ]
