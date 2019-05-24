from pyforms_web.web.middleware import PyFormsMiddleware
from pyforms_web.widgets.django import ModelFormWidget
from pyforms.controls import ControlEmptyWidget
from pyforms.controls import ControlAutoComplete
from django.contrib.contenttypes.models import ContentType
from model_extra_fields.models import Form, FormObject
from .custom_form import CustomForm

class CustomModelForm(ModelFormWidget):


    def __init__(self, *args, **kwargs):
        self._custom_form_app_id = None

        self.select_form = ControlAutoComplete('Form', changed_event=self.__update_custom_form_evt)
        self.customized_form = ControlEmptyWidget(name='customized_form', parent=self)

        super().__init__(*args, **kwargs)

    def create_model_formfields(self):
        super().create_model_formfields()
        ctype = ContentType.objects.get_for_model(self.model)
        self.select_form.queryset = Form.objects.filter(content_type=ctype)

    def __update_custom_form_evt(self):
        formtype = self.select_form.objects.first() if self.select_form.objects else None

        if formtype:
            custom_form_app = CustomForm(form_type=formtype)
            self.customized_form.value = custom_form_app
            self._custom_form_app_id = custom_form_app.uid
            self._custom_form_app = custom_form_app
        else:
            self._custom_form_app_id = None
            self._custom_form_app = None
            self.customized_form.value = None
            self.customized_form.mark_to_update_client()


    def save_custom_model_form(self):
        formtype = self.select_form.objects.first()

        if formtype is None:
            ctype = ContentType.objects.get_for_model(self.model)
            FormObject.objects.filter(
                content_type=ctype, object_id=self.object_pk
            ).delete()

        else:
            if self._custom_form_app_id:
                custom_form_app = PyFormsMiddleware.get_instance(self._custom_form_app_id)
                custom_form_app.save_custom_form(self.model_object)


    def load_custom_model_form(self):
        if self._custom_form_app_id:
            custom_form_app = self._custom_form_app if self._custom_form_app else PyFormsMiddleware.get_instance(self._custom_form_app_id)
            custom_form_app.load_custom_form(self.model_object)


    def save_event(self, obj, new_object):
        res = super().save_event(obj, new_object)
        self.save_custom_model_form()
        return res

    def show_edit_form(self, pk=None):
        res = super().show_edit_form(pk)

        ctype = ContentType.objects.get_for_model(self.model)
        formobj = FormObject.objects.filter(content_type=ctype, object_id=pk).first()

        if formobj:
            self.select_form.value = formobj.form_type.pk

        self.load_custom_model_form()
        return res