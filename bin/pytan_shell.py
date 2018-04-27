#!/usr/bin/env python -i
"""Provide an interactive console with pytan available as handler."""

import os
import sys

__author__ = 'Jim Olsen <jim.olsen@tanium.com>'
__version__ = '2.1.5'

my_file = os.path.abspath(sys.argv[0])
my_name = os.path.splitext(os.path.basename(my_file))[0]
my_dir = os.path.dirname(my_file)
parent_dir = os.path.dirname(my_dir)
lib_dir = os.path.join(parent_dir, 'lib')
path_adds = [lib_dir]
[sys.path.append(aa) for aa in path_adds if aa not in sys.path]

try:
    import pytan
    import pytan.binsupport
    import taniumpy  # noqa
except Exception:
    raise


if __name__ == "__main__":
    pytan.binsupport.version_check(reqver=__version__)

    setupmethod = getattr(pytan.binsupport, 'setup_{}_argparser'.format(my_name))
    responsemethod = getattr(pytan.binsupport, 'process_{}_args'.format(my_name))

    parser = setupmethod(doc=__doc__)
    args = parser.parse_args()

    handler = pytan.binsupport.process_handler_args(parser=parser, args=args)
    response = responsemethod(parser=parser, handler=handler, args=args)

    def j(o):
        """Convert o into json."""
        r = handler.export_obj(o, "json")
        return r

    def jp(o):
        """Convert o into json and print it."""
        r = j(o)
        print(r)

# add_roles = [
#     "Legacy - Action User",
#     "Administrator",
#     "test111",
# ]
# del_roles = [
#     "Discover User",
#     "test discover",
#     # "xxx",
# ]
# z = handler.mod_roles_user(user="blah35", add_roles=add_roles, del_roles=del_roles)

# props = [
#     {"name": "info1", "value": "info here"},
#     {"name": "other info", "value": "other info here"},
#     {"name": "info3", "value": "hidden from console info here", "show": False},
# ]
# gn = [
#     "dumdum",
#     "aaaa",
#     "dumdumdddd",
# ]
# u1 = handler.create_user(name="testabc", props=props, del_exists=True, del_wait=0)
# u2 = handler.create_user(name="testabc", props=props, group_names=gn, del_exists=True, del_wait=0)
# v = handler.find_roles(roles=["Administrator", 1])
