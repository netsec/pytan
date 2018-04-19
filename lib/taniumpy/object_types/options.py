
# Copyright (c) 2015 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class Options(BaseType):

    _soap_tag = 'options'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties={'export_flag': int,
                        'export_format': int,
                        'export_leading_text': str,
                        'export_trailing_text': str,
                        'export_hide_csv_header_flag': int,
                        'flags': int,
                        'hide_errors_flag': int,
                        'include_answer_times_flag': int,
                        'row_counts_only_flag': int,
                        'aggregate_over_time_flag': int,
                        'no_result_row_collation_flag': int,
                        'most_recent_flag': int,
                        'include_hashes_flag': int,
                        'hide_no_results_flag': int,
                        'use_user_context_flag': int,
                        'script_data': str,
                        'return_lists_flag': int,
                        'return_cdata_flag': int,
                        'pct_done_limit': int,
                        'context_id': int,
                        'sample_frequency': int,
                        'sample_start': int,
                        'sample_count': int,
                        'audit_history_size': int,
                        'suppress_scripts': int,
                        'suppress_object_list': int,
                        'row_start': int,
                        'row_count': int,
                        'sort_order': str,
                        'filter_string': str,
                        'filter_not_flag': int,
                        'recent_result_buckets': str,
                        'cache_id': int,
                        'cache_expiration': int,
                        'cache_sort_fields': str,
                        'include_user_details': int,
                        'include_user_owned_object_ids_flag': int,
                        'include_hidden_flag': int,
                        'use_error_objects': int,
                        'use_json': int,
                        'json_pretty_print': int,
                        'live_snapshot_report_count_threshold': int,
                        'live_snapshot_expiration_seconds': int,
                        'live_snapshot_always_use_seconds': int,
                        'live_snapshot_invalidate_report_count_percentage': int,
                        'disable_live_snapshots': int,
                        'allow_cdata_base64_encode_flag': int,
                        'cdata_base64_encoded': int,
                        'import_analyze_conflicts_only': int,
                        'export_dont_include_related': int,
                        'export_omit_soap_envelope': int,
                        'import_existing_ignore_content_set': int,
                        'saved_question_qids_reissue_flag': int,
                        'saved_question_qids_allow_multiple_flag': int,
                        'saved_question_qids_include_expired_flag': int,
                        'saved_question_qids_ignore_mr_group_flag': int},
            complex_properties={'cache_filters': CacheFilterList,
                        'import_conflict_options': ImportConflictOptions},
            list_properties={},
        )
        self.export_flag = None
        self.export_format = None
        self.export_leading_text = None
        self.export_trailing_text = None
        self.export_hide_csv_header_flag = None
        self.flags = None
        self.hide_errors_flag = None
        self.include_answer_times_flag = None
        self.row_counts_only_flag = None
        self.aggregate_over_time_flag = None
        self.no_result_row_collation_flag = None
        self.most_recent_flag = None
        self.include_hashes_flag = None
        self.hide_no_results_flag = None
        self.use_user_context_flag = None
        self.script_data = None
        self.return_lists_flag = None
        self.return_cdata_flag = None
        self.pct_done_limit = None
        self.context_id = None
        self.sample_frequency = None
        self.sample_start = None
        self.sample_count = None
        self.audit_history_size = None
        self.suppress_scripts = None
        self.suppress_object_list = None
        self.row_start = None
        self.row_count = None
        self.sort_order = None
        self.filter_string = None
        self.filter_not_flag = None
        self.recent_result_buckets = None
        self.cache_id = None
        self.cache_expiration = None
        self.cache_sort_fields = None
        self.include_user_details = None
        self.include_user_owned_object_ids_flag = None
        self.include_hidden_flag = None
        self.use_error_objects = None
        self.use_json = None
        self.json_pretty_print = None
        self.live_snapshot_report_count_threshold = None
        self.live_snapshot_expiration_seconds = None
        self.live_snapshot_always_use_seconds = None
        self.live_snapshot_invalidate_report_count_percentage = None
        self.disable_live_snapshots = None
        self.allow_cdata_base64_encode_flag = None
        self.cdata_base64_encoded = None
        self.import_analyze_conflicts_only = None
        self.export_dont_include_related = None
        self.export_omit_soap_envelope = None
        self.import_existing_ignore_content_set = None
        self.saved_question_qids_reissue_flag = None
        self.saved_question_qids_allow_multiple_flag = None
        self.saved_question_qids_include_expired_flag = None
        self.saved_question_qids_ignore_mr_group_flag = None
        self.cache_filters = None
        self.import_conflict_options = None
        

from cache_filter_list import CacheFilterList
from import_conflict_options import ImportConflictOptions

