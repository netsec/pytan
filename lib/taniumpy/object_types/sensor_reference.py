
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class SensorReference(BaseType):

    _soap_tag = 'sensor_reference'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={'name': str,
                        'start_char': int,
                        'real_ms_avg': int},
            complex_properties={},
            list_properties={},
        )
        self.name = None
        self.start_char = None
        self.real_ms_avg = None
        
        



