
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class ImportConflictOptions(BaseType):

    _soap_tag = 'import_conflict_options'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={},
            list_properties={'import_conflict_option': int},
        )
        
        
        self.import_conflict_option = []



