
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class UserGroup(BaseType):

    _soap_tag = 'user_group'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={'id': int,
                        'name': str,
                        'deleted_flag': int},
            complex_properties={'user_list': UserList,
                        'content_set_roles': ContentSetRoleList,
                        'group': Group},
            list_properties={},
        )
        self.id = None
        self.name = None
        self.deleted_flag = None
        self.user_list = None
        self.content_set_roles = None
        self.group = None
        

from user_list import UserList
from content_set_role_list import ContentSetRoleList
from group import Group

