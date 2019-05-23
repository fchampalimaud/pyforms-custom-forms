from pyforms_web.widgets.django import ModelAdminWidget
from custom_forms.models import FormTypeField
from .form import FormTypeFieldApp
from confapp import conf

class FormTypeFieldsApp(ModelAdminWidget):

    MODEL = FormTypeField

    #SEARCH_FIELDS = ['label__icontains', 'text__icontains']
    LIST_DISPLAY = ['field_name', 'field_type']
    #LIST_FILTER = ['notification_type__label', 'user', 'created_on', 'period']

    TITLE = 'Forms types fields'

    EDITFORM_CLASS = FormTypeFieldApp

    LAYOUT_POSITION         = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU          = 'middle-left'
    ORQUESTRA_MENU_ICON     = 'bell blue'
    ORQUESTRA_MENU_ORDER    = 0

    #AUTHORIZED_GROUPS = ['superuser']
