
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class ContentSetRole(BaseType):

    _soap_tag = 'content_set_role'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={'id': int,
                        'name': str,
                        'description': str,
                        'reserved_name': str,
                        'deny_flag': int,
                        'all_content_sets_flag': int,
                        'category': str},
            complex_properties={'metadata': MetadataList,
                        'content_set_role_privileges': ContentSetRolePrivilegeOnRoleList},
            list_properties={},
        )
        self.id = None
        self.name = None
        self.description = None
        self.reserved_name = None
        self.deny_flag = None
        self.all_content_sets_flag = None
        self.category = None
        self.metadata = None
        self.content_set_role_privileges = None
        

from metadata_list import MetadataList
from content_set_role_privilege_on_role_list import ContentSetRolePrivilegeOnRoleList

