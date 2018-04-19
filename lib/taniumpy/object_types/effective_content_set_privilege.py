
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class EffectiveContentSetPrivilege(BaseType):

    _soap_tag = 'effective_content_set_privilege'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={'content_set': ContentSet,
                        'content_set_privilege_list': ContentSetPrivilegeList},
            list_properties={},
        )
        
        self.content_set = None
        self.content_set_privilege_list = None
        

from content_set import ContentSet
from content_set_privilege_list import ContentSetPrivilegeList

