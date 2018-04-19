
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class ContentSetPrivilegeList(BaseType):

    _soap_tag = 'content_set_privileges'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={},
            list_properties={'content_set_privilege': ContentSetPrivilege,
                        'content_set_privilege': ContentSetPrivilege},
        )
        
        
        self.content_set_privilege = []
        self.content_set_privilege = []

from content_set_privilege import ContentSetPrivilege
from content_set_privilege import ContentSetPrivilege

