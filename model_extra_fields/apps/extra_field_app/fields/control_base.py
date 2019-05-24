from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlCheckBox

class ControlBaseParameters(BaseWidget):

    TITLE = 'ControlBase parameters'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._p_label         = ControlText('Label')
        self._p_helptext      = ControlText('Help text')
        self._p_default       = ControlText('Default value')
        self._p_css           = ControlText('Css')
        self._p_field_css     = ControlText('Field css')
        self._p_label_visible = ControlCheckBox('The label is visible', default=True)

        self.formset = [
            ('_p_label', '_p_default'),
            '_p_helptext',
            ' ',
            ('_p_css', '_p_field_css'),
            '_p_label_visible'
        ]

    def set_parameters(self, data):
        self._p_label.value         = data.get('label', '')
        self._p_helptext.value      = data.get('helptext', '')
        self._p_default.value       = data.get('default', None)
        self._p_css.value           = data.get('css', '')
        self._p_field_css.value     = data.get('field_css', '')
        self._p_label_visible.value = data.get('label_visible', '')


    def get_parameters(self):
        return {
            'label':         self._p_label.value,
            'helptext':      self._p_helptext.value,
            'default':       self._p_default.value,
            'css':           self._p_css.value,
            'field_css':     self._p_field_css.value,
            'label_visible': self._p_label_visible.value,
        }