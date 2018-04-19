
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class DashboardList(BaseType):

    _soap_tag = 'dashboard_list'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={},
            list_properties={'dashboard': Dashboard},
        )
        
        
        self.dashboard = []

from dashboard import Dashboard

