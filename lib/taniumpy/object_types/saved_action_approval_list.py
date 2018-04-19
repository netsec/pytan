
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class SavedActionApprovalList(BaseType):

    _soap_tag = 'saved_action_approvals'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={},
            list_properties={'saved_action_approval': SavedActionApproval},
        )
        
        
        self.saved_action_approval = []

from saved_action_approval import SavedActionApproval

