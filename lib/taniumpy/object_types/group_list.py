
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class GroupList(BaseType):

    _soap_tag = 'groups'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={'cache_info': CacheInfo},
            list_properties={'group': Group},
        )
        
        self.cache_info = None
        self.group = []

from group import Group
from cache_info import CacheInfo

