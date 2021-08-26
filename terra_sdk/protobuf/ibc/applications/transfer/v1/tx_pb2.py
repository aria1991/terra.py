# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/transfer/v1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ibc/applications/transfer/v1/tx.proto',
  package='ibc.applications.transfer.v1',
  syntax='proto3',
  serialized_options=b'Z4github.com/cosmos/ibc-go/modules/apps/transfer/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%ibc/applications/transfer/v1/tx.proto\x12\x1cibc.applications.transfer.v1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1fibc/core/client/v1/client.proto\"\xd5\x02\n\x0bMsgTransfer\x12+\n\x0bsource_port\x18\x01 \x01(\tB\x16\xf2\xde\x1f\x12yaml:\"source_port\"\x12\x31\n\x0esource_channel\x18\x02 \x01(\tB\x19\xf2\xde\x1f\x15yaml:\"source_channel\"\x12.\n\x05token\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x0e\n\x06sender\x18\x04 \x01(\t\x12\x10\n\x08receiver\x18\x05 \x01(\t\x12Q\n\x0etimeout_height\x18\x06 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x1d\xf2\xde\x1f\x15yaml:\"timeout_height\"\xc8\xde\x1f\x00\x12\x37\n\x11timeout_timestamp\x18\x07 \x01(\x04\x42\x1c\xf2\xde\x1f\x18yaml:\"timeout_timestamp\":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x15\n\x13MsgTransferResponse2o\n\x03Msg\x12h\n\x08Transfer\x12).ibc.applications.transfer.v1.MsgTransfer\x1a\x31.ibc.applications.transfer.v1.MsgTransferResponseB6Z4github.com/cosmos/ibc-go/modules/apps/transfer/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,ibc_dot_core_dot_client_dot_v1_dot_client__pb2.DESCRIPTOR,])




_MSGTRANSFER = _descriptor.Descriptor(
  name='MsgTransfer',
  full_name='ibc.applications.transfer.v1.MsgTransfer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_port', full_name='ibc.applications.transfer.v1.MsgTransfer.source_port', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\022yaml:\"source_port\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_channel', full_name='ibc.applications.transfer.v1.MsgTransfer.source_channel', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\025yaml:\"source_channel\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='ibc.applications.transfer.v1.MsgTransfer.token', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sender', full_name='ibc.applications.transfer.v1.MsgTransfer.sender', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receiver', full_name='ibc.applications.transfer.v1.MsgTransfer.receiver', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeout_height', full_name='ibc.applications.transfer.v1.MsgTransfer.timeout_height', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\025yaml:\"timeout_height\"\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeout_timestamp', full_name='ibc.applications.transfer.v1.MsgTransfer.timeout_timestamp', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\030yaml:\"timeout_timestamp\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=159,
  serialized_end=500,
)


_MSGTRANSFERRESPONSE = _descriptor.Descriptor(
  name='MsgTransferResponse',
  full_name='ibc.applications.transfer.v1.MsgTransferResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=502,
  serialized_end=523,
)

_MSGTRANSFER.fields_by_name['token'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_MSGTRANSFER.fields_by_name['timeout_height'].message_type = ibc_dot_core_dot_client_dot_v1_dot_client__pb2._HEIGHT
DESCRIPTOR.message_types_by_name['MsgTransfer'] = _MSGTRANSFER
DESCRIPTOR.message_types_by_name['MsgTransferResponse'] = _MSGTRANSFERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgTransfer = _reflection.GeneratedProtocolMessageType('MsgTransfer', (_message.Message,), {
  'DESCRIPTOR' : _MSGTRANSFER,
  '__module__' : 'ibc.applications.transfer.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.transfer.v1.MsgTransfer)
  })
_sym_db.RegisterMessage(MsgTransfer)

MsgTransferResponse = _reflection.GeneratedProtocolMessageType('MsgTransferResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGTRANSFERRESPONSE,
  '__module__' : 'ibc.applications.transfer.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.transfer.v1.MsgTransferResponse)
  })
_sym_db.RegisterMessage(MsgTransferResponse)


DESCRIPTOR._options = None
_MSGTRANSFER.fields_by_name['source_port']._options = None
_MSGTRANSFER.fields_by_name['source_channel']._options = None
_MSGTRANSFER.fields_by_name['token']._options = None
_MSGTRANSFER.fields_by_name['timeout_height']._options = None
_MSGTRANSFER.fields_by_name['timeout_timestamp']._options = None
_MSGTRANSFER._options = None

_MSG = _descriptor.ServiceDescriptor(
  name='Msg',
  full_name='ibc.applications.transfer.v1.Msg',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=525,
  serialized_end=636,
  methods=[
  _descriptor.MethodDescriptor(
    name='Transfer',
    full_name='ibc.applications.transfer.v1.Msg.Transfer',
    index=0,
    containing_service=None,
    input_type=_MSGTRANSFER,
    output_type=_MSGTRANSFERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MSG)

DESCRIPTOR.services_by_name['Msg'] = _MSG

# @@protoc_insertion_point(module_scope)
