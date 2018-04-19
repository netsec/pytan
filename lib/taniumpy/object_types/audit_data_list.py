
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class AuditDataList(BaseType):

    _soap_tag = 'entries'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={},
            list_properties={'entry': AuditData},
        )
        
        
        self.entry = []

from audit_data import AuditData

