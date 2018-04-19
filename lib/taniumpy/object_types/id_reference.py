
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class IdReference(BaseType):

    _soap_tag = 'content_set'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={'id': int,
                        'name': str},
            complex_properties={},
            list_properties={},
        )
        self.id = None
        self.name = None
        
        



