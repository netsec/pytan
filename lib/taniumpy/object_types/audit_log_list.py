
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class AuditLogList(BaseType):

    _soap_tag = 'audit_logs'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={},
            list_properties={'audit_log': AuditLog},
        )
        
        
        self.audit_log = []

from audit_log import AuditLog

