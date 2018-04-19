
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class ParameterValueList(BaseType):

    _soap_tag = 'parameter_values'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={'value': str},
            complex_properties={},
            list_properties={},
        )
        self.value = None
        
        



