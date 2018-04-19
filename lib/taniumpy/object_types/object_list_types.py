from action import Action
from action_group import ActionGroup
from action_group_list import ActionGroupList
from action_stop import ActionStop
from action_stop_list import ActionStopList
from action_list import ActionList
from system_status_aggregate import SystemStatusAggregate
from archived_question import ArchivedQuestion
from archived_question_list import ArchivedQuestionList
from plugin_argument import PluginArgument
from plugin_argument_list import PluginArgumentList
from audit_log import AuditLog
from audit_log_list import AuditLogList
from cache_info import CacheInfo
from client_count import ClientCount
from client_status import ClientStatus
from plugin_sql_column_list import PluginSqlColumnList
from plugin_command_list import PluginCommandList
from computer_group import ComputerGroup
from computer_group_list import ComputerGroupList
from computer_group_spec import ComputerGroupSpec
from computer_spec_list import ComputerSpecList
from id_reference import IdReference
from content_set_privilege import ContentSetPrivilege
from content_set_privilege_list import ContentSetPrivilegeList
from content_set_role import ContentSetRole
from content_set_role_membership import ContentSetRoleMembership
from content_set_role_membership_list import ContentSetRoleMembershipList
from content_set_role_privilege_on_role import ContentSetRolePrivilegeOnRole
from content_set_role_privilege_on_role_list import ContentSetRolePrivilegeOnRoleList
from content_set_role_list import ContentSetRoleList
from content_set_user_group_role_membership import ContentSetUserGroupRoleMembership
from content_set_user_group_role_membership_list import ContentSetUserGroupRoleMembershipList
from content_set_list import ContentSetList
from dashboard import Dashboard
from dashboard_group import DashboardGroup
from dashboard_list import DashboardList
from effective_content_set_privilege import EffectiveContentSetPrivilege
from effective_content_set_privilege_request import EffectiveContentSetPrivilegeRequest
from audit_data_list import AuditDataList
from audit_data import AuditData
from xml_error import XmlError
from error_list import ErrorList
from package_file import PackageFile
from upload_file_list import UploadFileList
from package_file_status_list import PackageFileStatusList
from package_file_template import PackageFileTemplate
from package_file_template_list import PackageFileTemplateList
from filter import Filter
from filter_list import FilterList
from computer_id_list import ComputerIdList
from group import Group
from group_list import GroupList
from hashed_string import HashedString
from hashed_string_list import HashedStringList
from import_conflict_options import ImportConflictOptions
from question_list_info import QuestionListInfo
from metadata_item import MetadataItem
from ldap_sync_connector import LdapSyncConnector
from ldap_sync_connector_list import LdapSyncConnectorList
from metadata_list import MetadataList
from object_list import ObjectList
from options import Options
from user_owned_object_ids import UserOwnedObjectIds
from package_file_list import PackageFileList
from package_spec import PackageSpec
from package_spec_list import PackageSpecList
from parameter import Parameter
from parameter_value_list import ParameterValueList
from parameter_list import ParameterList
from parse_job import ParseJob
from parse_job_list import ParseJobList
from parse_result import ParseResult
from parse_result_group import ParseResultGroup
from parse_result_group_list import ParseResultGroupList
from parse_result_list import ParseResultList
from permission_list import PermissionList
from plugin import Plugin
from plugin_schedule import PluginSchedule
from plugin_schedule_list import PluginScheduleList
from plugin_list import PluginList
from saved_action_policy import SavedActionPolicy
from sensor_query_list import SensorQueryList
from sensor_query import SensorQuery
from question import Question
from question_list import QuestionList
from plugin_sql_result_list import PluginSqlResultList
from user_role import UserRole
from user_role_list import UserRoleList
from saved_action_row_id_list import SavedActionRowIdList
from saved_action import SavedAction
from saved_action_approval import SavedActionApproval
from saved_action_approval_list import SavedActionApprovalList
from saved_action_list import SavedActionList
from saved_question import SavedQuestion
from saved_question_package_specs import SavedQuestionPackageSpecs
from saved_question_question import SavedQuestionQuestion
from saved_question_question_list import SavedQuestionQuestionList
from saved_question_list import SavedQuestionList
from select import Select
from select_list import SelectList
from sensor import Sensor
from sensor_reference import SensorReference
from sensor_reference_list import SensorReferenceList
from sensor_list import SensorList
from soap_error import SoapError
from solution import Solution
from solution_list import SolutionList
from plugin_sql import PluginSql
from package_file_status import PackageFileStatus
from string_hint_list import StringHintList
from cache_filter_list import CacheFilterList
from sensor_subcolumn import SensorSubcolumn
from sensor_subcolumn_list import SensorSubcolumnList
from system_setting import SystemSetting
from system_setting_list import SystemSettingList
from system_status_list import SystemStatusList
from upload_file import UploadFile
from upload_file_status import UploadFileStatus
from user import User
from user_group import UserGroup
from user_group_list import UserGroupList
from user_list import UserList
from version_aggregate import VersionAggregate
from version_aggregate_list import VersionAggregateList
from white_listed_url import WhiteListedUrl
from white_listed_url_list import WhiteListedUrlList


