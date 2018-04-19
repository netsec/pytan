
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class ContentSetRolePrivilegeList(BaseType):

    _soap_tag = 'content_set_role_privileges'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={},
            list_properties={'content_set_role_privilege': ContentSetRolePrivilege},
        )
        
        
        self.content_set_role_privilege = []

from content_set_role_privilege import ContentSetRolePrivilege

