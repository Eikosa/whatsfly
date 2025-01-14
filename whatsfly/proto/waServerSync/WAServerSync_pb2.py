# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: waServerSync/WAServerSync.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fwaServerSync/WAServerSync.proto\x12\x0cWAServerSync\"\xa0\x01\n\rSyncdMutation\x12=\n\toperation\x18\x01 \x01(\x0e\x32*.WAServerSync.SyncdMutation.SyncdOperation\x12)\n\x06record\x18\x02 \x01(\x0b\x32\x19.WAServerSync.SyncdRecord\"%\n\x0eSyncdOperation\x12\x07\n\x03SET\x10\x00\x12\n\n\x06REMOVE\x10\x01\"\x1f\n\x0cSyncdVersion\x12\x0f\n\x07version\x18\x01 \x01(\x04\"&\n\x08\x45xitCode\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x04\x12\x0c\n\x04text\x18\x02 \x01(\t\"\x1a\n\nSyncdIndex\x12\x0c\n\x04\x62lob\x18\x01 \x01(\x0c\"\x1a\n\nSyncdValue\x12\x0c\n\x04\x62lob\x18\x01 \x01(\x0c\"\x13\n\x05KeyId\x12\n\n\x02ID\x18\x01 \x01(\x0c\"\x83\x01\n\x0bSyncdRecord\x12\'\n\x05index\x18\x01 \x01(\x0b\x32\x18.WAServerSync.SyncdIndex\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.WAServerSync.SyncdValue\x12\"\n\x05keyID\x18\x03 \x01(\x0b\x32\x13.WAServerSync.KeyId\"\x8f\x01\n\x15\x45xternalBlobReference\x12\x10\n\x08mediaKey\x18\x01 \x01(\x0c\x12\x12\n\ndirectPath\x18\x02 \x01(\t\x12\x0e\n\x06handle\x18\x03 \x01(\t\x12\x15\n\rfileSizeBytes\x18\x04 \x01(\x04\x12\x12\n\nfileSHA256\x18\x05 \x01(\x0c\x12\x15\n\rfileEncSHA256\x18\x06 \x01(\x0c\"\x99\x01\n\rSyncdSnapshot\x12+\n\x07version\x18\x01 \x01(\x0b\x32\x1a.WAServerSync.SyncdVersion\x12*\n\x07records\x18\x02 \x03(\x0b\x32\x19.WAServerSync.SyncdRecord\x12\x0b\n\x03mac\x18\x03 \x01(\x0c\x12\"\n\x05keyID\x18\x04 \x01(\x0b\x32\x13.WAServerSync.KeyId\"@\n\x0eSyncdMutations\x12.\n\tmutations\x18\x01 \x03(\x0b\x32\x1b.WAServerSync.SyncdMutation\"\xcc\x02\n\nSyncdPatch\x12+\n\x07version\x18\x01 \x01(\x0b\x32\x1a.WAServerSync.SyncdVersion\x12.\n\tmutations\x18\x02 \x03(\x0b\x32\x1b.WAServerSync.SyncdMutation\x12>\n\x11\x65xternalMutations\x18\x03 \x01(\x0b\x32#.WAServerSync.ExternalBlobReference\x12\x13\n\x0bsnapshotMAC\x18\x04 \x01(\x0c\x12\x10\n\x08patchMAC\x18\x05 \x01(\x0c\x12\"\n\x05keyID\x18\x06 \x01(\x0b\x32\x13.WAServerSync.KeyId\x12(\n\x08\x65xitCode\x18\x07 \x01(\x0b\x32\x16.WAServerSync.ExitCode\x12\x13\n\x0b\x64\x65viceIndex\x18\x08 \x01(\r\x12\x17\n\x0f\x63lientDebugData\x18\t \x01(\x0c\x42(Z&go.mau.fi/whatsmeow/proto/waServerSync')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'waServerSync.WAServerSync_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z&go.mau.fi/whatsmeow/proto/waServerSync'
  _SYNCDMUTATION._serialized_start=50
  _SYNCDMUTATION._serialized_end=210
  _SYNCDMUTATION_SYNCDOPERATION._serialized_start=173
  _SYNCDMUTATION_SYNCDOPERATION._serialized_end=210
  _SYNCDVERSION._serialized_start=212
  _SYNCDVERSION._serialized_end=243
  _EXITCODE._serialized_start=245
  _EXITCODE._serialized_end=283
  _SYNCDINDEX._serialized_start=285
  _SYNCDINDEX._serialized_end=311
  _SYNCDVALUE._serialized_start=313
  _SYNCDVALUE._serialized_end=339
  _KEYID._serialized_start=341
  _KEYID._serialized_end=360
  _SYNCDRECORD._serialized_start=363
  _SYNCDRECORD._serialized_end=494
  _EXTERNALBLOBREFERENCE._serialized_start=497
  _EXTERNALBLOBREFERENCE._serialized_end=640
  _SYNCDSNAPSHOT._serialized_start=643
  _SYNCDSNAPSHOT._serialized_end=796
  _SYNCDMUTATIONS._serialized_start=798
  _SYNCDMUTATIONS._serialized_end=862
  _SYNCDPATCH._serialized_start=865
  _SYNCDPATCH._serialized_end=1197
# @@protoc_insertion_point(module_scope)
