from django.core.exceptions import ValidationError
from pyforms_web.basewidget import BaseWidget
from model_extra_fields.models import Form, FormObject, FieldValue
from pyforms.basewidget import no_columns, segment
import datetime

class CustomForm(BaseWidget):

    CUSTOM_FORM_CODE = None

    def __init__(self, *args, **kwargs):

        formtype = kwargs.get('custom_form', None)
        formcode = kwargs.get('form_code', self.CUSTOM_FORM_CODE)

        if formtype is None and formcode:
            formtype = Form.objects.get(form_code=formcode)

        if formtype is None:
            raise Exception('No form type defined')
        else:
            self.formtype = formtype

        kwargs['title'] = formtype.form_title

        super().__init__(*args, **kwargs)

        for i, field in enumerate(formtype.fields.all()):
            setattr(self, field.field_name, field.create_control() )

        if formtype.form_set:
            self.formset = eval(formtype.form_set)


    def validate_custom_form(self, obj):
        for i, field in enumerate(self.formtype.fields.all()):
            pyforms_field = getattr(self, field.field_name)

            if field.mandatory and not pyforms_field.value:
                pyforms_field.error = True
                raise Exception(f'The field [{field.label}] is mandatory.')



    def save_custom_form(self, obj):
        form_obj, created = FormObject.objects.get_or_create(
            content_type=self.formtype.content_type,
            object_id=obj.pk,
            custom_form=self.formtype
        )

        # remove all existing register if the formtype was updated
        if created:
            FieldValue.objects.filter(form_object=form_obj).delete()

        for i, field in enumerate(self.formtype.fields.all()):
            pyforms_field = getattr(self, field.field_name)

            field_value, created = FieldValue.objects.get_or_create(form_object=form_obj, field=field)
            field_value.value = pyforms_field.value
            field_value.save()


    def load_custom_form(self, obj):
        form_obj = FormObject.objects.get(
            custom_form=self.formtype,
            object_id=obj.pk
        )

        for i, field in enumerate(self.formtype.fields.all()):
            pyforms_field = getattr(self, field.field_name)

            field_value = FieldValue.objects.filter(form_object=form_obj, field=field).first()
            if field_value:
                pyforms_field.value = field_value.value
