# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: greeting.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0egreeting.proto\x12\x08tutorial\"\x1f\n\x0fGreetingRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"$\n\x10GreetingResponse\x12\x10\n\x08greeting\x18\x01 \x01(\t2\x8c\x01\n\x07Greeter\x12>\n\x05Greet\x12\x19.tutorial.GreetingRequest\x1a\x1a.tutorial.GreetingResponse\x12\x41\n\x04\x43hat\x12\x19.tutorial.GreetingRequest\x1a\x1a.tutorial.GreetingResponse(\x01\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'greeting_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GREETINGREQUEST._serialized_start=28
  _GREETINGREQUEST._serialized_end=59
  _GREETINGRESPONSE._serialized_start=61
  _GREETINGRESPONSE._serialized_end=97
  _GREETER._serialized_start=100
  _GREETER._serialized_end=240
# @@protoc_insertion_point(module_scope)
