#!/usr/bin/env python
"""Provide an interactive console with pytan available as handler."""

import os
import re
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

    setupmethod = getattr(pytan.binsupport, 'setup_pytan_shell_argparser')
    responsemethod = getattr(pytan.binsupport, 'process_pytan_shell_args')

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

    def run(c):
        """Print and eval code c."""
        print("code: {}".format(c))
        exec(c, globals(), globals())


old_server_name = "oldserver.test.com"
new_server_name = "newserver.test.com"

old_name_re = r"(.*)({})(.*)".format(old_server_name)
new_name_re = r"\1{}\3".format(new_server_name)
old_name_re = re.compile(old_name_re, re.I)

enable_save = False
debug = False

# get all packages
all_pkgs = handler.get_all("package", include_hidden_flag=1)

for p in all_pkgs:
    if not p.files:
        continue
    do_save = False
    for f in p.files:
        if debug:
            m = "Now in pkg: {!r} file name: {!r}, file_source: {!r}"
            print(m.format(p.name, f.name, f.source))
        if f.name and old_name_re.search(f.name):
            new_txt = old_name_re.sub(new_name_re, f.name)
            m = "Updating pkg: {!r} file name: {!r} to name: {!r}"
            print(m.format(p.name, f.name, new_txt))
            f.name = new_txt
            do_save = True
        if f.source and old_name_re.search(f.source):
            new_txt = old_name_re.sub(new_name_re, f.source)
            m = "Updating pkg: {!r} file source: {!r} to source: {!r}"
            print(m.format(p.name, f.source, new_txt))
            f.source = new_txt
            do_save = True
    if do_save:
        if enable_save:
            p = handler.session.save(p)
            m = "Saved changes to pkg: {!r}"
            print(m.format(p.name))
        else:
            m = "WOULD save changes to pkg: {!r}"
            print(m.format(p.name))


'''
search = taniumpy.PackageFileList()
result = handler.session.find(search)
for i in result:
    print("name: {}, id: {}, source: {}".format(i.name, i.id, i.source))
'''
