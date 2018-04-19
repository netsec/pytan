
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class ParseResultGroup(BaseType):

    _soap_tag = 'parse_result_group'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={'score': int,
                        'question_text': str},
            complex_properties={'parse_results': ParseResultList,
                        'question': Question,
                        'question_group_sensors': SensorList,
                        'parameter_values': ParameterValueList,
                        'sensor_references': SensorReferenceList},
            list_properties={},
        )
        self.score = None
        self.question_text = None
        self.parse_results = None
        self.question = None
        self.question_group_sensors = None
        self.parameter_values = None
        self.sensor_references = None
        

from parse_result_list import ParseResultList
from question import Question
from sensor_list import SensorList
from parameter_value_list import ParameterValueList
from sensor_reference_list import SensorReferenceList

