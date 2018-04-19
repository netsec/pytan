
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class SavedQuestionQuestion(BaseType):

    _soap_tag = 'saved_question_question'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={'saved_question': IdReference,
                        'questions': QuestionList},
            list_properties={},
        )
        
        self.saved_question = None
        self.questions = None
        

from id_reference import IdReference
from question_list import QuestionList

