from .control_base import ControlBaseParameters
from pyforms.controls import ControlCombo

class ControlCheckBoxParameters(ControlBaseParameters):

    TITLE = 'ControlCheckBox parameters'


    OPTIONS = [
        ('True', True),
        ('False', False)
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._p_default = ControlCombo('Default value', items=self.OPTIONS)


