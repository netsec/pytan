#!/usr/bin/env python
# -*- mode: Python; tab-width: 4; indent-tabs-mode: nil; -*-
# ex: set tabstop=4
# Please do not change the two lines above. See PEP 8, PEP 263.
"""Create a group object from command line arguments using a CSV as data source."""

import csv
import os
import sys

__author__ = 'Jim Olsen <jim.olsen@tanium.com>'
__version__ = '2.2.0'

pytan_path = "/github/pytan-master/lib"

my_file = os.path.abspath(sys.argv[0])
my_name = os.path.splitext(os.path.basename(my_file))[0]
my_dir = os.path.dirname(my_file)
parent_dir = os.path.dirname(my_dir)
lib_dir = os.path.join(parent_dir, 'lib')
path_adds = [lib_dir, pytan_path]
[sys.path.append(aa) for aa in path_adds if aa not in sys.path]

try:
    import pytan  # noqa
    import pytan.binsupport  # noqa
    import taniumpy  # noqa
except Exception:
    raise

pytan.binsupport.version_check(reqver=__version__)

setupmethod = getattr(pytan.binsupport, 'setup_pytan_shell_argparser')
responsemethod = getattr(pytan.binsupport, 'process_pytan_shell_args')

parser = setupmethod(doc=__doc__)
parser.add_argument(
    '-csv',
    required=True,
    action='store',
    dest='csvfile',
    type=str,
    default="",
    help=(
        "Path to CSV file containing group definitions to create."
        "Format is: Group Name, Filter Value"
    ),
)
parser.add_argument(
    '-s',
    '--sensor',
    required=False,
    action='store',
    dest='sensor_name',
    type=str,
    default="Tanium Client Subnet",
    help="Sensor name to use for ALL filters for ALL groups that are created",
)
parser.add_argument(
    '-f',
    '--filter',
    required=False,
    action='store',
    dest='filter_type',
    type=str,
    default="contains",
    help="Filter type to use for filter value on --sensor",
)
parser.add_argument(
    '--debug',
    required=False,
    action='store_true',
    dest='debug',
    default=False,
    help="Enable debug mode",
)
parser.add_argument(
    '--pre_cleanup',
    required=False,
    action='store_true',
    dest='pre_cleanup',
    default=False,
    help="Enable pre cleanup mode (try to delete groups by name if they exist before creating them)",
)
parser.add_argument(
    '--post_cleanup',
    required=False,
    action='store_true',
    dest='post_cleanup',
    default=False,
    help="Enable post cleanup mode (try to delete groups by name after creating them)",
)

# list of csv headers that must exist for every row in args.csvfile
csv_headers = ["Group Name", "Group Definition"]

args = parser.parse_args()

if not os.path.exists(args.csvfile):
    m = "UNABLE TO FIND CSV FILE AT: {}".format
    m = m(args.csvfile)
    raise Exception(m)

csv_rows = []

try:
    m = "Now parsing CSV FILE '{}'".format
    m = m(args.csvfile)
    print(m)

    with open(args.csvfile) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print(row['Group Name'], row['last_name'])
            # CSV file MUST HAVE two columns for each row::
            # Group Name, Group Definition
            m = "Now processing row: {}".format
            m = m(row)
            if args.debug:
                print(m)

            for h in csv_headers:
                value = row.get(h, "")
                if not value:
                    m = "Row {} missing value for header {!r}".format
                    m = m(row, h)
                    raise Exception(m)
                else:
                    m = "Row has value {!r} for header {!r}".format
                    m = m(value, h)
                    if args.debug:
                        print(m)
            csv_rows.append(row)

except Exception as e:
    m = "Error while parsing CSV FILE AT: {} -- error: {}".format
    m = m(args.csvfile, e)
    raise e

handler = pytan.binsupport.process_handler_args(parser=parser, args=args)
response = responsemethod(parser=parser, handler=handler, args=args)

for row in csv_rows:
    m = "Now creating computer group for row: {}".format
    m = m(row)
    print(m)
    f1_tpl = "{sensor}{{{value}}}, that {filter1}:=True".format
    f1 = f1_tpl(
        sensor=args.sensor_name,
        filter1=args.filter_type,
        value=row["Group Definition"]
    )

    if args.pre_cleanup:
        try:
            cg_obj = handler.get('group', name=row["Group Name"])[0]
            if args.debug:
                m = "Pre-Cleanup enabled, found computer group named {!r}".format
                m = m(row["Group Name"])
                print(m)
        except:
            m = "Pre-Cleanup enabled, but unable to find computer group named {!r}".format
            m = m(row["Group Name"])
            print(m)
        else:
            try:
                handler.session.delete(cg_obj)
                m = (
                    "Pre-Cleanup enabled!! Computer group {0.name!r} deleted"
                    " with ID {0.id!r}, filter text: {0.text!r}"
                ).format
                print(m(cg_obj))
            except Exception as e:
                m = "Pre-Cleanup enabled, but unable to delete computer group named {!r}, {}".format
                m = m(row["Group Name"], e)
                raise Exception(m)

    cg_args = {}
    cg_args['groupname'] = row["Group Name"]
    cg_args['filters'] = [f1]

    try:
        response = handler.create_group(**cg_args)
    except:
        raise
    else:
        m = "Computer group {0.name!r} created with ID {0.id!r}, filter text: {0.text!r}".format
        print(m(response))

    if args.post_cleanup:
        handler.session.delete(response)
        m = "Post Cleanup enabled, group named {} removed!!!".format
        m = m(row["Group Name"])
        print(m)
