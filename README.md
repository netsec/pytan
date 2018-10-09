<!-- MarkdownTOC -->

- [PyTan](#pytan)
  - [What is it?](#what-is-it)
  - [Versions](#versions)
  - [Documentation Links](#documentation-links)
  - [Quick Install Instructions](#quick-install-instructions)
  - [Release strategy](#release-strategy)
  - [Package Info](#package-info)

<!-- /MarkdownTOC -->

# PyTan

## What is it?

This is a set of packages and scripts that provide a simple way for interfacing with the [Tanium](https://www.tanium.com/) SOAP API using python or the command line.

## Versions
 * **2.2.3 (Oct 9 2018)** [Release Link](https://github.com/tanium/pytan/releases/tag/2.2.3)

## Documentation Links

Documentation is only generated for major releases!

* Online documentation for PyTan 2.1.6:
  * [HTML: Main Index](http://tanium.github.io/pytan)
  * [HTML: PyTan API Examples](http://tanium.github.io/pytan/examples/pytan_examples.html)
  * [HTML: PyTan Command Line Usage](http://tanium.github.io/pytan/_static/bin_doc/index.html)
  * [PDF: Standalone PDF version of HTML](http://tanium.github.io/pytan/PyTan-2.1.6.pdf)
* Offline documentation for PyTan 2.1.6:
  * [Zipped HTML documentation for PyTan 2.1.6](doc/html/PyTan-2.1.6-HTML_DOC.zip)
  * [PDF documentation for PyTan 2.1.6](doc/pdf/PyTan-2.1.6.pdf)
* Other documentation:
  * [Change Log for PyTan](CHANGELOG.md)
  * [To Do List for PyTan](TODO.md)

## Quick Install Instructions 

* First, download PyTan using your browser by browsing to: https://github.com/tanium/pytan/releases/latest and choosing one of the Downloads (zip or tar.gz)
* Then refer to the OS specific instructions below to proceed.
* Additional information on installation can be found in the [documentation](http://tanium.github.io/pytan/introduction.html#installation)

### Mac OSX
* Create a new directory for storing PyTan:
```
mkdir ~/tanium
```
* Extract the PyTan ZIP file you downloaded to ~/tanium:
```
cd ~/tanium
unzip pytan-2.2.2.zip
```
* Verify that your OSX install has Python 2.7.x installed and that your PYTHONPATH points to 2.7.x:
```
python -V
python -c “import sys; print sys.path”
```

### Linux

* Create a new directory for storing PyTan:
```
mkdir ~/tanium
```
* Extract the PyTan ZIP file you downloaded to ~/tanium:
```
cd ~/tanium
unzip pytan-2.2.2.zip
```
* Verify that your linux distribution has Python 2.7.x installed and that your PYTHONPATH points to 2.7.x:
```
python -V
python -c “import sys; print sys.path”
```

### Windows

* Create a new directory for storing PyTan:
```
mkdir c:\tanium
```
* Extract the PyTan ZIP file you downloaded to C:\tanium
* Install Python 2.7.10:
  * Using your browser, download Python 2.7.10 from: https://www.python.org/downloads/release/python-2710/
  * Run the Python 2.7.10 installer
  * On the __Customize Python__ section of the installer select, 
'Add Python.exe to Path' to allow you to run Python from cmd shell without absolute path
  * Accept all other defaults for the installer
   
## Release strategy

* The current stable version will always be maintained in the master branch. 
* Unstable and development versions can be accessed via the develop branch.
* Full regression tests will be performed every major (x.0.0) or minor (0.x.0) release of PyTan
* All documentation and API examples will be rebuilt every major (x.0.0) or minor (0.x.0) release of PyTan
* Revision releases (0.0.x) will only be tested against the latest stable release of Tanium for each minor build (6.2.314.xxxx, 6.5.314.xxxx, etc.)

## Package Info

* Author and Maintainer: Jim Olsen (jim.olsen@tanium.com)
* License: MIT
* Copyright: Tanium Inc. 2017
