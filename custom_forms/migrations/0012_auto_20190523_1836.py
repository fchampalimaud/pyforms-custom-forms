# Generated by Django 2.2 on 2019-05-23 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('custom_forms', '0011_fieldvalue_formtypeobject'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='formtypeobject',
            unique_together={('object_id', 'content_type')},
        ),
    ]