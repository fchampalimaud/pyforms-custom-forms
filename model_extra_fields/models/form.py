from django.db import models
from django.contrib.contenttypes.models import ContentType

class Form(models.Model):

    active     = models.BooleanField('Active')
    form_code  = models.SlugField('Code', max_length=50)
    form_title = models.CharField('Title', max_length=255)
    form_set   = models.TextField('Formset')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    def __str__(self):
        return self.form_title

    class Meta:
        unique_together = [
            ('form_code', 'content_type')
        ]
