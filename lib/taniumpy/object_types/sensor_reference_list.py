
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class SensorReferenceList(BaseType):

    _soap_tag = 'sensor_references'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={'sensor_reference': SensorReference},
            list_properties={},
        )
        
        self.sensor_reference = None
        

from sensor_reference import SensorReference

