
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class EffectiveContentSetPrivilegeList(BaseType):

    _soap_tag = 'effective_content_set_privileges'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={},
            list_properties={'effective_content_set_privilege': EffectiveContentSetPrivilege},
        )
        
        
        self.effective_content_set_privilege = []

from effective_content_set_privilege import EffectiveContentSetPrivilege

