# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: filesystem.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import permissions_pb2 as permissions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x66ilesystem.proto\x12\nfilesystem\x1a\x1bgoogle/protobuf/empty.proto\x1a\x11permissions.proto\"e\n\x11\x43reateFileRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x16\n\x0e\x63reate_parents\x18\x02 \x01(\x08\x12*\n\x06\x61\x63\x63\x65ss\x18\x03 \x01(\x0b\x32\x1a.permissions.AccessControl\"p\n\x0eMakeDirRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x16\n\x0e\x63reate_parents\x18\x02 \x01(\x08\x12\x0c\n\x04mode\x18\x03 \x01(\r\x12*\n\x06\x61\x63\x63\x65ss\x18\x04 \x01(\x0b\x32\x1a.permissions.AccessControl\"d\n\x11\x43reateLinkRequest\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x02 \x01(\t\x12*\n\x06\x61\x63\x63\x65ss\x18\x03 \x01(\x0b\x32\x1a.permissions.AccessControl\"g\n\x14\x43reateSymlinkRequest\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x02 \x01(\t\x12*\n\x06\x61\x63\x63\x65ss\x18\x03 \x01(\x0b\x32\x1a.permissions.AccessControl\"q\n\x0b\x43opyRequest\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x02 \x01(\t\x12\x11\n\trecursive\x18\x03 \x01(\x08\x12*\n\x06\x61\x63\x63\x65ss\x18\x04 \x01(\x0b\x32\x1a.permissions.AccessControl\"V\n\x0c\x43hmodRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0c\n\x04mode\x18\x02 \x01(\r\x12*\n\x06\x61\x63\x63\x65ss\x18\x03 \x01(\x0b\x32\x1a.permissions.AccessControl\"b\n\x0c\x43hownRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0b\n\x03uid\x18\x02 \x01(\r\x12\x0b\n\x03gid\x18\x03 \x01(\r\x12*\n\x06\x61\x63\x63\x65ss\x18\x04 \x01(\x0b\x32\x1a.permissions.AccessControl\"\x8b\x01\n\x0fReadFileRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x13\n\x06offset\x18\x03 \x01(\x04H\x00\x88\x01\x01\x12\x13\n\x06length\x18\x04 \x01(\x04H\x01\x88\x01\x01\x12*\n\x06\x61\x63\x63\x65ss\x18\x05 \x01(\x0b\x32\x1a.permissions.AccessControlB\t\n\x07_offsetB\t\n\x07_length\" \n\x10ReadFileResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"G\n\x0bStatRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12*\n\x06\x61\x63\x63\x65ss\x18\x02 \x01(\x0b\x32\x1a.permissions.AccessControl\"4\n\x0cStatResponse\x12$\n\x05\x65ntry\x18\x01 \x01(\x0b\x32\x15.filesystem.EntryInfo\"\xc8\x01\n\x10WriteFileRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x1c\n\x14\x63reate_if_not_exists\x18\x03 \x01(\x08\x12\x0e\n\x06\x61ppend\x18\x04 \x01(\x08\x12\x13\n\x06offset\x18\x05 \x01(\x04H\x00\x88\x01\x01\x12\x13\n\x06length\x18\x06 \x01(\x04H\x01\x88\x01\x01\x12*\n\x06\x61\x63\x63\x65ss\x18\x07 \x01(\x0b\x32\x1a.permissions.AccessControlB\t\n\x07_offsetB\t\n\x07_length\"V\n\rRemoveRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0b\n\x03\x61ll\x18\x02 \x01(\x08\x12*\n\x06\x61\x63\x63\x65ss\x18\x03 \x01(\x0b\x32\x1a.permissions.AccessControl\"^\n\x0bMoveRequest\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x02 \x01(\t\x12*\n\x06\x61\x63\x63\x65ss\x18\x03 \x01(\x0b\x32\x1a.permissions.AccessControl\"\x9b\x01\n\tEntryInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\"\n\x04type\x18\x02 \x01(\x0e\x32\x14.filesystem.FileType\x12\x0c\n\x04mode\x18\x03 \x01(\r\x12\x0c\n\x04size\x18\x04 \x01(\x04\x12\x15\n\rlast_modified\x18\x05 \x01(\x04\x12)\n\x05owner\x18\x06 \x01(\x0b\x32\x1a.permissions.AccessControl\"J\n\x0eReadDirRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12*\n\x06\x61\x63\x63\x65ss\x18\x02 \x01(\x0b\x32\x1a.permissions.AccessControl\"9\n\x0fReadDirResponse\x12&\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x15.filesystem.EntryInfo\"H\n\x0cWatchRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12*\n\x06\x61\x63\x63\x65ss\x18\x02 \x01(\x0b\x32\x1a.permissions.AccessControl\"j\n\x0f\x46ilesystemEvent\x12\x0c\n\x04path\x18\x01 \x01(\t\x12#\n\x04type\x18\x02 \x01(\x0e\x32\x15.filesystem.EventType\x12$\n\x05\x65ntry\x18\x03 \x01(\x0b\x32\x15.filesystem.EntryInfo*P\n\x08\x46ileType\x12\x14\n\x10UNKNOWN_FileType\x10\x00\x12\x08\n\x04\x46ILE\x10\x01\x12\r\n\tDIRECTORY\x10\x02\x12\x08\n\x04LINK\x10\x03\x12\x0b\n\x07SYMLINK\x10\x04*\\\n\tEventType\x12\x15\n\x11UNKNOWN_EventType\x10\x00\x12\n\n\x06\x43REATE\x10\x01\x12\t\n\x05WRITE\x10\x02\x12\n\n\x06REMOVE\x10\x03\x12\n\n\x06RENAME\x10\x04\x12\t\n\x05\x43HMOD\x10\x05\x32\x94\x07\n\nFilesystem\x12\x39\n\x04Stat\x12\x17.filesystem.StatRequest\x1a\x18.filesystem.StatResponse\x12\x43\n\nCreateFile\x12\x1d.filesystem.CreateFileRequest\x1a\x16.google.protobuf.Empty\x12G\n\x08ReadFile\x12\x1b.filesystem.ReadFileRequest\x1a\x1c.filesystem.ReadFileResponse0\x01\x12\x41\n\tWriteFile\x12\x1c.filesystem.WriteFileRequest\x1a\x16.google.protobuf.Empty\x12=\n\x07MakeDir\x12\x1a.filesystem.MakeDirRequest\x1a\x16.google.protobuf.Empty\x12\x42\n\x07ReadDir\x12\x1a.filesystem.ReadDirRequest\x1a\x1b.filesystem.ReadDirResponse\x12\x43\n\nCreateLink\x12\x1d.filesystem.CreateLinkRequest\x1a\x16.google.protobuf.Empty\x12I\n\rCreateSymlink\x12 .filesystem.CreateSymlinkRequest\x1a\x16.google.protobuf.Empty\x12@\n\x05Watch\x12\x18.filesystem.WatchRequest\x1a\x1b.filesystem.FilesystemEvent0\x01\x12\x39\n\x06Rename\x12\x17.filesystem.MoveRequest\x1a\x16.google.protobuf.Empty\x12;\n\x06Remove\x12\x19.filesystem.RemoveRequest\x1a\x16.google.protobuf.Empty\x12\x39\n\x05\x43hmod\x12\x18.filesystem.ChmodRequest\x1a\x16.google.protobuf.Empty\x12\x39\n\x05\x43hown\x12\x18.filesystem.ChownRequest\x1a\x16.google.protobuf.Empty\x12\x37\n\x04\x43opy\x12\x17.filesystem.CopyRequest\x1a\x16.google.protobuf.EmptyB-Z+github.com/e2b-dev/infra/packages/envd/specb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'filesystem_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z+github.com/e2b-dev/infra/packages/envd/spec'
  _globals['_FILETYPE']._serialized_start=1972
  _globals['_FILETYPE']._serialized_end=2052
  _globals['_EVENTTYPE']._serialized_start=2054
  _globals['_EVENTTYPE']._serialized_end=2146
  _globals['_CREATEFILEREQUEST']._serialized_start=80
  _globals['_CREATEFILEREQUEST']._serialized_end=181
  _globals['_MAKEDIRREQUEST']._serialized_start=183
  _globals['_MAKEDIRREQUEST']._serialized_end=295
  _globals['_CREATELINKREQUEST']._serialized_start=297
  _globals['_CREATELINKREQUEST']._serialized_end=397
  _globals['_CREATESYMLINKREQUEST']._serialized_start=399
  _globals['_CREATESYMLINKREQUEST']._serialized_end=502
  _globals['_COPYREQUEST']._serialized_start=504
  _globals['_COPYREQUEST']._serialized_end=617
  _globals['_CHMODREQUEST']._serialized_start=619
  _globals['_CHMODREQUEST']._serialized_end=705
  _globals['_CHOWNREQUEST']._serialized_start=707
  _globals['_CHOWNREQUEST']._serialized_end=805
  _globals['_READFILEREQUEST']._serialized_start=808
  _globals['_READFILEREQUEST']._serialized_end=947
  _globals['_READFILERESPONSE']._serialized_start=949
  _globals['_READFILERESPONSE']._serialized_end=981
  _globals['_STATREQUEST']._serialized_start=983
  _globals['_STATREQUEST']._serialized_end=1054
  _globals['_STATRESPONSE']._serialized_start=1056
  _globals['_STATRESPONSE']._serialized_end=1108
  _globals['_WRITEFILEREQUEST']._serialized_start=1111
  _globals['_WRITEFILEREQUEST']._serialized_end=1311
  _globals['_REMOVEREQUEST']._serialized_start=1313
  _globals['_REMOVEREQUEST']._serialized_end=1399
  _globals['_MOVEREQUEST']._serialized_start=1401
  _globals['_MOVEREQUEST']._serialized_end=1495
  _globals['_ENTRYINFO']._serialized_start=1498
  _globals['_ENTRYINFO']._serialized_end=1653
  _globals['_READDIRREQUEST']._serialized_start=1655
  _globals['_READDIRREQUEST']._serialized_end=1729
  _globals['_READDIRRESPONSE']._serialized_start=1731
  _globals['_READDIRRESPONSE']._serialized_end=1788
  _globals['_WATCHREQUEST']._serialized_start=1790
  _globals['_WATCHREQUEST']._serialized_end=1862
  _globals['_FILESYSTEMEVENT']._serialized_start=1864
  _globals['_FILESYSTEMEVENT']._serialized_end=1970
  _globals['_FILESYSTEM']._serialized_start=2149
  _globals['_FILESYSTEM']._serialized_end=3065
# @@protoc_insertion_point(module_scope)
