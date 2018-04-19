
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class ContentSet(BaseType):

    _soap_tag = 'content_set'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={'id': int,
                        'name': str,
                        'description': str,
                        'reserved_name': str},
            complex_properties={'metadata': MetadataList},
            list_properties={},
        )
        self.id = None
        self.name = None
        self.description = None
        self.reserved_name = None
        self.metadata = None
        

from metadata_list import MetadataList

