
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class HashedString(BaseType):

    _soap_tag = 'hashed_string'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={'sensor_hash': int,
                        'value_hash': int,
                        'which_computer_id': int,
                        'value': str,
                        'error_flag': int,
                        'collision_flag': int,
                        'first_collision': str,
                        'second_collision': str},
            complex_properties={},
            list_properties={'first_computer_id': ComputerIdList,
                        'second_computer_id': ComputerIdList},
        )
        self.sensor_hash = None
        self.value_hash = None
        self.which_computer_id = None
        self.value = None
        self.error_flag = None
        self.collision_flag = None
        self.first_collision = None
        self.second_collision = None
        
        self.first_computer_id = []
        self.second_computer_id = []

from computer_id_list import ComputerIdList
from computer_id_list import ComputerIdList

