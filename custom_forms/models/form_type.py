from django.db import models
from django.contrib.contenttypes.models import ContentType

class FormType(models.Model):

    form_name = models.CharField('Title', max_length=255)
    form_code = models.SlugField('Code', max_length=50, unique=True)
    form_set  = models.TextField('Formset')
    active    = models.BooleanField('Active')


    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)


    def __str__(self):
        return self.form_name
