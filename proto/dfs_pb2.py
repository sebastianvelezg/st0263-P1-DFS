# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dfs.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tdfs.proto\x12\x05\x66iles\"\x0e\n\x0c\x45mptyMessage\"\x1f\n\rStatusMessage\x12\x0e\n\x06status\x18\x01 \x01(\x05\" \n\x11PingFilesResponse\x12\x0b\n\x03\x61\x63k\x18\x01 \x01(\t\"2\n\x11ListFilesResponse\x12\r\n\x05\x66iles\x18\x01 \x03(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\"#\n\x0f\x46indFileRequest\x12\x10\n\x08\x66ileName\x18\x01 \x01(\t\"9\n\x10\x46indFileResponse\x12\x15\n\rnodeAddresses\x18\x01 \x03(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\"\'\n\x13\x44ownloadFileRequest\x12\x10\n\x08\x66ileName\x18\x01 \x01(\t\"*\n\x14\x44ownloadFileResponse\x12\x12\n\nchunk_data\x18\x01 \x01(\x0c\"H\n\x11UploadFileRequest\x12\x12\n\x08\x66ileName\x18\x01 \x01(\tH\x00\x12\x14\n\nchunk_data\x18\x02 \x01(\x0cH\x00\x42\t\n\x07request\".\n\x0fNameNodeRequest\x12\x0c\n\x04\x63onn\x18\x01 \x01(\t\x12\r\n\x05\x66iles\x18\x02 \x03(\t\"1\n\x10\x44\x61taNodeResponse\x12\r\n\x05\x63onns\x18\x01 \x03(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\x32\x93\x04\n\x03\x64\x66s\x12:\n\tPingFiles\x12\x13.files.EmptyMessage\x1a\x18.files.PingFilesResponse\x12:\n\tListFiles\x12\x13.files.EmptyMessage\x1a\x18.files.ListFilesResponse\x12I\n\x0c\x44ownloadFile\x12\x1a.files.DownloadFileRequest\x1a\x1b.files.DownloadFileResponse0\x01\x12=\n\nUploadFile\x12\x18.files.UploadFileRequest\x1a\x13.files.EmptyMessage(\x01\x12<\n\x0cNamenodeConn\x12\x16.files.NameNodeRequest\x1a\x14.files.StatusMessage\x12K\n\x14NamenodeDownloadFile\x12\x1a.files.DownloadFileRequest\x1a\x17.files.DataNodeResponse\x12\x42\n\x12NamenodeUploadFile\x12\x13.files.EmptyMessage\x1a\x17.files.DataNodeResponse\x12;\n\x08\x46indFile\x12\x16.files.FindFileRequest\x1a\x17.files.FindFileResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dfs_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EMPTYMESSAGE']._serialized_start=20
  _globals['_EMPTYMESSAGE']._serialized_end=34
  _globals['_STATUSMESSAGE']._serialized_start=36
  _globals['_STATUSMESSAGE']._serialized_end=67
  _globals['_PINGFILESRESPONSE']._serialized_start=69
  _globals['_PINGFILESRESPONSE']._serialized_end=101
  _globals['_LISTFILESRESPONSE']._serialized_start=103
  _globals['_LISTFILESRESPONSE']._serialized_end=153
  _globals['_FINDFILEREQUEST']._serialized_start=155
  _globals['_FINDFILEREQUEST']._serialized_end=190
  _globals['_FINDFILERESPONSE']._serialized_start=192
  _globals['_FINDFILERESPONSE']._serialized_end=249
  _globals['_DOWNLOADFILEREQUEST']._serialized_start=251
  _globals['_DOWNLOADFILEREQUEST']._serialized_end=290
  _globals['_DOWNLOADFILERESPONSE']._serialized_start=292
  _globals['_DOWNLOADFILERESPONSE']._serialized_end=334
  _globals['_UPLOADFILEREQUEST']._serialized_start=336
  _globals['_UPLOADFILEREQUEST']._serialized_end=408
  _globals['_NAMENODEREQUEST']._serialized_start=410
  _globals['_NAMENODEREQUEST']._serialized_end=456
  _globals['_DATANODERESPONSE']._serialized_start=458
  _globals['_DATANODERESPONSE']._serialized_end=507
  _globals['_DFS']._serialized_start=510
  _globals['_DFS']._serialized_end=1041
# @@protoc_insertion_point(module_scope)