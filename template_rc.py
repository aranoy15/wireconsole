# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (Qt v5.12.1)
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x00\xb4\
\x00\
\x00\x05\xa1\x78\x9c\xab\xe6\x52\x00\x02\xa5\x94\xc4\x92\x44\x25\
\x2b\x85\x68\x30\x0f\x04\xaa\xe1\x2c\xb0\x7c\x66\x0a\x50\xd6\x40\
\x07\x55\x30\x2f\x31\x37\x15\x28\xac\x14\x92\x5a\x5c\x62\xa8\x84\
\x26\x59\x9e\x59\x94\x5a\x8c\x62\x24\x76\xa3\xe1\x1a\xf2\x4b\x4b\
\x30\xed\x40\x38\x20\x0f\x6c\x98\x61\x2c\x86\x74\x2d\xa6\x0e\xbc\
\x36\x18\xe3\xb7\xc1\x40\x47\xc1\x98\x72\x4b\x4c\xf0\x5b\x62\x44\
\xb9\x0d\x66\xf8\x6d\x30\xd1\x51\x30\xd5\x51\x30\xc7\x62\x0f\x8a\
\x08\x42\x1e\xc9\x7e\x6c\x71\x6f\x88\x27\xee\x8d\x46\xe3\x1e\xd9\
\x92\x41\x12\xf7\x66\x94\xdb\x63\x8e\xdf\x1e\x73\x1d\x05\x0b\x1d\
\x05\x4b\xca\xed\xb1\xc0\x6f\x8f\x05\xe5\x36\x58\xd2\x3c\x4e\x0c\
\x09\xa4\x5e\x4b\x1d\xa0\x12\x12\xb2\x23\x17\x84\x5f\x0b\x00\x73\
\xa1\xe9\x41\
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
\x00\x00\x01\x6b\x93\x93\xde\x21\
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