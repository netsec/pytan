
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class ActionGroup(BaseType):

    _soap_tag = 'action_group'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={'id': int,
                        'name': str,
                        'and_flag': int,
                        'public_flag': int,
                        'deleted_flag': int},
            complex_properties={'groups': GroupList,
                        'user_groups': UserGroupList},
            list_properties={},
        )
        self.id = None
        self.name = None
        self.and_flag = None
        self.public_flag = None
        self.deleted_flag = None
        self.groups = None
        self.user_groups = None
        

from group_list import GroupList
from user_group_list import UserGroupList

