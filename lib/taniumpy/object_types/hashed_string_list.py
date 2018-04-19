
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class HashedStringList(BaseType):

    _soap_tag = 'hashed_strings'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={},
            list_properties={'hashed_string': HashedString},
        )
        
        
        self.hashed_string = []

from hashed_string import HashedString

