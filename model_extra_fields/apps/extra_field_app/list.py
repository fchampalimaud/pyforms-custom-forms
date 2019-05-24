from pyforms_web.widgets.django import ModelAdminWidget
from model_extra_fields.models import ExtraField
from .form import ExtraFieldApp

class FormTypeFieldsApp(ModelAdminWidget):

    TITLE = 'Fields'
    MODEL = ExtraField

    LIST_DISPLAY   = ['field_name', 'field_type', 'mandatory']
    EDITFORM_CLASS = ExtraFieldApp
