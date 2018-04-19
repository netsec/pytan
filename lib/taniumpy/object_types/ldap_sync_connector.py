
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class LdapSyncConnector(BaseType):

    _soap_tag = 'ldap_sync_connector'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={'id': int,
                        'name': str,
                        'enable': int,
                        'host': str,
                        'port': int,
                        'secure': int,
                        'use_ntlm': int,
                        'ldap_user': str,
                        'ldap_password': str,
                        'base_users': str,
                        'filter_users': str,
                        'members_only_flag': int,
                        'user_id': str,
                        'user_name': str,
                        'user_domain': str,
                        'user_display_name': str,
                        'base_groups': str,
                        'filter_groups': str,
                        'group_id': str,
                        'group_name': str,
                        'group_member': str,
                        'last_sync_timestamp': str,
                        'last_sync_result': str,
                        'disable_ldap_auth': int},
            complex_properties={},
            list_properties={},
        )
        self.id = None
        self.name = None
        self.enable = None
        self.host = None
        self.port = None
        self.secure = None
        self.use_ntlm = None
        self.ldap_user = None
        self.ldap_password = None
        self.base_users = None
        self.filter_users = None
        self.members_only_flag = None
        self.user_id = None
        self.user_name = None
        self.user_domain = None
        self.user_display_name = None
        self.base_groups = None
        self.filter_groups = None
        self.group_id = None
        self.group_name = None
        self.group_member = None
        self.last_sync_timestamp = None
        self.last_sync_result = None
        self.disable_ldap_auth = None
        
        



