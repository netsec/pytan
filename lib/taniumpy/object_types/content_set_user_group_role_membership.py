
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class ContentSetUserGroupRoleMembership(BaseType):

    _soap_tag = 'content_set_user_group_role_membership'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={'id': int},
            complex_properties={'user_group': IdReference,
                        'content_set_role': IdReference},
            list_properties={},
        )
        self.id = None
        self.user_group = None
        self.content_set_role = None
        

from id_reference import IdReference
from id_reference import IdReference

