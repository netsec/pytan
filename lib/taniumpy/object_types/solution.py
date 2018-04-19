
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class Solution(BaseType):

    _soap_tag = 'solution'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={'id': int,
                        'solution_id': str,
                        'name': str,
                        'imported_version': str,
                        'signature': str,
                        'last_update': str,
                        'dup_resolve_type': int,
                        'imported_by': str,
                        'description': str,
                        'category': str,
                        'installed_xml_url': str,
                        'delete_xml_url': str,
                        'deleted_flag': int},
            complex_properties={},
            list_properties={},
        )
        self.id = None
        self.solution_id = None
        self.name = None
        self.imported_version = None
        self.signature = None
        self.last_update = None
        self.dup_resolve_type = None
        self.imported_by = None
        self.description = None
        self.category = None
        self.installed_xml_url = None
        self.delete_xml_url = None
        self.deleted_flag = None
        
        