OBJECT_LIST_TYPES = {
	'action': Action,
	'action_group': ActionGroup,
	'action_groups': ActionGroupList,
	'action_stop': ActionStop,
	'action_stops': ActionStopList,
	'actions': ActionList,
	'aggregate': SystemStatusAggregate,
	'archived_question': ArchivedQuestion,
	'archived_questions': ArchivedQuestionList,
	'argument': PluginArgument,
	'arguments': PluginArgumentList,
	'audit_log': AuditLog,
	'audit_logs': AuditLogList,
	'cache_info': CacheInfo,
	'client_count': ClientCount,
	'client_status': ClientStatus,
	'columns': PluginSqlColumnList,
	'commands': PluginCommandList,
	'computer_group': ComputerGroup,
	'computer_groups': ComputerGroupList,
	'computer_spec': ComputerGroupSpec,
	'computer_specs': ComputerSpecList,
	'content_set': IdReference,
	'content_set_privilege': ContentSetPrivilege,
	'content_set_privileges': ContentSetPrivilegeList,
	'content_set_role': ContentSetRole,
	'content_set_role_membership': ContentSetRoleMembership,
	'content_set_role_memberships': ContentSetRoleMembershipList,
	'content_set_role_privilege': ContentSetRolePrivilegeOnRole,
	'content_set_role_privileges': ContentSetRolePrivilegeOnRoleList,
	'content_set_roles': ContentSetRoleList,
	'content_set_user_group_role_membership': ContentSetUserGroupRoleMembership,
	'content_set_user_group_role_memberships': ContentSetUserGroupRoleMembershipList,
	'content_sets': ContentSetList,
	'dashboard': Dashboard,
	'dashboard_group': DashboardGroup,
	'dashboard_list': DashboardList,
	'effective_content_set_privilege': EffectiveContentSetPrivilege,
	'effective_content_set_privileges': EffectiveContentSetPrivilegeRequest,
	'entries': AuditDataList,
	'entry': AuditData,
	'error': XmlError,
	'errors': ErrorList,
	'file': PackageFile,
	'file_parts': UploadFileList,
	'file_status': PackageFileStatusList,
	'file_template': PackageFileTemplate,
	'file_templates': PackageFileTemplateList,
	'filter': Filter,
	'filters': FilterList,
	'first_computer_id': ComputerIdList,
	'group': Group,
	'groups': GroupList,
	'hashed_string': HashedString,
	'hashed_strings': HashedStringList,
	'import_conflict_options': ImportConflictOptions,
	'info': QuestionListInfo,
	'item': MetadataItem,
	'ldap_sync_connector': LdapSyncConnector,
	'ldap_sync_connector_list': LdapSyncConnectorList,
	'metadata': MetadataList,
	'object_list': ObjectList,
	'options': Options,
	'owned_object_ids': UserOwnedObjectIds,
	'package_files': PackageFileList,
	'package_spec': PackageSpec,
	'package_specs': PackageSpecList,
	'parameter': Parameter,
	'parameter_values': ParameterValueList,
	'parameters': ParameterList,
	'parse_job': ParseJob,
	'parse_jobs': ParseJobList,
	'parse_result': ParseResult,
	'parse_result_group': ParseResultGroup,
	'parse_result_groups': ParseResultGroupList,
	'parse_results': ParseResultList,
	'permissions': PermissionList,
	'plugin': Plugin,
	'plugin_schedule': PluginSchedule,
	'plugin_schedules': PluginScheduleList,
	'plugins': PluginList,
	'policy': SavedActionPolicy,
	'queries': SensorQueryList,
	'query': SensorQuery,
	'question': Question,
	'questions': QuestionList,
	'result_row': PluginSqlResultList,
	'role': UserRole,
	'roles': UserRoleList,
	'row_ids': SavedActionRowIdList,
	'saved_action': SavedAction,
	'saved_action_approval': SavedActionApproval,
	'saved_action_approvals': SavedActionApprovalList,
	'saved_actions': SavedActionList,
	'saved_question': SavedQuestion,
	'saved_question_package_specs': SavedQuestionPackageSpecs,
	'saved_question_question': SavedQuestionQuestion,
	'saved_question_questions': SavedQuestionQuestionList,
	'saved_questions': SavedQuestionList,
	'select': Select,
	'selects': SelectList,
	'sensor': Sensor,
	'sensor_reference': SensorReference,
	'sensor_references': SensorReferenceList,
	'sensors': SensorList,
	'soap_error': SoapError,
	'solution': Solution,
	'solutions': SolutionList,
	'sql_response': PluginSql,
	'status': PackageFileStatus,
	'string_hints': StringHintList,
	'sub_filters': CacheFilterList,
	'subcolumn': SensorSubcolumn,
	'subcolumns': SensorSubcolumnList,
	'system_setting': SystemSetting,
	'system_settings': SystemSettingList,
	'system_status': SystemStatusList,
	'upload_file': UploadFile,
	'upload_file_status': UploadFileStatus,
	'user': User,
	'user_group': UserGroup,
	'user_groups': UserGroupList,
	'users': UserList,
	'version': VersionAggregate,
	'versions': VersionAggregateList,
	'white_listed_url': WhiteListedUrl,
	'white_listed_urls': WhiteListedUrlList,
}