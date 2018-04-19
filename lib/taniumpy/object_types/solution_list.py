
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class SolutionList(BaseType):

    _soap_tag = 'solutions'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={},
            list_properties={'solution': Solution},
        )
        
        
        self.solution = []

from solution import Solution

