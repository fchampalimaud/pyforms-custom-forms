from custom_forms.widgets.custom_form import CustomForm
from confapp import conf

class TestApp(CustomForm):

    UID = 'custom-form-test-app'

    TITLE = 'Custom form test'

    CUSTOM_FORM_CODE = 'FIRST_APP'

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'middle-left'
    ORQUESTRA_MENU_ICON = 'bell blue'
    ORQUESTRA_MENU_ORDER = 0