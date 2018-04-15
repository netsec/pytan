"""Handler and testing configuration variables."""

SERVER_INFO = {
    # pytan handler arguments
    "username": "Administrator",
    "password": "Tanium2015!",
    "host": "172.16.30.130",
    "port": "443",
    "debugformat": False,
    "loglevel": 1,  # control level of logging for pytan
    # testing arguments
    "testlevel": 3,  # control level of logging / verbosity for unittest
    'FAILFAST': False,  # have unittest exit immediately on unexpected error
    'CATCHBREAK': True,  # catch control-C to allow current test suite to finish (press 2x to force)
    'BUFFER': False,  # only show output from failed tests
}
