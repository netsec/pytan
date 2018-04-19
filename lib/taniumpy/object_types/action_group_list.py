
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class ActionGroupList(BaseType):

    _soap_tag = 'action_groups'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={},
            list_properties={'action_group': ActionGroup},
        )
        
        
        self.action_group = []

from action_group import ActionGroup

