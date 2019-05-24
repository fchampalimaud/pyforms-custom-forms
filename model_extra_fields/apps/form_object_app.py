from pyforms.basewidget import segment, no_columns
from pyforms_web.widgets.django import ModelAdminWidget
from .extra_field_app.list import FormTypeFieldsApp
from model_extra_fields.models import FormObject
from confapp import conf

class FormObjectApp(ModelAdminWidget):

    UID = 'objects-vs-forms-types'
    MODEL = FormObject

    #SEARCH_FIELDS = ['label__icontains', 'text__icontains']
    #LIST_DISPLAY = ['active', 'form_code', 'form_name', 'content_type']
    #LIST_COLS_SIZES = ['30px', '20%', '50%', '50px']
    #LIST_COLS_ALIGN = ['center', 'center', 'left', 'center']
    #LIST_FILTER = ['notification_type__label', 'user', 'created_on', 'period']
    #INLINES = [FormTypeFieldsApp]
    """
    FIELDSETS = [
        no_columns('active','form_code'),
        'form_name',
        'content_type',
        'form_set',
        segment('FormTypeFieldsApp')
    ]"""

    TITLE = 'Objects vs Form'

    LAYOUT_POSITION         = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU          = 'middle-left'
    ORQUESTRA_MENU_ICON     = 'bell blue'
    ORQUESTRA_MENU_ORDER    = 0

    #AUTHORIZED_GROUPS = ['superuser']
