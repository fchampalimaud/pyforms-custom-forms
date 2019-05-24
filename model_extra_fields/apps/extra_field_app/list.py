from pyforms_web.widgets.django import ModelAdminWidget
from model_extra_fields.models import ExtraField
from .form import ExtraFieldApp

class FormTypeFieldsApp(ModelAdminWidget):

    TITLE = 'Fields'
    MODEL = ExtraField

    LIST_DISPLAY = ['field_name', 'field_type', 'mandatory']
    LIST_HEADERS = ['Field name', 'Type', 'It is mandatory']
    LIST_COLS_ALIGN = ['left', 'center', 'center']
    LIST_COLS_SIZES = ['40%', '30%', '30%']

    EDITFORM_CLASS = ExtraFieldApp
