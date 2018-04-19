
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class LdapSyncConnectorList(BaseType):

    _soap_tag = 'ldap_sync_connector_list'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={},
            list_properties={'ldap_sync_connector': LdapSyncConnector},
        )
        
        
        self.ldap_sync_connector = []

from ldap_sync_connector import LdapSyncConnector

