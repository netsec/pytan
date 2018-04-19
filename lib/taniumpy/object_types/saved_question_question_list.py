
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class SavedQuestionQuestionList(BaseType):

    _soap_tag = 'saved_question_questions'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={},
            list_properties={'saved_question_question': SavedQuestionQuestion},
        )
        
        
        self.saved_question_question = []

from saved_question_question import SavedQuestionQuestion

