from pyforms.basewidget import no_columns
from pyforms_web.web.middleware import PyFormsMiddleware
from pyforms_web.widgets.django.modelform import ModelFormWidget
from model_extra_fields.models import ExtraField
from pyforms.controls import ControlEmptyWidget
from .fields.control_text import ControlTextParameters
from .fields.control_checkbox import ControlCheckBoxParameters
from .fields.control_date import ControlDateParameters
import datetime

class ExtraFieldApp(ModelFormWidget):

    MODEL = ExtraField

    FIELDSETS = [
        ('field_name','field_type', 'mandatory'),
        '_parms'
    ]

    def __init__(self, *args, **kwargs):
        self._parmsapp_uid = None

        self._parms = ControlEmptyWidget(css='ui segment red', parent=self, name='_parms')

        super().__init__(*args, **kwargs)

        self.__field_type_changed_evt()

        self.field_type.changed_event = self.__field_type_changed_evt

    def __field_type_changed_evt(self):
        obj   = self.model_object

        parms = eval(obj.field_parms) if obj else {}

        if self.field_type.value=='ControlText':
            app = ControlTextParameters()

        elif self.field_type.value=='ControlCheckBox':
            app = ControlCheckBoxParameters()

        elif self.field_type.value=='ControlDate':
            app = ControlDateParameters()

        else:
            app = None

        self._parms.value  = app

        if app:
            app.set_parameters(parms)
            self._parmsapp_uid = app.uid


    def update_object_fields(self, obj):
        obj = super().update_object_fields(obj)

        app_uid = self._parmsapp_uid
        if app_uid:
            app = PyFormsMiddleware.get_instance(self._parmsapp_uid)
            obj.field_parms = str(app.get_parameters())


        return obj


