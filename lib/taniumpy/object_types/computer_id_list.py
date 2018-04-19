
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class ComputerIdList(BaseType):

    _soap_tag = 'first_computer_id'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={},
            list_properties={'id': int},
        )
        
        
        self.id = []



