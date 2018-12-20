#!/usr/bin/env python
# -*- mode: Python; tab-width: 4; indent-tabs-mode: nil; -*-
# ex: set tabstop=4
# Please do not change the two lines above. See PEP 8, PEP 263.
'''Provides an interactive console with pytan available as handler'''
__author__ = 'Jim Olsen <jim.olsen@tanium.com>'
__version__ = '2.1.5'

import os
import sys
sys.dont_write_bytecode = True

my_file = os.path.abspath(sys.argv[0])
my_name = os.path.splitext(os.path.basename(my_file))[0]
my_dir = os.path.dirname(my_file)
parent_dir = os.path.dirname(my_dir)
lib_dir = os.path.join(parent_dir, 'lib')
path_adds = [lib_dir]
[sys.path.append(aa) for aa in path_adds if aa not in sys.path]

import pytan
import pytan.binsupport
import taniumpy

if __name__ == "__main__":
    pytan.binsupport.version_check(reqver=__version__)

    setupmethod = getattr(pytan.binsupport, 'setup_pytan_shell_argparser')
    responsemethod = getattr(pytan.binsupport, 'process_pytan_shell_args')

    parser = setupmethod(doc=__doc__)
    parser.add_argument(
        '-c',
        '--count',
        required=False,
        action='store',
        dest='client_count',
        type=int,
        default=5,
        help='client count',
    )
    args = parser.parse_args()

    handler = pytan.binsupport.process_handler_args(parser=parser, args=args)
    response = responsemethod(parser=parser, handler=handler, args=args)

    import xmltodict
    client_count = args.client_count
    object_list = "<client_count>{}</client_count>".format(client_count)
    request_body = handler.session._build_body(object_list=object_list, command="GetObject", )
    response_body = handler.session._get_response(request_body=request_body)
    response_dict = xmltodict.parse(response_body)
    result_object = response_dict["soap:Envelope"]["soap:Body"]["t:return"]["result_object"]
    client_count = result_object["client_count"]
    print(client_count)
