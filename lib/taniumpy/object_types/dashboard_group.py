
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class DashboardGroup(BaseType):

    _soap_tag = 'dashboard_group'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={'id': int,
                        'name': str,
                        'public_flag': int,
                        'editable_flag': int,
                        'other_flag': int,
                        'text': str,
                        'display_index': int,
                        'icon': str},
            complex_properties={'user': User,
                        'content_set': ContentSet,
                        'dashboard_list': DashboardList},
            list_properties={},
        )
        self.id = None
        self.name = None
        self.public_flag = None
        self.editable_flag = None
        self.other_flag = None
        self.text = None
        self.display_index = None
        self.icon = None
        self.user = None
        self.content_set = None
        self.dashboard_list = None
        

from user import User
from content_set import ContentSet
from dashboard_list import DashboardList

