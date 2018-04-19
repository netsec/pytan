
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class AuditLog(BaseType):

    _soap_tag = 'audit_log'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={'id': int,
                        'type': str},
            complex_properties={'entries': AuditDataList},
            list_properties={},
        )
        self.id = None
        self.type = None
        self.entries = None
        

from audit_data_list import AuditDataList

