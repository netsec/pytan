
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class UserOwnedObjectIds(BaseType):

    _soap_tag = 'owned_object_ids'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={},
            complex_properties={'saved_actions': SavedActionList,
                        'saved_questions': SavedQuestionList,
                        'plugin_schedules': PluginScheduleList},
            list_properties={},
        )
        
        self.saved_actions = None
        self.saved_questions = None
        self.plugin_schedules = None
        

from saved_action_list import SavedActionList
from saved_question_list import SavedQuestionList
from plugin_schedule_list import PluginScheduleList

