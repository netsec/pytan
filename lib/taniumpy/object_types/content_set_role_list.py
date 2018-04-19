
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class ContentSetRoleList(BaseType):

    _soap_tag = 'content_set_roles'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={},
            list_properties={'content_set_role': ContentSetRole},
        )
        
        
        self.content_set_role = []

from content_set_role import ContentSetRole

