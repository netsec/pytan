
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class ContentSetRoleMembership(BaseType):

    _soap_tag = 'content_set_role_membership'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={'id': int},
            complex_properties={'user': User,
                        'content_set_role': IdReference},
            list_properties={},
        )
        self.id = None
        self.user = None
        self.content_set_role = None
        

from user import User
from id_reference import IdReference

