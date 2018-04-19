
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class AuditData(BaseType):

    _soap_tag = 'entry'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={'object_id': int,
                        'details': str,
                        'creation_time': str,
                        'modification_time': str,
                        'last_modified_by': str,
                        'modifier_user_id': int,
                        'type': int},
            complex_properties={},
            list_properties={},
        )
        self.object_id = None
        self.details = None
        self.creation_time = None
        self.modification_time = None
        self.last_modified_by = None
        self.modifier_user_id = None
        self.type = None
        
        



