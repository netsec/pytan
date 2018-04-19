
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class User(BaseType):

    _soap_tag = 'user'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={'id': int,
                        'name': str,
                        'domain': str,
                        'display_name': str,
                        'group_id': int,
                        'effective_group_id': int,
                        'deleted_flag': int,
                        'last_login': str,
                        'active_session_count': int,
                        'local_admin_flag': int},
            complex_properties={'permissions': PermissionList,
                        'roles': UserRoleList,
                        'metadata': MetadataList,
                        'content_set_roles': ContentSetRoleList,
                        'effective_content_set_privileges': EffectiveContentSetPrivilegeList,
                        'owned_object_ids': UserOwnedObjectIds},
            list_properties={},
        )
        self.id = None
        self.name = None
        self.domain = None
        self.display_name = None
        self.group_id = None
        self.effective_group_id = None
        self.deleted_flag = None
        self.last_login = None
        self.active_session_count = None
        self.local_admin_flag = None
        self.permissions = None
        self.roles = None
        self.metadata = None
        self.content_set_roles = None
        self.effective_content_set_privileges = None
        self.owned_object_ids = None
        

from permission_list import PermissionList
from user_role_list import UserRoleList
from metadata_list import MetadataList
from content_set_role_list import ContentSetRoleList
from effective_content_set_privilege_list import EffectiveContentSetPrivilegeList
from user_owned_object_ids import UserOwnedObjectIds

