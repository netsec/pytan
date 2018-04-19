
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class EffectiveContentSetPrivilegeRequest(BaseType):

    _soap_tag = 'effective_content_set_privileges'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={},
            list_properties={'user': User},
        )
        
        
        self.user = []

from user import User

