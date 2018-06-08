"""BaseType used by all taniumpy objects."""
import csv
import functools
import io
import json
import operator
import pprint
import re
import sys

try:
    import xml.etree.cElementTree as ET
except:
    import xml.etree.ElementTree as ET

IS_PY2 = sys.version_info[0] == 2
"""Coarse Python version differential."""

STR = unicode if IS_PY2 else str  # noqa
"""String type to use, depending on Python version."""

STR_TYPES = (STR, basestring) if IS_PY2 else (STR,)  # noqa
"""Tuple of valid string types, depending on Python version."""

INT_TYPES = (int, long) if IS_PY2 else (int,)  # noqa
"""Tuple of valid int types, depending on Python version."""

LIST_TYPES = (list, tuple)
"""Tuple of valid list types."""


def rgetattr(obj, attr, *args):
    """Method that supplies dotted notation to getattr."""
    def _getattr(obj, attr):
        return getattr(obj, attr, *args)
    return functools.reduce(_getattr, [obj] + attr.split('.'))


def mkargs(orig_kwargs, **new_kwargs):
    """Make a new kwargs dict with orig_kwargs and **new_kwargs."""
    margs = {}
    margs.update(orig_kwargs)
    margs.update(new_kwargs)
    if orig_kwargs.get('pytan_help', ""):
        margs['pytan_help'] = orig_kwargs.get('pytan_help', "")
    return margs


class IncorrectTypeException(Exception):
    """Raised when a property is not of the expected type."""

    def __init__(self, property, expected, actual):
        """Constructor."""
        self.property = property
        self.expected = expected
        self.actual = actual
        err = 'Property {} is not of type {}, got {}'.format
        Exception.__init__(self, err(property, str(expected), str(actual)))


