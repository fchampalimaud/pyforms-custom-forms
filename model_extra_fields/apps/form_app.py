from pyforms.basewidget import segment, no_columns
from pyforms_web.widgets.django import ModelAdminWidget, ModelFormWidget
from .extra_field_app.list import FormTypeFieldsApp
from model_extra_fields.models import Form
from confapp import conf


class FormEditApp(ModelFormWidget):
    MODEL = Form
    INLINES = [FormTypeFieldsApp]

    FIELDSETS = [
        no_columns('form_code', 'content_type', 'active'),
        'form_title',
        'form_set',
        segment('FormTypeFieldsApp')
    ]

    AUTHORIZED_GROUPS = ['superuser']

    def get_readonly(self, default):
        if self.object_pk:
            return default + ['content_type']
        else:
            return default


class FormApp(ModelAdminWidget):

    UID = 'custom-forms'
    MODEL = Form

    #SEARCH_FIELDS = ['label__icontains', 'text__icontains']
    LIST_DISPLAY = ['active', 'form_code', 'form_title', 'content_type']
    LIST_COLS_SIZES = ['30px', '20%', '50%', '50px']
    LIST_COLS_ALIGN = ['center', 'center', 'left', 'center']
    #LIST_FILTER = ['notification_type__label', 'user', 'created_on', 'period']

    TITLE = 'Custom forms'

    EDITFORM_CLASS = FormEditApp

    LAYOUT_POSITION         = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU          = 'user'
    ORQUESTRA_MENU_ICON     = 'window restore'
    ORQUESTRA_MENU_ORDER    = 0

    #AUTHORIZED_GROUPS = ['superuser']


