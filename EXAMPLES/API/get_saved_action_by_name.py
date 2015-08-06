
"""
Get a saved action by name
"""

import os
import sys
sys.dont_write_bytecode = True

# Determine our script name, script dir
my_file = os.path.abspath(sys.argv[0])
my_dir = os.path.dirname(my_file)

# determine the pytan lib dir and add it to the path
parent_dir = os.path.dirname(my_dir)
pytan_root_dir = os.path.dirname(parent_dir)
lib_dir = os.path.join(pytan_root_dir, 'lib')
path_adds = [lib_dir]

for aa in path_adds:
    if aa not in sys.path:
        sys.path.append(aa)


# connection info for Tanium Server
USERNAME = "Tanium User"
PASSWORD = "T@n!um"
HOST = "172.16.31.128"
PORT = "444"

# Logging conrols
LOGLEVEL = 2
DEBUGFORMAT = False

import tempfile

import pytan
handler = pytan.Handler(
    username=USERNAME,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    loglevel=LOGLEVEL,
    debugformat=DEBUGFORMAT,
)

print handler

# setup the arguments for the handler method
kwargs = {}
kwargs["objtype"] = u'saved_action'
kwargs["name"] = u'Distribute Tanium Standard Utilities'

# call the handler with the get method, passing in kwargs for arguments
response = handler.get(**kwargs)

print ""
print "Type of response: ", type(response)

print ""
print "print of response:"
print response

print ""
print "length of response (number of objects returned): "
print len(response)

print ""
print "print the first object returned in JSON format:"
out = response.to_json(response[0])
if len(out.splitlines()) > 15:
    out = out.splitlines()[0:15]
    out.append('..trimmed for brevity..')
    out = '\n'.join(out)

print out



'''Output from running this:
Handler for Session to 172.16.31.128:444, Authenticated: True, Version: Not yet determined!

Type of response:  <class 'taniumpy.object_types.saved_action_list.SavedActionList'>

print of response:
SavedActionList, len: 1

length of response (number of objects returned): 
1

print the first object returned in JSON format:
{
  "_type": "saved_action", 
  "action_group_id": 0, 
  "comment": "Distributes the Hardware Tools used for hardware identification.", 
  "creation_time": "2015-03-03T19:06:00", 
  "distribute_seconds": 0, 
  "end_time": "Never", 
  "expire_seconds": 660, 
  "id": 14, 
  "issue_count": 0, 
  "issue_seconds": 86400, 
  "last_action": {
    "_type": "action", 
    "id": 4294967295, 
    "start_time": "Never"
..trimmed for brevity..

'''
