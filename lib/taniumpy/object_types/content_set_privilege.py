
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class ContentSetPrivilege(BaseType):

    _soap_tag = 'content_set_privilege'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={'id': int,
                        'name': str,
                        'reserved_name': str,
                        'privilege_type': str,
                        'privilege_module': str},
            complex_properties={'metadata': MetadataList},
            list_properties={},
        )
        self.id = None
        self.name = None
        self.reserved_name = None
        self.privilege_type = None
        self.privilege_module = None
        self.metadata = None
        

from metadata_list import MetadataList

