# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: terra/market/v1beta1/market.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='terra/market/v1beta1/market.proto',
  package='terra.market.v1beta1',
  syntax='proto3',
  serialized_options=b'Z*github.com/terra-money/core/x/market/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!terra/market/v1beta1/market.proto\x12\x14terra.market.v1beta1\x1a\x14gogoproto/gogo.proto\"\x95\x02\n\x06Params\x12U\n\tbase_pool\x18\x01 \x01(\x0c\x42\x42\xf2\xde\x1f\x10yaml:\"base_pool\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12=\n\x14pool_recovery_period\x18\x02 \x01(\x04\x42\x1f\xf2\xde\x1f\x1byaml:\"pool_recovery_period\"\x12k\n\x14min_stability_spread\x18\x03 \x01(\x0c\x42M\xf2\xde\x1f\x1byaml:\"min_stability_spread\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x01\x98\xa0\x1f\x00\x42,Z*github.com/terra-money/core/x/market/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='terra.market.v1beta1.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_pool', full_name='terra.market.v1beta1.Params.base_pool', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\020yaml:\"base_pool\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pool_recovery_period', full_name='terra.market.v1beta1.Params.pool_recovery_period', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\033yaml:\"pool_recovery_period\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_stability_spread', full_name='terra.market.v1beta1.Params.min_stability_spread', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\033yaml:\"min_stability_spread\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\001\230\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=359,
)

DESCRIPTOR.message_types_by_name['Params'] = _PARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'terra.market.v1beta1.market_pb2'
  # @@protoc_insertion_point(class_scope:terra.market.v1beta1.Params)
  })
_sym_db.RegisterMessage(Params)


DESCRIPTOR._options = None
_PARAMS.fields_by_name['base_pool']._options = None
_PARAMS.fields_by_name['pool_recovery_period']._options = None
_PARAMS.fields_by_name['min_stability_spread']._options = None
_PARAMS._options = None
# @@protoc_insertion_point(module_scope)
