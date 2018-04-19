
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class ContentSetList(BaseType):

    _soap_tag = 'content_sets'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={},
            list_properties={'content_set': ContentSet},
        )
        
        
        self.content_set = []

from content_set import ContentSet

