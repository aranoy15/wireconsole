# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (Qt v5.12.1)
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x01\x5f\
\x00\
\x00\x11\xa5\x78\x9c\xd5\xd7\xbd\x6e\x83\x30\x14\x05\xe0\x3d\x4f\
\x61\x31\x33\x70\xcf\x85\xfc\xf4\x39\xba\x55\x1d\x90\xc2\x90\xa1\
\xa9\xd4\x50\x75\x88\xf2\xee\xa1\x54\x4a\x42\xb1\x7c\x54\xf9\x30\
\x94\x09\x7c\x65\x1f\x24\xfb\x03\xfb\xbc\x0a\xc3\x55\xec\xdb\xbe\
\x2d\x9e\xc2\xcb\xf8\xf4\x7d\x9d\x6f\x77\x63\xfd\xb0\x1f\xaa\x55\
\x39\x6d\x3c\xb6\x6f\xdd\xd0\x5c\x3c\x77\xa7\xde\x8a\x5f\xc5\xaf\
\xc3\x47\x77\x9a\x0c\x19\x1f\xfa\xd6\xe1\xfd\xb3\x9f\x67\xdc\x5f\
\xe0\x38\x0e\x66\xaf\xb3\xf2\x65\xde\x23\x99\xe0\xe9\x84\xaa\x0c\
\x9e\x1f\x52\xa7\x43\x90\x9f\xb0\x4e\x27\xd4\x65\x68\xca\xb0\x89\
\xe4\x4c\x5a\xee\xf5\x87\xfc\xd8\xdc\x5b\x62\xee\xf1\x6f\xe6\xde\
\x16\x4f\xc0\xe2\x13\x4f\xd6\xef\xf2\x8b\xb7\xce\x4f\x68\xd2\x09\
\xcd\xe2\x3c\xd6\xf9\x09\x9b\x74\x42\x8c\xde\x1f\x13\xb6\xe9\x84\
\x6d\x7e\xc2\x2e\x9d\xb0\x13\x88\x63\xa8\x2b\x41\x06\x63\xad\xf8\
\x72\x10\xd8\x26\x90\x6d\x84\xb6\x09\x6c\x1b\xc1\x6d\x02\xdd\x46\
\x78\x9b\xc0\xb7\x11\xe0\x26\x10\x6e\x84\xb8\x09\x8c\x1b\x41\x6e\
\x02\xe5\x46\x98\x9b\xc0\x39\x88\x73\x08\x9c\x83\x38\x87\xe2\xff\
\xcd\x7e\xe0\x02\xe7\x20\xce\x21\x70\x0e\xb6\x03\x15\x38\x07\x71\
\x0e\x81\x73\x10\xe7\x10\x38\x07\x71\x0e\x81\x73\x10\xe7\x10\x38\
\x07\x71\x0e\x81\x73\x27\xce\x5d\xe0\xdc\x89\x73\x57\x9c\x02\x89\
\x73\x57\xec\xd4\xd9\x56\x5d\xe0\xdc\x89\x73\x17\x38\x77\xe2\xdc\
\x05\xce\x9d\x38\x77\x81\x73\x27\xce\x5d\xe0\xdc\x89\x73\x8f\x39\
\x9f\xb4\x3c\x1c\xc9\x57\x3f\xcf\x97\x2b\x8c\xa5\xd0\xab\
"

qt_resource_name = b"\
\x00\x0d\
\x00\x0d\xff\x5e\
\x00\x74\
\x00\x65\x00\x6d\x00\x70\x00\x6c\x00\x61\x00\x74\x00\x65\x00\x2e\x00\x6a\x00\x73\x00\x6f\x00\x6e\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x6b\x98\xb3\x03\xbf\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