class BaseType(object):
    """BaseType used by all taniumpy objects."""

    _soap_tag = None
    STR_ATTRS = None
    SUMMARY = None

    def __init__(self, simple_properties, complex_properties, list_properties):
        """Constructor."""
        self._initialized = False
        self._simple_properties = simple_properties
        self._complex_properties = complex_properties
        self._list_properties = list_properties
        self._initialized = True
        str_attrs = getattr(self, "STR_ATTRS", []) or []
        def_attrs = [x for x in ["name", "id"] if x in self._sprops]
        self.STR_ATTRS = def_attrs + str_attrs

    """LIST METHOD."""
    def __getitem__(self, n):
        """Allow automatic indexing into lists."""
        return self._list[n]

    """LIST METHOD."""
    def __iadd__(self, value):
        """Support += operand."""
        other = self._item_types(value)
        self._list += other
        return self

    """LIST METHOD."""
    def __add__(self, value):
        """Support + operand."""
        other = self._item_types(value)
        ret = self._new
        ret._list = self._list + other
        return ret

    def __len__(self):
        """Allow len() for lists."""
        if self.is_list:
            ret = len(getattr(self, self.list_attrs["attr"]))
        else:
            ret = len([v for k, v in self._avals.items() if v is not None])
        return ret

    def __str__(self):
        """String method."""
        vals = []
        if getattr(self, "SUMMARY", None):
            m = "Summary: {}".format(self.SUMMARY)
            vals.append(m)
        if self.is_list:
            m = "length: {}".format(len(self))
            vals.append(m)
        else:
            # invattr = "Invalid attr: {!r}".format
            # m = "{!r}".format({k: v for k, v in self._avals.items() if k in self.STR_ATTRS})
            m = pprint.pformat({k: v for k, v in self._avals.items() if k in self.STR_ATTRS}, width=200)
            vals.append(m)
            # setcnt = len([v for k, v in self._avals.items() if v is not None])
            # unsetcnt = len([v for k, v in self._avals.items() if v is None])
            # m = "attrs: {s} set, {u} unset".format(s=setcnt, u=unsetcnt)
            # vals.append(m)
        ret = "{} {}".format(self._sname, ", ".join(vals))
        return ret

    def __eq__(self, value):
        """Allow for self == / != value using serialized json of self and value."""
        if not isinstance(value, self.__class__):
            m = "Unable to compare '{s}' type {st} against value '{v}' type {vt}"
            m = m.format(s=self, st=type(self), v=value, vt=type(value))
            raise Exception(m)

        selfj = self.to_json(self)
        valuej = value.to_json(value)
        ret = selfj == valuej
        return ret

    def __repr__(self):
        """Return the string instead of default repr."""
        ret = "{!r}".format(self.__str__())
        return ret

    def __setattr__(self, attr, value):
        """Enforce type for self.attr = value, if attr is a complex property."""
        if value is not None and attr != "_initialized" and self._isinit:
            if attr in self._cprops:
                ctype = self._cprops[attr]
                if not isinstance(value, ctype):
                    raise IncorrectTypeException(property=value, expected=ctype, actual=type(value))
        super(BaseType, self).__setattr__(attr, value)

    @property
    def _isinit(self):
        """Return bool if self._initialized."""
        ret = getattr(self, "_initialized", False)
        return ret

    @property
    def _lprops(self):
        """Return _list_properties dict."""
        ret = getattr(self, "_list_properties", {})
        return ret

    @property
    def _cprops(self):
        """Return _complex_properties dict."""
        ret = getattr(self, "_complex_properties", {})
        return ret

    @property
    def _sprops(self):
        """Return _simple_properties dict."""
        ret = getattr(self, "_simple_properties", {})
        return ret

    @property
    def _svals(self):
        """Return a dictionary with all of the key/value pairs of obj that are simple properties."""
        ret = {k: getattr(self, k) for k in self._sprops.keys()}
        return ret

    @property
    def _cvals(self):
        """Return a dictionary with all of the key/value pairs of obj that are complex properties."""
        ret = {k: getattr(self, k) for k in self._cprops.keys()}
        return ret

    @property
    def _avals(self):
        """Return a dictionary with all of the key/value pairs of obj that are simple or complex properties."""
        ret = dict(list(self._svals.items()) + list(self._cvals.items()))
        return ret

    @property
    def _new(self):
        """Return a new instance of self."""
        return self.__class__()

    @property
    def _name(self):
        """Return class name of self."""
        return self.__class__.__name__

    @property
    def _sname(self):
        """Return soap name of self."""
        return "<{}>".format(self._soap_tag)

    """LIST METHOD."""
    def _item_types(self, value):
        """Check that all items in list value are of the right list item type."""
        if isinstance(value, self.__class__):
            other = value._list
        elif isinstance(value, LIST_TYPES):
            other = value
        else:
            m = "Supplied value {!r} of type {}, must supply one of types {}"
            m = m.format(value, type(value), [LIST_TYPES, self.__class__])
            raise Exception(m)

        for o in other:
            self._item_type(o, other)
        return other

    def _item_type(self, value, container=None):
        """Check that item in value is of the right list item type."""
        if not isinstance(value, self.list_attrs["type"]):
            if container:
                m = "Supplied item {!r} of type {} in {} with {} items, all items must be of type {}"
                m = m.format(value, type(value), type(container), len(container), self.list_attrs["type"])
            else:
                m = "Supplied item {!r} of type {}, item must be of type {}"
                m = m.format(value, type(value), self.list_attrs["type"])
            raise Exception(m)

    """LIST METHOD."""
    @property
    def _list(self):
        """Access this objects ACTUAL list object."""
        ret = getattr(self, self.list_attrs["attr"])
        return ret

    """LIST METHOD."""
    @_list.setter
    def _list(self, value):
        """Update this objects ACTUAL list object."""
        ret = setattr(self, self.list_attrs["attr"], value)
        return ret

    """LIST METHOD."""
    def search(self, val, attr, op, **kwargs):
        """Find items in list by attr & op."""
        margs = mkargs(kwargs, attr=attr, val=val, op=op)
        margs["newobj"] = newobj = margs.get("newobj", False)
        margs["slower"] = slower = margs.get("slower", False)
        margs["smax"] = smax = margs.get("smax", None)
        margs["smin"] = smin = margs.get("smin", None)
        margs["snot"] = snot = margs.get("snot", False)
        margs["serror"] = serror = margs.get("serror", True)

        margs["val"] = val = "{}".format(val).lower() if slower else val
        margs["voc"] = ["in", "ends", "starts"]
        margs["vop"] = [x for x in dir(operator) if not x.startswith("_")]
        margs["istxt"] = "IS NOT" if snot else "IS"
        margs["me"] = self
        margs["matches"] = matches = []

        for obj in self._list:
            aval = rgetattr(obj, attr)
            aval = "{}".format(aval).lower() if slower else aval
            if op == "in":
                smatch = aval in val
            elif op == "ends":
                smatch = "{}".format(aval).endswith("{}".format(val))
            elif op == "starts":
                smatch = "{}".format(aval).startswith("{}".format(val))
            else:
                if hasattr(operator, op):
                    aop = getattr(operator, op)
                    smatch = aop(aval, val)
                else:
                    m = "{op} is an invalid operator, use any of {voc} or {vop}!".format(**margs)
                    raise Exception(m)

            smatch = not smatch if snot else smatch
            if smatch and obj not in matches:
                matches.append(obj)

        margs["mcnt"] = mcnt = len(matches)
        m = (
            "{mcnt} matches found in {me} where attributes {attr!r} {istxt} {op} {val!r}, "
            "minimum matches: {smin}, maximum matches: {smax}"
        )
        m = m.format(**margs)

        if ((smin is not None and mcnt < smin) or (smax is not None and mcnt > smax)) and serror:
            raise Exception(m)

        if newobj:
            ret = self._new
            ret._list = matches
        elif smax == 1:
            if mcnt == 1:
                # return single found object if smax is 1
                ret = matches[0]
            else:
                ret = None
        # just return all matches as a regular list
        else:
            ret = matches
        return ret

    @property
    def info(self):
        """Construct a string that explains self."""
        ret = []
        m = "{}".format(self)
        ret.append(m)
        j = "\n\t"
        if self.is_list:
            m = ", items: {i}".format
            if self._list:
                items = ["IDX:{} {}".format(idx, x) for idx, x in enumerate(self._list)]
                ret.append(m(i=j + j.join(items)))
            else:
                ret.append(m(i="none"))
        else:
            ret.append(", ALL ATTRIBUTES:")
            atxt = "{}.{} = {!r}".format
            setitems = sorted([atxt(self._name, k, v) for k, v in self._avals.items() if v is not None])
            unsetitems = sorted([atxt(self._name, k, v) for k, v in self._avals.items() if v is None])
            if setitems:
                ret.append(j + j.join(setitems))
            if unsetitems:
                ret.append(j + j.join(unsetitems))
        ret = "".join(ret)
        return ret

    """LIST METHOD."""
    @property
    def is_list(self):
        """Return true/false if self is a list type object."""
        ret = len(self._lprops) == 1
        return ret

    """LIST METHOD."""
    @property
    def list_attrs(self):
        """Return this objects list attributes as a dict with attr/type."""
        if not self.is_list:
            m = "Not a list type, can not get list attributes from _list_properties: {}"
            m = m.format(self._lprops)
            raise Exception(m)

        i = self._lprops.items()[0]
        a, t = i
        ret = {"attr": a, "type": t}
        return ret

    """LIST METHOD."""
    def append(self, value):
        """Allow adding to list."""
        self._item_type(value)
        self._list.append(value)

    """LIST METHOD."""
    def remove(self, value, attr=None, **kwargs):
        """Allow removing from list, optionally by attr."""
        if attr is None:
            self._item_type(value)
            self._list.remove(value)
        else:
            self._list = self._filter(value, attr, **kwargs)

    """LIST METHOD."""
    def sort(self, attr="id", reverse=False):
        """Sort a list in place."""
        self._list = sorted(self._list, key=lambda x: getattr(x, attr), reverse=reverse)

    def toSOAPElement(self, minimal=False): # noqa
        root = ET.Element(self._soap_tag)
        for p in self._simple_properties:
            el = ET.Element(p)
            val = getattr(self, p)
            if val is not None:
                el.text = str(val)
            if val is not None or not minimal:
                root.append(el)
        for p, t in self._complex_properties.iteritems():
            val = getattr(self, p)
            if val is not None or not minimal:
                if val is not None and not isinstance(val, t):
                    raise IncorrectTypeException(p, t, type(val))
                if isinstance(val, BaseType):
                    child = val.toSOAPElement(minimal=minimal)
                    # the tag name is the property name,
                    # not the property type's soap tag
                    el = ET.Element(p)
                    if child.getchildren() is not None:
                        for child_prop in child.getchildren():
                            el.append(child_prop)
                    root.append(el)
                else:
                    el = ET.Element(p)
                    root.append(el)
                    if val is not None:
                        el.append(str(val))
        for p, t in self._list_properties.iteritems():
            vals = getattr(self, p)
            if not vals:
                continue
            # fix for str types in list props
            if issubclass(t, BaseType):
                for val in vals:
                    root.append(val.toSOAPElement(minimal=minimal))
            else:
                for val in vals:
                    el = ET.Element(p)
                    root.append(el)
                    if val is not None:
                        el.text = str(val)
                    if vals is not None or not minimal:
                        root.append(el)
        return root

    def toSOAPBody(self, minimal=False): # noqa
        out = io.BytesIO()
        ET.ElementTree(self.toSOAPElement(minimal=minimal)).write(out)
        return out.getvalue()

    @classmethod
    def fromSOAPElement(cls, el): # noqa
        result = cls()
        for p, t in result._simple_properties.iteritems():
            pel = el.find("./{}".format(p))
            if pel is not None and pel.text:
                setattr(result, p, t(pel.text))
            else:
                setattr(result, p, None)
        for p, t in result._complex_properties.iteritems():
            elems = el.findall('./{}'.format(p))
            if len(elems) > 1:
                raise Exception(
                    'Unexpected: {} elements for property'.format(p)
                )
            elif len(elems) == 1:
                setattr(
                    result,
                    p,
                    result._complex_properties[p].fromSOAPElement(elems[0]),
                )
            else:
                setattr(result, p, None)
        for p, t in result._list_properties.iteritems():
            setattr(result, p, [])
            elems = el.findall('./{}'.format(p))
            for elem in elems:
                if issubclass(t, BaseType):
                    getattr(result, p).append(t.fromSOAPElement(elem))
                else:
                    getattr(result, p).append(elem.text)

        return result

    @classmethod
    def fromSOAPBody(cls, body): # noqa
        """Parse body (text) and produce Python tanium objects.

        This method assumes a single result_object, which
        may be a list or a single object.

        """
        tree = ET.fromstring(body)
        result_object = tree.find(".//result_object/*")
        if result_object is None:
            return None  # no results, not an error
        # based on the tag of the matching element,
        # find the appropriate tanium_type and deserialize
        from object_list_types import OBJECT_LIST_TYPES
        if result_object.tag not in OBJECT_LIST_TYPES:
            raise Exception('Unknown type {}'.format(result_object.tag))
        r = OBJECT_LIST_TYPES[result_object.tag].fromSOAPElement(result_object)
        r._RESULT_OBJECT = result_object
        return r

    def flatten_jsonable(self, val, prefix):
        """Return a json representation with children represented in . format."""
        result = {}
        if type(val) == list:
            for i, v in enumerate(val):
                result.update(self.flatten_jsonable(
                    v,
                    '_'.join([prefix, str(i)]))
                )
        elif type(val) == dict:
            for k, v in val.iteritems():
                result.update(self.flatten_jsonable(
                    v,
                    '_'.join([prefix, k] if prefix else k))
                )
        else:
            result[prefix] = val
        return result

    def to_flat_dict_explode_json(self, val, prefix=""):
        """If the value is json. If so, flatten it out into a dict."""
        try:
            js = json.loads(val)
            return self.flatten_jsonable(js, prefix)
        except Exception:
            return None

    def to_flat_dict(self, prefix='', explode_json_string_values=False):
        """Convert the object to a dict, flattening any lists or nested types."""
        result = {}
        prop_start = '{}_'.format(prefix) if prefix else ''
        for p, _ in self._simple_properties.iteritems():
            val = getattr(self, p)
            if val is not None:
                json_out = None
                if explode_json_string_values:
                    json_out = self.to_flat_dict_explode_json(val, p)
                if json_out is not None:
                    result.update(json_out)
                else:
                    result['{}{}'.format(prop_start, p)] = val
        for p, _ in self._complex_properties.iteritems():
            val = getattr(self, p)
            if val is not None:
                result.update(val.to_flat_dict(
                    prefix='{}{}'.format(prop_start, p),
                    explode_json_string_values=explode_json_string_values,
                ))
        for p, _ in self._list_properties.iteritems():
            val = getattr(self, p)
            if val is not None:
                for ind, item in enumerate(val):
                    prefix = '{}{}_{}'.format(prop_start, p, ind)
                    if isinstance(item, BaseType):
                        result.update(item.to_flat_dict(
                            prefix=prefix,
                            explode_json_string_values=explode_json_string_values,
                        ))
                    else:
                        result[prefix] = item
        return result

    def explode_json(self, val):
        """Load value as a json object."""
        try:
            return json.loads(val)
        except Exception:
            return None

    def to_jsonable(self, explode_json_string_values=False, include_type=True):
        """Turn self into a json representation."""
        result = {}
        if include_type:
            result['_type'] = self._soap_tag
        for p, _ in self._simple_properties.iteritems():
            val = getattr(self, p)
            if val is not None:
                json_out = None
                if explode_json_string_values:
                    json_out = self.explode_json(val)
                if json_out is not None:
                    result[p] = json_out
                else:
                    result[p] = val
        for p, _ in self._complex_properties.iteritems():
            val = getattr(self, p)
            if val is not None:
                result[p] = val.to_jsonable(
                    explode_json_string_values=explode_json_string_values,
                    include_type=include_type)
        for p, _ in self._list_properties.iteritems():
            val = getattr(self, p)
            if val is not None:
                result[p] = []
                for ind, item in enumerate(val):
                    if isinstance(item, BaseType):
                        result[p].append(item.to_jsonable(
                            explode_json_string_values=explode_json_string_values,
                            include_type=include_type))
                    else:
                        result[p].append(item)
        return result

    @staticmethod
    def to_json(jsonable, **kwargs):
        """Convert to a json string.

        jsonable can be a single BaseType instance of a list
        of BaseType

        """
        sort_keys = kwargs.get("sort_keys", True)
        indent = kwargs.get("indent", 2)
        if type(jsonable) == list:
            ret = [item.to_jsonable(**kwargs) for item in jsonable]
        else:
            ret = jsonable.to_jsonable(**kwargs)
        ret = json.dumps(ret, sort_keys=sort_keys, indent=indent)
        return ret

    @classmethod
    def _from_json(cls, jsonable):
        """Private helper to parse from JSON after type is instantiated."""
        result = cls()
        for p, t in result._simple_properties.iteritems():
            val = jsonable.get(p)
            if val is not None:
                setattr(result, p, t(val))
        for p, t in result._complex_properties.iteritems():
            val = jsonable.get(p)
            if val is not None:
                setattr(result, p, BaseType.from_jsonable(val))
        for p, t in result._list_properties.iteritems():
            val = jsonable.get(p)
            if val is not None:
                vals = []
                for item in val:
                    if issubclass(t, BaseType):
                        vals.append(BaseType.from_jsonable(item))
                    else:
                        vals.append(item)
                setattr(result, p, vals)
        return result

    @staticmethod
    def from_jsonable(jsonable):
        """Inverse of to_jsonable, with explode_json_string_values=False.

        This can be used to import objects from serialized JSON.
        This JSON should come from BaseType.to_jsonable(explode_json_string_values=False, include+type=True)

        Examples
        --------
        >>> with open('question_list.json') as fd:
        ...    questions = json.loads(fd.read())
        ...    # is a list of serialized questions
        ...    question_objects = BaseType.from_jsonable(questions)
        ...    # will return a list of api.Question

        """
        if type(jsonable) == list:
            return [BaseType.from_jsonable(item for item in list)]
        elif type(jsonable) == dict:
            if not jsonable.get('_type'):
                raise Exception('JSON must contain _type to be deserialized')
            from object_list_types import OBJECT_LIST_TYPES
            if jsonable['_type'] not in OBJECT_LIST_TYPES:
                raise Exception('Unknown type {}'.format(jsonable['_type']))
            result = OBJECT_LIST_TYPES[jsonable['_type']]._from_json(jsonable)
            return result
        else:
            raise Exception('Expected list or dict to deserialize')

    @staticmethod
    def write_csv(fd, val, explode_json_string_values=False, **kwargs):
        """Write 'val' to CSV. val can be a BaseType instance or a list of BaseType.

        This does a two-pass, calling to_flat_dict for each object, then
        finding the union of all headers,
        then writing out the value of each column for each object
        sorted by header name

        explode_json_string_values attempts to see if any of the str values
        are parseable by json.loads, and if so treat each property as a column
        value

        fd is a file-like object
        """
        def sort_headers(headers, **kwargs):
            """Return a list of sorted headers (Column names).

            If kwargs has 'header_sort':
              if header_sort == False, do no sorting
              if header_sort == [] or True, do sorted(headers)
              if header_sort == ['col1', 'col2'], do sorted(headers), then
                put those headers first in order if they exist
            """
            header_sort = kwargs.get('header_sort', [])

            if header_sort is False:
                return headers
            elif header_sort is True:
                pass
            elif not type(header_sort) in [list, tuple]:
                raise Exception("header_sort must be a list!")

            headers = sorted(headers)

            if header_sort is True or not header_sort:
                return headers

            custom_sorted_headers = []
            for hs in header_sort:
                for hidx, h in enumerate(headers):
                    if h.lower() == hs.lower():
                        custom_sorted_headers.append(headers.pop(hidx))

            # append the rest of the sorted_headers that didn't
            # match header_sort
            custom_sorted_headers += headers
            return custom_sorted_headers

        def fix_newlines(val):
            if type(val) == str:
                # turn \n into \r\n
                val = re.sub(r"([^\r])\n", r"\1\r\n", val)
            return val

        base_type_list = [val] if isinstance(val, BaseType) else val
        headers = set()
        for base_type in base_type_list:
            row = base_type.to_flat_dict(explode_json_string_values=explode_json_string_values)
            for col in row:
                headers.add(col)

        writer = csv.writer(fd)

        headers_sorted = sort_headers(list(headers), **kwargs)
        writer.writerow(headers_sorted)

        for base_type in base_type_list:
            row = base_type.to_flat_dict(explode_json_string_values=explode_json_string_values)
            writer.writerow([fix_newlines(row.get(col, '')) for col in headers_sorted])
