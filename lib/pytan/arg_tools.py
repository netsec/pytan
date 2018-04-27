"""Argument processing and validation tools."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import pprint
import sys
import traceback

IS_PY2 = sys.version_info[0] == 2
"""Coarse Python version differential."""

if IS_PY2:
    STR = unicode  # noqa
    STR_TYPES = (STR, basestring)  # noqa
else:
    STR = str
    STR_TYPES = (STR,)

INT_TYPES = (int,)
LIST_TYPES = (list, tuple)
BOOL_TYPES = (bool,)
DICT_TYPES = (dict,)

# TODO(jeo):
"""
- finish list
 - need list of X (dict, int, str, bool?)
- add list tests
- Doc all method args
- add valid_values to everything
- rename to arg_tools/ Val.*=> Arg.*
- add parent arg mapper?
- add pointers to arg_tools obj in each class? ala
    ARGTOOL = arg_tools.ArgumentTool()
    ARGSTR = ARGTOOL.argstr
make each val type subclass ArgumentTool?
- list method can check for empty values?
- add taniumpy type checking, but do it thru passthru of init, not locally?
"""
# TODO(jeo): argtool.arglist should have subtype checking builtin!


class ArgumentError(Exception):
    """General Exception."""

    def __init__(self, msg, **kwargs):
        """Constructor."""
        kwtxt = "Exception arguments:\n{}".format(pprint.pformat(kwargs))
        kwargs["msg"] = msg
        kwargs["key"] = "No key supplied!" if "key" not in kwargs else kwargs["key"]
        kwargs["value"] = "No value supplied!" if "value" not in kwargs else kwargs["value"]
        kwargs["argtype"] = type(kwargs["value"])

        merr = "Error with argument name {key!r} value {value!r} of type: {argtype}:\nError message: {msg}"
        merr = merr.format(**kwargs)
        msgs = []
        msgs.append(merr)
        msgs.append(kwtxt)

        if "exc" in kwargs and IS_PY2:
            exc_tb = ''.join(traceback.format_exception(*kwargs["exc"]))
            exc_msg = "Original Traceback:\n{exc_tb}".format(exc_tb=exc_tb)
            msgs.append(exc_msg)

        m = "\n".join(msgs)
        super(ArgumentError, self).__init__(m)


class MissingError(ArgumentError):
    """Required argument missing."""


class InvalidTypeError(ArgumentError):
    """Argument value is invalid type."""


class EmptyError(ArgumentError):
    """Argument value is empty."""


class MinMaxError(ArgumentError):
    """Argument value not <= max or >= min."""


class ArgumentTool(object):
    """Validator class."""

    def argstr(self, key, **targs):
        """Validate ``value`` or ``kwargs[key]`` is defined and is an instance of STR_TYPES.

        Parameters
        ----------
        key : str
            * key within ``kwargs`` to get ``value`` from, or name of variable ``value`` came from
        """
        targs["key"] = key
        targs["argtypes"] = targs.get("argtypes", STR_TYPES)
        targs = self.get_value(**targs)
        targs = self.val_type(**targs)
        targs = self.val_empty_ok(**targs)
        return targs["value"]

    def argint(self, key, **targs):
        """Validate ``value`` or ``kwargs[key]`` is defined and an instance of INT_TYPES.

        Parameters
        ----------
        key : str
            * key within ``kwargs`` to get ``value`` from, or name of variable ``value`` came from
        """
        targs["key"] = key
        targs["argtypes"] = targs.get("argtypes", INT_TYPES)
        targs["trytype"] = targs.get("trytype", int)
        targs = self.get_value(**targs)
        targs = self.val_type(**targs)
        targs = self.val_minmax(**targs)
        return targs["value"]

    def argbool(self, key, **targs):
        """Validate ``value`` or ``kwargs[key]`` is defined and an instance of BOOL_TYPES.

        Parameters
        ----------
        key : str
            * key within ``kwargs`` to get ``value`` from, or name of variable ``value`` came from
        """
        targs["key"] = key
        targs["argtypes"] = targs.get("argtypes", BOOL_TYPES)
        targs = self.get_value(**targs)
        targs = self.val_type(**targs)
        return targs["value"]

    def argdict(self, key, **targs):
        """Validate ``value`` or ``kwargs[key]`` is defined and an instance of DICT_TYPES.

        Parameters
        ----------
        key : str
            * key within ``kwargs`` to get ``value`` from, or name of variable ``value`` came from
        """
        targs["key"] = key
        targs["argtypes"] = targs.get("argtypes", DICT_TYPES)
        targs = self.get_value(**targs)
        targs = self.val_type(**targs)
        targs = self.val_empty_ok(**targs)
        return targs["value"]

    def arglist(self, key, **targs):
        """Validate ``value`` or ``kwargs[key]`` is defined and an instance of LIST_TYPES.

        Parameters
        ----------
        key : str
            * key within ``kwargs`` to get ``value`` from, or name of variable ``value`` came from
        """
        targs["key"] = key
        targs["argtypes"] = targs.get("argtypes", LIST_TYPES)
        targs = self.get_value(**targs)
        targs = self.val_type(**targs)
        targs = self.val_empty_ok(**targs)
        return targs["value"]

    def val_type(self, **targs):
        """Validate type of ``value`` is one of ``argtypes``.

        Parameters
        ----------
        argtypes : tuple of types, optional, no default
            * tuple of valid types that ``value`` should be an instance of
        trytype : type, optional, no default
            * try to force ``value`` to this type
        """
        # if ``argtypes`` is not in targs and ``argtypes`` is None, don't do any type checking
        if "argtypes" not in targs and targs.get("argtypes", None) is None:
            return targs

        # if ``value`` isn't an instance of ``argtypes``
        if not isinstance(targs["value"], targs["argtypes"]):
            # if ``trytype`` supplied, try to force ``value`` to type ``trytype``
            if "trytype" in targs:
                try:
                    targs["value"] = targs["trytype"](targs["value"])
                # throw error if trytype failed
                except Exception:
                    targs["exc"] = sys.exc_info()
                    targs["msg"] = "Invalid type supplied, must be one of types: {argtypes}".format(**targs)
                    raise InvalidTypeError(**targs)
            else:
                targs["msg"] = "Invalid type supplied, must be one of types: {argtypes}".format(**targs)
                raise InvalidTypeError(**targs)
        return targs

    def val_empty_ok(self, **targs):
        """Validate if ``value`` is allowed to be empty.

        Parameters
        ----------
        emptyok : bool, optional, no default
            * True - do not error if ``value`` is empty
            * False - error if ``value`` is empty
        """
        if "emptyok" in targs and not targs["emptyok"] and not targs["value"]:
            targs["msg"] = "Empty value supplied and emptyok={emptyok}".format(**targs)
            raise EmptyError(**targs)
        return targs

    def val_minmax(self, **targs):
        """Validate if ``value`` is >= ``valmin`` or <= valmax, if supplied.

        Parameters
        ----------
        valmin : int, optional, no default
            * if supplied, error if ``value`` is not >= ``valmin``
        valmax : int, optional, no default
            * if supplied, error if ``value`` is <= ``valmax``
        """
        if "valmin" in targs:
            if not targs["value"] >= targs["valmin"]:
                targs["msg"] = "{value} is not greater than or equal to {valmin}".format(**targs)
                raise MinMaxError(**targs)
        if "valmax" in targs:
            if not targs["value"] <= targs["valmax"]:
                targs["msg"] = "{value} is not less than or equal to {valmax}".format(**targs)
                raise MinMaxError(**targs)
        return targs

    def get_value(self, **targs):
        """Derive ``value`` from targs.

        If ``value`` not provided, check for ``kwargs[key]`` or ``default`` and add to targs.

        Parameters
        ----------
        kwargs : dict, optional, no default
            * a dict of arguments supplied to the caller to get ``key`` from
        value : str, optional, no default
            * manually provide the ``value`` of ``key`` instead of getting ``value`` from ``kwargs[key]``
        req : bool, optional, no default
            * True - error if ``value`` not supplied and ``key`` is not in ``kwargs``
            * False - if ``default`` provided, use ``default`` as ``value``
              IF ``key`` is not in ``kwargs`` and ``value`` is not supplied.
              IF ``default`` not provided and no ``value`` found, error
        default : obj, optional, no default
            * default ``value`` to use if ``req`` is supplied and is False, and
              ``key`` is not in ``kwargs``, and ``value`` not supplied.
        """
        # if ``value`` already passed in, just use that
        if "value" in targs:
            return targs

        # if ``kwargs`` supplied and is not a dict, raise error
        if "kwargs" in targs and not isinstance(targs["kwargs"], dict):
            targs["key"] = "kwargs"
            targs["value"] = targs["kwargs"]
            targs["argtypes"] = DICT_TYPES
            targs["msg"] = "Invalid type supplied, must be of type: {argtypes}".format(**targs)
            raise ArgumentError(**targs)

        # if ``kwargs`` supplied and ``key`` is in ``kwargs``, use that as ``value``
        if "kwargs" in targs and targs["key"] in targs["kwargs"]:
            key = targs["key"]
            targs["value"] = targs["kwargs"][key]
            return targs

        # if ``req`` supplied and ``req``=True, raise error
        if "req" in targs and targs["req"]:
            targs["msg"] = "Required but was not supplied!"
            raise MissingError(**targs)

        # if ``default`` not supplied, raise error
        if "default" not in targs:
            targs["msg"] = "Not supplied and no default!"
            raise MissingError(**targs)

        # use ``default`` as ``value``
        targs["value"] = targs["default"]

        # delete ``argtypes`` to skip type check against ``default``
        if "argtypes" in targs:
            del(targs["argtypes"])
        return targs


if __name__ == "__main__":  # noqa
    import unittest

    # add test that value gets used instead of kwargs[key]
    class TestStrArgs(unittest.TestCase):
        """Test ArgumentTool.argstr method."""

        @classmethod
        def setUpClass(cls):  # noqa
            cls.ARG_TOOL = ArgumentTool()
            cls.method = cls.ARG_TOOL.argstr
            cls.itypes = STR_TYPES
            print("Testing ArgumentTool().argstr()\n_______________________________")

        def test_exists(self):
            """Key "foo" exists with value "BAR", returns "BAR"."""
            kwargs = {"foo": "BAR"}
            value = self.method(key="foo", kwargs=kwargs)
            self.assertIsInstance(value, self.itypes)
            self.assertEqual(value, "BAR")

        @unittest.skipIf(not IS_PY2, "only valid for python2")
        def test_exists_str(self):
            """Key "foo" exists with value str("BAR"), returns str("BAR")."""
            kwargs = {"foo": str("BAR")}
            value = self.method(key="foo", kwargs=kwargs)
            self.assertIsInstance(value, self.itypes)
            self.assertEqual(value, str("BAR"))

        def test_missing_default(self):
            """Key "foo" missing, default = "", returns ""."""
            kwargs = {}
            value = self.method(key="foo", kwargs=kwargs, default="")
            self.assertIsInstance(value, self.itypes)
            self.assertEqual(value, "")

        def test_nokwargs_kv(self):
            """Supply no kwargs, a manual key "foo", value "BAR", returns "BAR"."""
            value = self.method(key="foo", value="BAR")
            self.assertIsInstance(value, self.itypes)
            self.assertEqual(value, "BAR")

        def test_exists_req(self):
            """Key "foo" is required, key exists with value "BAR", returns "BAR"."""
            kwargs = {"foo": "BAR"}
            value = self.method(key="foo", kwargs=kwargs, req=True)
            self.assertIsInstance(value, self.itypes)
            self.assertEqual(value, "BAR")

        def test_exists_badtype(self):
            """Key "foo" exists with value 123, throws InvalidTypeError due to invalid str."""
            kwargs = {"foo": 123}
            with self.assertRaises(InvalidTypeError):
                self.method(key="foo", kwargs=kwargs)

        def test_empty(self):
            """Key "foo" exists with value "", throws EmptyError due to empty value."""
            kwargs = {"foo": ""}
            with self.assertRaises(EmptyError):
                self.method(key="foo", kwargs=kwargs, emptyok=False)

        def test_missing(self):
            """Key "foo" missing, no default, throws MissingError due to missing key."""
            kwargs = {}
            with self.assertRaises(MissingError):
                self.method(key="foo", kwargs=kwargs)

        def test_missing_req(self):
            """Key "foo" missing, default of "", is required, throws MissingError due to missing key."""
            kwargs = {}
            with self.assertRaises(MissingError):
                self.method(key="foo", kwargs=kwargs, default="", req=True)

        def test_nokwargs_nov(self):
            """Supply no kwargs, no v, throws MissingError due to missing value."""
            with self.assertRaises(MissingError):
                self.method(key="foo")

        def test_badkwargs(self):
            """Supply kwargs as non dict, throws ArgumentError due to invalid kwargs."""
            kwargs = []
            with self.assertRaises(ArgumentError):
                self.method(key="foo", kwargs=kwargs)

    class TestIntArgs(unittest.TestCase):
        """Test Val.argint method."""

        @classmethod
        def setUpClass(cls):  # noqa
            cls.ARG_TOOL = ArgumentTool()
            cls.method = cls.ARG_TOOL.argint
            cls.itypes = INT_TYPES
            print("Testing ArgumentTool().argint()\n_______________________________")

        def test_exists(self):
            """Key "foo" exists with value 123, returns 123."""
            kwargs = {"foo": 123}
            value = self.method(key="foo", kwargs=kwargs)
            self.assertIsInstance(value, self.itypes)
            self.assertEqual(value, 123)

        def test_missing_default(self):
            """Key "foo" missing, default = 0, returns 0."""
            kwargs = {}
            value = self.method(key="foo", kwargs=kwargs, default=0)
            self.assertIsInstance(value, self.itypes)
            self.assertEqual(value, 0)

        def test_exists_req(self):
            """Key "foo" exists with value 123 is required, returns 123."""
            kwargs = {"foo": 123}
            value = self.method(key="foo", kwargs=kwargs, req=True)
            self.assertIsInstance(value, self.itypes)
            self.assertEqual(value, 123)

        def test_exists_str(self):
            """Key "foo" exists with value "123", returns 123."""
            kwargs = {"foo": "123"}
            value = self.method(key="foo", kwargs=kwargs, req=True)
            self.assertIsInstance(value, self.itypes)
            self.assertEqual(value, 123)

        def test_exists_min(self):
            """Key "foo" exists with value 10, meets valmin 5, returns 10."""
            kwargs = {"foo": 10}
            value = self.method(key="foo", kwargs=kwargs, valmin=5)
            self.assertIsInstance(value, self.itypes)
            self.assertEqual(value, 10)

        def test_exists_max(self):
            """Key "foo" exists with value 10, meets valmax 15, returns 10."""
            kwargs = {"foo": 10}
            value = self.method(key="foo", kwargs=kwargs, valmax=15)
            self.assertIsInstance(value, self.itypes)
            self.assertEqual(value, 10)

        def test_exists_minmax(self):
            """Key "foo" exists with value 10, meets valmin 10, valmax  10, returns 10."""
            kwargs = {"foo": 10}
            value = self.method(key="foo", kwargs=kwargs, valmin=10, valmax=10)
            self.assertIsInstance(value, self.itypes)
            self.assertEqual(value, 10)

        def test_nokwargs_kv(self):
            """Supply no kwargs, key "foo", a manual value 123. Returns 123."""
            value = self.method(key="foo", value=123)
            self.assertIsInstance(value, self.itypes)
            self.assertEqual(value, 123)

        def test_exists_badmin(self):
            """Key "foo" exists with value 10, valmin 15, throws MinMaxError due to 15 >= 10."""
            kwargs = {"foo": 10}
            with self.assertRaises(MinMaxError):
                self.method(key="foo", kwargs=kwargs, valmin=15)

        def test_exists_badmax(self):
            """Key "foo" exists with value 10, valmax 5, throws MinMaxError due to 5 <= 10."""
            kwargs = {"foo": 10}
            with self.assertRaises(MinMaxError):
                self.method(key="foo", kwargs=kwargs, valmax=5)

        def test_exists_badminmax(self):
            """Key "foo" exists with value 10, valmin of 1, valmax of 9, throws MinMaxError due to 9 <= 10."""
            kwargs = {"foo": 10}
            with self.assertRaises(MinMaxError):
                self.method(key="foo", kwargs=kwargs, valmin=1, valmax=9)

        def test_exists_badtype(self):
            """Key "foo" exists with value "BAR", throws InvalidTypeError due to invalid int."""
            kwargs = {"foo": "BAR"}
            with self.assertRaises(InvalidTypeError):
                self.method(key="foo", kwargs=kwargs)

        def test_missing(self):
            """Key "foo" missing, throws MissingError due to missing key and no default."""
            kwargs = {}
            with self.assertRaises(MissingError):
                self.method(key="foo", kwargs=kwargs)

        def test_missing_req(self):
            """Key "foo" missing, is required, throws MissingError due to missing key."""
            kwargs = {}
            with self.assertRaises(MissingError):
                self.method(key="foo", kwargs=kwargs, req=True)

        def test_nokwargs_nov(self):
            """Supply no kwargs, no v, throws MissingError due to missing value."""
            with self.assertRaises(ArgumentError):
                self.method(key="foo")

        def test_badkwargs(self):
            """Supply kwargs as non dict, throws ArgumentError due to invalid kwargs."""
            kwargs = []
            with self.assertRaises(ArgumentError):
                self.method(key="foo", kwargs=kwargs)

    class TestBoolArgs(unittest.TestCase):
        """Test ArgumentTool.argbool method."""

        @classmethod
        def setUpClass(cls):  # noqa
            cls.ARG_TOOL = ArgumentTool()
            cls.method = cls.ARG_TOOL.argbool
            cls.itypes = BOOL_TYPES
            print("Testing ArgumentTool().argbool()\n_______________________________")

        def test_exists(self):
            """Key "foo" exists with value True, returns True."""
            kwargs = {"foo": True}
            value = self.method(key="foo", kwargs=kwargs)
            self.assertIsInstance(value, self.itypes)
            self.assertEqual(value, True)

        def test_missing_default(self):
            """Key "foo" missing, default = True, returns True."""
            kwargs = {}
            value = self.method(key="foo", kwargs=kwargs, default=True)
            self.assertIsInstance(value, self.itypes)
            self.assertEqual(value, True)

        def test_nokwargs_kv(self):
            """Supply no kwargs, a manual key "foo", value True, returns True."""
            value = self.method(key="foo", value=True)
            self.assertIsInstance(value, self.itypes)
            self.assertEqual(value, True)

        def test_exists_req(self):
            """Key "foo" is required, key exists with value True, returns True."""
            kwargs = {"foo": True}
            value = self.method(key="foo", kwargs=kwargs, req=True)
            self.assertIsInstance(value, self.itypes)
            self.assertEqual(value, True)

        def test_exists_badtype(self):
            """Key "foo" exists with value 123, throws InvalidTypeError due to invalid str."""
            kwargs = {"foo": 123}
            with self.assertRaises(InvalidTypeError):
                self.method(key="foo", kwargs=kwargs)

        def test_missing(self):
            """Key "foo" missing, no default, throws MissingError due to missing key."""
            kwargs = {}
            with self.assertRaises(MissingError):
                self.method(key="foo", kwargs=kwargs)

        def test_missing_req(self):
            """Key "foo" missing, default of True, is required, throws MissingError due to missing key."""
            kwargs = {}
            with self.assertRaises(MissingError):
                self.method(key="foo", kwargs=kwargs, default=True, req=True)

        def test_nokwargs_nov(self):
            """Supply no kwargs, no v, throws MissingError due to missing value."""
            with self.assertRaises(ArgumentError):
                self.method(key="foo")

        def test_badkwargs(self):
            """Supply kwargs as non dict, throws ArgumentError due to invalid kwargs."""
            kwargs = []
            with self.assertRaises(ArgumentError):
                self.method(key="foo", kwargs=kwargs)

    class TestDictArgs(unittest.TestCase):
        """Test ArgumentTool.argdict method."""

        @classmethod
        def setUpClass(cls):  # noqa
            cls.ARG_TOOL = ArgumentTool()
            cls.method = cls.ARG_TOOL.argdict
            cls.itypes = DICT_TYPES
            print("Testing ArgumentTool().argdict()\n_______________________________")

        def test_exists(self):
            """Key "foo" exists with value {"x": 1}, returns {"x": 1}."""
            kwargs = {"foo": {"x": 1}}
            value = self.method(key="foo", kwargs=kwargs)
            self.assertIsInstance(value, self.itypes)
            self.assertEqual(value, {"x": 1})

        def test_missing_default(self):
            """Key "foo" missing, default = {"x": 1}, returns {"x": 1}."""
            kwargs = {}
            value = self.method(key="foo", kwargs=kwargs, default={"x": 1})
            self.assertIsInstance(value, self.itypes)
            self.assertEqual(value, {"x": 1})

        def test_nokwargs_kv(self):
            """Supply no kwargs, a manual key "foo", value {"x": 1}, returns {"x": 1}."""
            value = self.method(key="foo", value={"x": 1})
            self.assertIsInstance(value, self.itypes)
            self.assertEqual(value, {"x": 1})

        def test_exists_req(self):
            """Key "foo" is required, key exists with value {"x": 1}, returns {"x": 1}."""
            kwargs = {"foo": {"x": 1}}
            value = self.method(key="foo", kwargs=kwargs, req=True)
            self.assertIsInstance(value, self.itypes)
            self.assertEqual(value, {"x": 1})

        def test_exists_badtype(self):
            """Key "foo" exists with value 123, throws InvalidTypeError due to invalid str."""
            kwargs = {"foo": 123}
            with self.assertRaises(InvalidTypeError):
                self.method(key="foo", kwargs=kwargs)

        def test_missing(self):
            """Key "foo" missing, no default, throws MissingError due to missing key."""
            kwargs = {}
            with self.assertRaises(MissingError):
                self.method(key="foo", kwargs=kwargs)

        def test_missing_req(self):
            """Key "foo" missing, default of {"x": 1}, is required, throws MissingError due to missing key."""
            kwargs = {}
            with self.assertRaises(MissingError):
                self.method(key="foo", kwargs=kwargs, default={"x": 1}, req=True)

        def test_nokwargs_nov(self):
            """Supply no kwargs, no v, throws MissingError due to missing value."""
            with self.assertRaises(ArgumentError):
                self.method(key="foo")

        def test_badkwargs(self):
            """Supply kwargs as non dict, throws ArgumentError due to invalid kwargs."""
            kwargs = []
            with self.assertRaises(ArgumentError):
                self.method(key="foo", kwargs=kwargs)

    unittest.main(verbosity=3, failfast=True)
