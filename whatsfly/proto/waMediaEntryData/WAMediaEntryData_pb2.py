# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: waMediaEntryData/WAMediaEntryData.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'waMediaEntryData/WAMediaEntryData.proto\x12\x10WAMediaEntryData\"\xc9\x05\n\nMediaEntry\x12\x12\n\nfileSHA256\x18\x01 \x01(\x0c\x12\x10\n\x08mediaKey\x18\x02 \x01(\x0c\x12\x15\n\rfileEncSHA256\x18\x03 \x01(\x0c\x12\x12\n\ndirectPath\x18\x04 \x01(\t\x12\x19\n\x11mediaKeyTimestamp\x18\x05 \x01(\x03\x12\x17\n\x0fserverMediaType\x18\x06 \x01(\t\x12\x13\n\x0buploadToken\x18\x07 \x01(\x0c\x12\x1a\n\x12validatedTimestamp\x18\x08 \x01(\x0c\x12\x0f\n\x07sidecar\x18\t \x01(\x0c\x12\x10\n\x08objectID\x18\n \x01(\t\x12\x0c\n\x04\x46\x42ID\x18\x0b \x01(\t\x12Q\n\x15\x64ownloadableThumbnail\x18\x0c \x01(\x0b\x32\x32.WAMediaEntryData.MediaEntry.DownloadableThumbnail\x12\x0e\n\x06handle\x18\r \x01(\t\x12\x10\n\x08\x66ilename\x18\x0e \x01(\t\x12S\n\x16progressiveJPEGDetails\x18\x0f \x01(\x0b\x32\x33.WAMediaEntryData.MediaEntry.ProgressiveJpegDetails\x12\x0c\n\x04size\x18\x10 \x01(\x03\x12$\n\x1clastDownloadAttemptTimestamp\x18\x11 \x01(\x03\x1a>\n\x16ProgressiveJpegDetails\x12\x13\n\x0bscanLengths\x18\x01 \x03(\r\x12\x0f\n\x07sidecar\x18\x02 \x01(\x0c\x1a\x95\x01\n\x15\x44ownloadableThumbnail\x12\x12\n\nfileSHA256\x18\x01 \x01(\x0c\x12\x15\n\rfileEncSHA256\x18\x02 \x01(\x0c\x12\x12\n\ndirectPath\x18\x03 \x01(\t\x12\x10\n\x08mediaKey\x18\x04 \x01(\x0c\x12\x19\n\x11mediaKeyTimestamp\x18\x05 \x01(\x03\x12\x10\n\x08objectID\x18\x06 \x01(\tB,Z*go.mau.fi/whatsmeow/proto/waMediaEntryData')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'waMediaEntryData.WAMediaEntryData_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z*go.mau.fi/whatsmeow/proto/waMediaEntryData'
  _MEDIAENTRY._serialized_start=62
  _MEDIAENTRY._serialized_end=775
  _MEDIAENTRY_PROGRESSIVEJPEGDETAILS._serialized_start=561
  _MEDIAENTRY_PROGRESSIVEJPEGDETAILS._serialized_end=623
  _MEDIAENTRY_DOWNLOADABLETHUMBNAIL._serialized_start=626
  _MEDIAENTRY_DOWNLOADABLETHUMBNAIL._serialized_end=775
# @@protoc_insertion_point(module_scope)