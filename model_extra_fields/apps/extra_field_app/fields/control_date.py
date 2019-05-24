from .control_base import ControlBaseParameters
from pyforms.controls import ControlDate

class ControlDateParameters(ControlBaseParameters):

    TITLE = 'ControlDate parameters'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._p_default = ControlDate('Default value')
