
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class UserGroupList(BaseType):

    _soap_tag = 'user_groups'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={},
            list_properties={'user_group': UserGroup},
        )
        
        
        self.user_group = []

from user_group import UserGroup

