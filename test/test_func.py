#!/usr/bin/env python -ttB
"""Functional tests for pytan.

These tests require a connection to a Tanium server in order to run.
The connection info is pulled from the SERVER_INFO dictionary in test/API_INFO.py.

These tests all use :mod:`ddt`, a package that provides for data driven tests via JSON files.
"""  # TODO(jeo): fix message to relate to new handler arg handling
from __future__ import print_function

import StringIO
import csv
import glob
import os
import pprint
import re
import sys
import tempfile
import unittest

THIS_PATH = os.path.abspath(sys.argv[0])
THIS_FILE = os.path.basename(THIS_PATH)
THIS_DIR = os.path.dirname(THIS_PATH)
PARENT_DIR = os.path.abspath(os.path.join(THIS_DIR, os.pardir))
PYTAN_LIB_DIR = os.path.join(PARENT_DIR, "lib")
TEST_LIB_DIR = os.path.join(THIS_DIR, "lib")
PATH_ADDS = [PYTAN_LIB_DIR, TEST_LIB_DIR]
[sys.path.insert(0, p) for p in PATH_ADDS if p not in sys.path]

try:
    import ddt
    import pytan
    import taniumpy
    import threaded_http
except Exception:
    raise

HANDLER_ARGS = {
    "username": "Administrator",
    "password": "Tanium2015!",
    "host": "172.16.29.130",
    "port": "443",
    "debugformat": False,
    "loglevel": 1,  # control level of logging for pytan
}
"""Arguments for creating pytan.Handler object."""
# TODO(jeo) CHANGE THIS TO ASK BEFORE RUNNING TESTS AND/OR USE ~/.pytan_config.json

TEST_ARGS = {
    "testlevel": 1,  # what level of spew.*() to log, see TEST_LEVELS to see what levels are
    "failfast": True,  # have unittests exit immediately on unexpected error
    "break": True,  # catch control-C to allow current test suite to finish (press 2x to force)
    "buffer": False,  # only show output from unittests
    "outdir": tempfile.gettempdir(),  # output directory for unittests
}
"""Arguments for running unittests."""

LOG_ARGS = {
    "level": logging.DEBUG,  # what level of logging to print out
    "format": (
        "[%(lineno)-5d - %(filename)20s:%(funcName)s()] %(asctime)s\n"
        "%(levelname)-8s %(name)s %(message)s"
    ),  # what format to use with logging
}

TEST_LEVELS = {
    "default": 0,  # default testlevel for anything that doesn't specify a level
    "run": 1,  # testlevel to log start/end messages
    "eval": 4,  # testlevel to log eval info
}
"""Levels that should be used by the various spew.*() methods."""

RUN_TMPL = """
*****************************************************************
START: {stime}
END: {etime}
HANDLER: {handler_obj}
PYTAN VERSION: {pver}
TANIUM VERSION: {tver}
""".format
"""Template used by tests to print start/end message."""

EVAL_TMPL = """EXPECTED {stxt}
against method: {mtxt}()
kwargs: {k}
ddt values: {d}
""".format
"""Template used by eval tests within unittests."""

FIX_TMPL = """FIXTURE: adding {} as {}""".format
"""Template used when adding fixtures."""

LOG = logging.getLogger(__name__)
logging.basicConfig(LOG_ARGS)


