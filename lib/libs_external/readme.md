# OSX example of resetting libs_external dirs
cd /gh/pytan/lib/libs_external/

# wipe out osx and any dirs
rm -rf osx/*
rm -rf any/*

# install the pure source packages to any
pip install --no-deps requests certifi chardet idna urllib3 pyOpenSSL asn1crypto enum34 six ipaddress pycparser xmltodict --target any

# install the binary packages to osx
pip install --no-deps cryptography cffi --target osx

# from windows system, use pip to install binary packages to a temp dir
# then copy over to /gh/pytan/lib/libs_external/win
pip install --no-deps cryptography cffi pyreadline --target win

# from linux system, use pip to install binary packages to a temp dir
# then copy over to /gh/pytan/lib/libs_external/nix
pip install --no-deps cryptography cffi --target nix
