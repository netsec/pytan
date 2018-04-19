
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class ContentSetRolePrivilege(BaseType):

    _soap_tag = 'content_set_role_privilege'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={'id': int},
            complex_properties={'content_set': IdReference,
                        'content_set_role': IdReference,
                        'content_set_privilege': IdReference},
            list_properties={},
        )
        self.id = None
        self.content_set = None
        self.content_set_role = None
        self.content_set_privilege = None
        

from id_reference import IdReference
from id_reference import IdReference
from id_reference import IdReference