@ddt.ddt
class ApiTests(unittest.TestCase):
    """Functional tests for pytan against a Tanium Platform Servers SOAP API."""

    FIXTURES = {
        "handler_obj": None,  # instantiated pytan.Handler
        "tver": pytan.__version__,  # pytan version
        "sver": None,  # tanium platform version
        "stime": pytan.utils.seconds_from_now(),  # start time
        "etime": None,  # end time
        "wl_names": ['wl test1', 'wl test2', 'wl test3'],  # names of whitelisted_urls to create
    }
    """Fixtures to be used throughout unittests."""

    def chew_csv(self, c):
        """Turn string c from csv data into a list of lists."""
        i = StringIO.StringIO(c)
        r = csv.reader(i)
        l = list(r)
        return l

    def spew(self, msg, target="default", loglvl="DEBUG"):
        """Log msg if TEST_ARGS["testlevel"] >= TEST_LEVELS[target] to LOG.loglvl."""
        testlvl = self.get_fixture("targ", {}).get("testlevel", 0)
        tlvl = self.get_fixture("spew_lvls").get(target, 0)
        if testlvl >= tlvl:
            print(msg, file=out)

    def spew_run(self):
        """Use spew to print out a start/finish message at testlevel 1 and above."""
        spew(m=RUN_TMPL(**self.FIXTURES), target="run")

    def spew_eval(self, s, m, k, d):
        """Use spew to print out a templated message with method/kwargs/ddt values."""
        mre_search = ".*method (.*) of <.*"
        mre_replace = r"\1"
        margs = {}
        margs.update(**locals())
        margs.update(self.FIXTURES)
        margs['stxt'] = "SUCCESS" if s else "FAILURE"
        margs['mtxt'] = re.sub(mre_search, mre_replace, "{}".format(m))
        spew(m=EVAL_TMPL(**margs), target="eval")

    def get_fixture(self, k):
        """Get value of fixture k from self.FIXTURES."""
        return self.FIXTURES.get(k, "")

    def set_fixture(self, k, v, l=5):
        """Set fixture k to value v in self.FIXTURES."""
        spew(m=FIX_TMPL(k, v), target="eval")
        self.FIXTURES[k] = v

    def setUp(self, l=3):
        """Setup the class with a pytan Handler for use by all tests."""
        test_args = self.get_fixture("targ")
        if not ["out"]:
            TEST_ARGS["out"] = os.path.join(tempfile.gettempdir())

        if not get_fixture("handler"):
            handler = pytan.Handler(**SERVER_INFO)
            self.set_fixture("handler", handler)

        if not get_fixture("sv"):
            sv = self.handler.session.get_server_version()
            self.set_fixture("sv", sv)

        if not get_fixture("st"):
            st = pytan.utils.seconds_from_now()
            self.set_fixture("st", pytan.utils.seconds_from_now())

        if not get_fixture("base_type_objects"):
            # fetch BaseType objects for export tests
            kwargs = {
                'name': ["Computer Name", "IP Route Details", "IP Address", 'Folder Contents'],
                'objtype': 'sensor',
            }
            spew("FIXTURE: Getting sensor objects for export tests of BaseType: {}".format(kwargs), 2)
            base_type_objs = self.get_fixture("handler").get(**kwargs)
            self.set_fixture("base_type_objects", base_type_objs)

        if not get_fixture("wl_objects"):
            # create whitelisted_urls for getobject tests
            for wlu in self.wlus:
                spew("TESTSETUP: Creating whitelisted URLs for get object tests")
                try:
                    self.handler.create_whitelisted_url(url=wlu)
                except:
                    pass

        if not hasattr(self, 'result_set_objs'):
            # ask questions for export tests
            kwargs = {
                'qtype': 'manual',
                'sensors': [
                    "Computer Name",
                    "IP Route Details",
                    "IP Address",
                    'Folder Contents{folderPath=C:\\Program Files}',
                ],
            }
            spew("TESTSETUP: Asking a question for export tests of ResultSet")
            self.result_set_objs = self.handler.ask(**kwargs)

        spew('\n' + str(self.handler))

    # TODO(jeo): use new stuff
    @classmethod
    def tearDownClass(cls): # noqa
        m = "{}\n{}: PyTan v'{}' against Tanium v'{}' -- Tests Finished".format
        cls.end_time = pytan.utils.seconds_from_now()
        spew(m(HEADER, cls.end_time, cls.pytan_version, cls.server_version), 2)

    def setup_test(self):
        """Used by each test to get access to the handler from self.handler."""
        spew("")
        self.assertTrue(self.base_type_objs)
        self.assertIsInstance(self.base_type_objs, taniumpy.BaseType)
        self.assertEquals(len(self.base_type_objs), 4)
        self.assertTrue(self.result_set_objs)
        self.assertIsInstance(self.result_set_objs['question_object'], taniumpy.Question)
        self.assertIsInstance(self.result_set_objs['question_results'], taniumpy.ResultSet)
        self.assertGreaterEqual(len(self.result_set_objs['question_results'].rows), 1)
        self.assertGreaterEqual(len(self.result_set_objs['question_results'].columns), 1)
        return self.handler

    @ddt.file_data('ddt/ddt_valid_export_resultset.json')
    def test_valid_export_resultset(self, value):
        """Load all tests from 'ddt/ddt_valid_export_resultset.json'."""
        handler = self.setup_test()
        method_name = "export_obj"
        method = getattr(handler, method_name)
        kwargs = {'obj': self.result_set_objs['question_results']}
        kwargs.update(value['args'])
        tests = value['tests']

        spew_test(s=True, m=method, k=kwargs, d=value)
        export_str = method(**kwargs)

        self.assertTrue(export_str)
        self.assertIsInstance(export_str, (str, unicode))

        export_str_list = chew_csv(export_str)
        for t in tests:
            spew(m="+++ EVAL TEST: {}".format(t), l=5)
            try:
                self.assertTrue(eval(t))
            except Exception:
                spew("!!! EVAL TEST FAILED: '{}' - Locals:\n{}".format(t, pprint.pprint(locals())))
                raise

    @ddt.file_data('ddt/ddt_valid_export_basetype.json')
    def test_valid_export_basetype(self, value):
        """Load all tests from 'ddt/ddt_valid_export_basetype.json'."""
        handler = self.setup_test()
        method_name = "export_obj"
        method = getattr(handler, method_name)
        kwargs = {'obj': self.base_type_objs}
        kwargs.update(value['args'])
        tests = value['tests']

        spew_test(s=True, m=method, k=kwargs, d=value)
        export_str = method(**kwargs)

        self.assertTrue(export_str)
        self.assertIsInstance(export_str, (str, unicode))

        for t in tests:
            spew(m="+++ EVAL TEST: {}".format(t), l=5)
            try:
                self.assertTrue(eval(t))
            except Exception:
                spew("!!! EVAL TEST FAILED: '{}' - Locals:\n{}".format(t, pprint.pprint(locals())))
                raise

    @ddt.file_data('ddt/ddt_valid_deploy_action.json')
    def test_valid_deploy_action(self, value):
        """Load all tests from 'ddt/ddt_valid_deploy_action.json'."""
        handler = self.setup_test()
        method_name = value['method']
        method = getattr(handler, method_name)
        kwargs = value['args']
        get_results = kwargs.get('get_results', True)

        spew_test(s=True, m=method, k=kwargs, d=value)

        ret = method(**kwargs)
        self.assertIsInstance(ret['action_object'], taniumpy.Action)
        self.assertIsInstance(ret['saved_action_object'], (taniumpy.SavedAction, type(None)))
        self.assertIsInstance(ret['package_object'], taniumpy.PackageSpec)
        self.assertIsInstance(ret['group_object'], (taniumpy.Group, type(None)))
        self.assertIsInstance(ret['action_info'], taniumpy.object_types.result_info.ResultInfo)
        self.assertIsInstance(ret['poller_object'], pytan.pollers.ActionPoller)

        if get_results:
            self.assertIsInstance(ret['action_results'], taniumpy.object_types.result_set.ResultSet)
            self.assertGreaterEqual(len(ret['action_results'].rows), 1)
            self.assertGreaterEqual(len(ret['action_results'].columns), 1)
            self.assertTrue(ret['action_result_map'])
            self.assertIsNotNone(ret['poller_success'])
            for ft in pytan.constants.EXPORT_MAPS['ResultSet'].keys():
                report_file, result = handler.export_to_report_file(
                    obj=ret['action_results'],
                    export_format=ft,
                    report_dir=TEST_OUT,
                    prefix=sys._getframe().f_code.co_name + '_',
                )
                self.assertTrue(report_file)
                self.assertTrue(result)
                self.assertTrue(os.path.isfile(report_file))
                self.assertGreaterEqual(len(result), 10)

    @ddt.file_data('ddt/ddt_valid_create_object.json')
    def test_valid_create_object(self, value):
        """Load all tests from 'ddt/ddt_valid_create_object.json'."""
        handler = self.setup_test()
        method_name = value['method']
        method = getattr(handler, method_name)
        kwargs = value['args']
        t_obj = eval(value['taniumpyobj'])
        delete_args = {str(k): str(v) for k, v in value['delete'].iteritems()}

        spew_test(s=True, m=method, k=kwargs, d=value)

        try:
            old_obj = handler.get(**delete_args)[0]
            spew("Found old object {} using {}, deleting".format(old_obj, delete_args))
            handler.delete(**delete_args)
        except:
            spew("Did not find old object using {}, not deleting".format(delete_args))

        ret = method(**kwargs)
        self.assertIsInstance(ret, t_obj)

        delete_obj = handler.delete(**delete_args)
        self.assertEquals(len(delete_obj), 1)
        for x in delete_obj:
            self.assertIsInstance(x, t_obj)

    @ddt.file_data('ddt/ddt_valid_create_object_from_json.json')
    def test_valid_create_object_from_json(self, value):
        """Load all tests from 'ddt/ddt_valid_create_object_from_json.json'."""
        handler = self.setup_test()
        method_name = "create_from_json"
        method = getattr(handler, method_name)

        orig_objs = handler.get(**value['get'])
        self.assertIsInstance(orig_objs, eval(value['listobj']))
        self.assertEquals(len(orig_objs), 1)
        self.assertIsInstance(orig_objs[0], eval(value['singleobj']))
        orig_obj = orig_objs[0]

        if value['transform_attr']:
            transform_val = getattr(orig_obj, value['transform_attr'])
            transform_val += value['transform_value']
            setattr(orig_obj, value['transform_attr'], transform_val)
            if value['delete_before']:
                del_kwargs = {}
                del_kwargs['objtype'] = value['objtype']
                del_kwargs[value['transform_attr']] = transform_val
                try:
                    old_sensor = handler.get(**del_kwargs)[0]
                    spew("Found old object {} using {}, deleting".format(old_sensor, del_kwargs))
                    handler.delete(**del_kwargs)
                except:
                    spew("Did not find old object using {}, not deleting".format(del_kwargs))

        json_file, results = handler.export_to_report_file(
            obj=orig_obj,
            export_format='json',
            report_dir=TEST_OUT,
            prefix=sys._getframe().f_code.co_name + '_',
        )

        kwargs = {'objtype': value['objtype'], 'json_file': json_file}
        spew_test(s=True, m=method, k=kwargs, d=value)

        new_obj = method(**kwargs)
        self.assertIsInstance(new_obj, eval(value['listobj']))
        self.assertEquals(len(new_obj), 1)
        self.assertIsInstance(new_obj[0], eval(value['singleobj']))

    @ddt.file_data('ddt/ddt_valid_questions.json')
    def test_valid_question(self, value):
        """Load all tests from 'ddt/ddt_valid_questions.json'."""
        handler = self.setup_test()
        method_name = value['method']
        method = getattr(handler, method_name)
        kwargs = value['args']
        get_results = kwargs.get('get_results', True)

        spew_test(s=True, m=method, k=kwargs, d=value)
        ret = method(**kwargs)

        self.assertIsInstance(ret['question_object'], taniumpy.Question)
        self.assertIsInstance(ret['poller_object'], pytan.pollers.QuestionPoller)

        parsed_q = kwargs['qtype'] == 'parsed'
        if parsed_q:
            self.assertIsInstance(ret['parse_results'], taniumpy.ParseResultGroupList)

        if get_results:
            self.assertIsNotNone(ret['poller_success'])
            self.assertIsInstance(ret['question_results'], taniumpy.ResultSet)
            self.assertGreaterEqual(len(ret['question_results'].rows), 1)
            self.assertGreaterEqual(len(ret['question_results'].columns), 1)
            for ft in pytan.constants.EXPORT_MAPS['ResultSet'].keys():
                report_file, result = handler.export_to_report_file(
                    obj=ret['question_results'],
                    export_format=ft,
                    report_dir=TEST_OUT,
                    prefix=sys._getframe().f_code.co_name + '_',
                )
                self.assertTrue(report_file)
                self.assertTrue(result)
                self.assertTrue(os.path.isfile(report_file))
                self.assertGreaterEqual(len(result), 10)

    @ddt.file_data('ddt/ddt_valid_saved_questions.json')
    def test_valid_saved_question(self, value):
        """Load all tests from 'ddt/ddt_valid_saved_questions.json'."""
        handler = self.setup_test()
        method_name = value['method']
        method = getattr(handler, method_name)
        kwargs = value['args']

        spew_test(s=True, m=method, k=kwargs, d=value)
        ret = method(**kwargs)

        self.assertIsInstance(ret['saved_question_object'], taniumpy.SavedQuestion)
        self.assertIsInstance(ret['question_object'], taniumpy.Question)
        self.assertIsInstance(ret['poller_object'], (pytan.pollers.QuestionPoller, type(None)))
        self.assertIsInstance(ret['poller_success'], (type(None), type(True)))
        self.assertIsInstance(ret['question_results'], taniumpy.ResultSet)
        self.assertGreaterEqual(len(ret['question_results'].rows), 1)
        self.assertGreaterEqual(len(ret['question_results'].columns), 1)
        for ft in pytan.constants.EXPORT_MAPS['ResultSet'].keys():
            report_file, result = handler.export_to_report_file(
                obj=ret['question_results'],
                export_format=ft,
                report_dir=TEST_OUT,
                prefix=sys._getframe().f_code.co_name + '_',
            )
            self.assertTrue(report_file)
            self.assertTrue(result)
            self.assertTrue(os.path.isfile(report_file))
            self.assertGreaterEqual(len(result), 10)

    @ddt.file_data('ddt/ddt_valid_get_object.json')
    def test_valid_get_object(self, value):
        """Load all tests from 'ddt/ddt_valid_get_object.json'."""
        handler = self.setup_test()
        method_name = value['method']
        method = getattr(handler, method_name)
        kwargs = value['args']
        tests = value['tests']

        spew_test(s=True, m=method, k=kwargs, d=value)
        response = method(**kwargs)

        self.assertTrue(response)
        self.assertIsInstance(response, taniumpy.BaseType)

        for t in tests:
            spew(m="+++ EVAL TEST: {}".format(t), l=5)
            try:
                self.assertTrue(eval(t))
            except Exception:
                spew("!!! EVAL TEST FAILED: '{}' - Locals:\n{}".format(t, pprint.pprint(locals())))
                raise

        for ft in pytan.constants.EXPORT_MAPS['BaseType'].keys():
            report_file, result = handler.export_to_report_file(
                obj=response, export_format=ft, report_dir=TEST_OUT,
                prefix=sys._getframe().f_code.co_name + '_',
            )
            self.assertTrue(report_file)
            self.assertTrue(result)
            self.assertTrue(os.path.isfile(report_file))
            self.assertGreaterEqual(len(result), 10)

    @ddt.file_data('ddt/ddt_invalid_export_basetype.json')
    def test_invalid_export_basetype(self, value):
        """Load all tests from 'ddt/ddt_invalid_export_basetype.json'."""
        handler = self.setup_test()
        method_name = "export_obj"
        method = getattr(handler, method_name)
        kwargs = {'obj': self.base_type_objs}
        kwargs.update(value['args'])
        exc = eval(value['exception'])
        e = value['error_str']

        spew_test(s=False, m=method, k=kwargs, d=value)
        with self.assertRaisesRegexp(exc, e):
            method(**kwargs)

    @ddt.file_data('ddt/ddt_invalid_create_object_from_json.json')
    def test_invalid_create_object_from_json(self, value):
        """Load all tests from 'ddt/ddt_invalid_create_object_from_json.json'."""
        handler = self.setup_test()
        method_name = "create_from_json"
        method = getattr(handler, method_name)
        exc = eval(value['exception'])
        e = value['error_str']

        orig_objs = handler.get(**value['get'])

        json_file, results = handler.export_to_report_file(
            obj=orig_objs,
            export_format='json',
            report_dir=TEST_OUT,
            prefix=sys._getframe().f_code.co_name + '_',
        )

        kwargs = {'objtype': value['objtype'], 'json_file': json_file}

        spew_test(s=False, m=method, k=kwargs, d=value)
        with self.assertRaisesRegexp(exc, e):
            method(**kwargs)

    @ddt.file_data('ddt/ddt_invalid_questions.json')
    def test_invalid_question(self, value):
        """Load all tests from 'ddt/ddt_invalid_questions.json'."""
        handler = self.setup_test()
        method_name = value['method']
        method = getattr(handler, method_name)
        kwargs = value['args']
        exc = eval(value['exception'])
        e = value['error_str']

        spew_test(s=False, m=method, k=kwargs, d=value)
        with self.assertRaisesRegexp(exc, e):
            method(**kwargs)

    @ddt.file_data('ddt/ddt_invalid_get_object.json')
    def test_invalid_get_object(self, value):
        """Load all tests from 'ddt/ddt_invalid_get_object.json'."""
        handler = self.setup_test()
        method_name = value['method']
        method = getattr(handler, method_name)
        kwargs = value['args']
        exc = eval(value['exception'])
        e = value['error_str']

        spew_test(s=False, m=method, k=kwargs, d=value)
        with self.assertRaisesRegexp(exc, e):
            method(**kwargs)

    @ddt.file_data('ddt/ddt_invalid_create_object.json')
    def test_invalid_create_object(self, value):
        """Load all tests from 'ddt/ddt_invalid_create_object.json'."""
        handler = self.setup_test()
        method_name = value['method']
        method = getattr(handler, method_name)
        kwargs = value['args']
        exc = eval(value['exception'])
        e = value['error_str']

        spew_test(s=False, m=method, k=kwargs, d=value)
        with self.assertRaisesRegexp(exc, e):
            method(**kwargs)

    @ddt.file_data('ddt/ddt_invalid_deploy_action.json')
    def test_invalid_deploy_action(self, value):
        """Load all tests from 'ddt/ddt_invalid_deploy_action.json'."""
        handler = self.setup_test()
        method_name = value['method']
        method = getattr(handler, method_name)
        kwargs = value['args']
        exc = eval(value['exception'])
        e = value['error_str']
        kwargs["report_dir"] = kwargs.get('report_dir', tempfile.gettempdir())

        spew_test(s=False, m=method, k=kwargs, d=value)
        with self.assertRaisesRegexp(exc, e):
            method(**kwargs)

    @ddt.file_data('ddt/ddt_invalid_export_resultset.json')
    def test_invalid_export_resultset(self, value):
        """Load all tests from 'ddt/ddt_invalid_export_resultset.json'."""
        handler = self.setup_test()
        method_name = "export_obj"
        method = getattr(handler, method_name)
        kwargs = {'obj': self.result_set_objs['question_results']}
        kwargs.update(value['args'])
        exc = eval(value['exception'])
        e = value['error_str']

        spew_test(s=False, m=method, k=kwargs, d=value)
        with self.assertRaisesRegexp(exc, e):
            method(**kwargs)


if __name__ == "__main__":
    if not os.path.isdir(TEST_OUT):
        os.mkdir(TEST_OUT)

    test_files = glob.glob(TEST_OUT + '/*.*')
    if test_files:
        spew("Cleaning up %s old test files" % len(test_files))
        [os.unlink(x) for x in test_files]

    unittest.main(
        verbosity=SERVER_INFO["testlevel"],
        failfast=SERVER_INFO["FAILFAST"],
        catchbreak=SERVER_INFO["CATCHBREAK"],
        buffer=SERVER_INFO["BUFFER"],
    )
