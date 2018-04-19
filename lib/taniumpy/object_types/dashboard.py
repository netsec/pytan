
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class Dashboard(BaseType):

    _soap_tag = 'dashboard'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={'id': int,
                        'name': str,
                        'public_flag': int,
                        'text': str},
            complex_properties={'user': User,
                        'content_set': ContentSet,
                        'group': Group,
                        'saved_question_list': SavedQuestionList},
            list_properties={},
        )
        self.id = None
        self.name = None
        self.public_flag = None
        self.text = None
        self.user = None
        self.content_set = None
        self.group = None
        self.saved_question_list = None
        

from user import User
from content_set import ContentSet
from group import Group
from saved_question_list import SavedQuestionList

