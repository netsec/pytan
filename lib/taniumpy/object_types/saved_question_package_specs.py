
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class SavedQuestionPackageSpecs(BaseType):

    _soap_tag = 'saved_question_package_specs'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={'saved_question': IdReference,
                        'packages': PackageSpecList},
            list_properties={},
        )
        
        self.saved_question = None
        self.packages = None
        

from id_reference import IdReference
from package_spec_list import PackageSpecList

