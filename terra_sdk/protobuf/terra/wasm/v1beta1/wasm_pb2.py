# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: terra/wasm/v1beta1/wasm.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="terra/wasm/v1beta1/wasm.proto",
    package="terra.wasm.v1beta1",
    syntax="proto3",
    serialized_options=b"Z(github.com/terra-money/core/x/wasm/types",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1dterra/wasm/v1beta1/wasm.proto\x12\x12terra.wasm.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto"\xc3\x01\n\x06Params\x12\x37\n\x11max_contract_size\x18\x01 \x01(\x04\x42\x1c\xf2\xde\x1f\x18yaml:"max_contract_size"\x12\x35\n\x10max_contract_gas\x18\x02 \x01(\x04\x42\x1b\xf2\xde\x1f\x17yaml:"max_contract_gas"\x12?\n\x15max_contract_msg_size\x18\x03 \x01(\x04\x42 \xf2\xde\x1f\x1cyaml:"max_contract_msg_size":\x08\xe8\xa0\x1f\x01\x98\xa0\x1f\x00"\x87\x01\n\x08\x43odeInfo\x12-\n\x07\x63ode_id\x18\x01 \x01(\x04\x42\x1c\xf2\xde\x1f\x0eyaml:"code_id"\xe2\xde\x1f\x06\x43odeID\x12\'\n\tcode_hash\x18\x02 \x01(\x0c\x42\x14\xf2\xde\x1f\x10yaml:"code_hash"\x12#\n\x07\x63reator\x18\x03 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"creator""\xf1\x01\n\x0c\x43ontractInfo\x12#\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12#\n\x07\x63reator\x18\x02 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"creator"\x12\x1f\n\x05\x61\x64min\x18\x03 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"admin"\x12-\n\x07\x63ode_id\x18\x04 \x01(\x04\x42\x1c\xf2\xde\x1f\x0eyaml:"code_id"\xe2\xde\x1f\x06\x43odeID\x12\x41\n\x08init_msg\x18\x05 \x01(\x0c\x42/\xf2\xde\x1f\x0fyaml:"init_msg"\xfa\xde\x1f\x18\x65ncoding/json.RawMessage:\x04\xe8\xa0\x1f\x01\x42*Z(github.com/terra-money/core/x/wasm/typesb\x06proto3',
    dependencies=[
        gogoproto_dot_gogo__pb2.DESCRIPTOR,
        cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,
    ],
)


_PARAMS = _descriptor.Descriptor(
    name="Params",
    full_name="terra.wasm.v1beta1.Params",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="max_contract_size",
            full_name="terra.wasm.v1beta1.Params.max_contract_size",
            index=0,
            number=1,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\030yaml:"max_contract_size"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="max_contract_gas",
            full_name="terra.wasm.v1beta1.Params.max_contract_gas",
            index=1,
            number=2,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\027yaml:"max_contract_gas"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="max_contract_msg_size",
            full_name="terra.wasm.v1beta1.Params.max_contract_msg_size",
            index=2,
            number=3,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\034yaml:"max_contract_msg_size"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\350\240\037\001\230\240\037\000",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=108,
    serialized_end=303,
)


_CODEINFO = _descriptor.Descriptor(
    name="CodeInfo",
    full_name="terra.wasm.v1beta1.CodeInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="code_id",
            full_name="terra.wasm.v1beta1.CodeInfo.code_id",
            index=0,
            number=1,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\016yaml:"code_id"\342\336\037\006CodeID',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="code_hash",
            full_name="terra.wasm.v1beta1.CodeInfo.code_hash",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\020yaml:"code_hash"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="creator",
            full_name="terra.wasm.v1beta1.CodeInfo.creator",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\016yaml:"creator"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=306,
    serialized_end=441,
)


_CONTRACTINFO = _descriptor.Descriptor(
    name="ContractInfo",
    full_name="terra.wasm.v1beta1.ContractInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="address",
            full_name="terra.wasm.v1beta1.ContractInfo.address",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\016yaml:"address"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="creator",
            full_name="terra.wasm.v1beta1.ContractInfo.creator",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\016yaml:"creator"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="admin",
            full_name="terra.wasm.v1beta1.ContractInfo.admin",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\014yaml:"admin"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="code_id",
            full_name="terra.wasm.v1beta1.ContractInfo.code_id",
            index=3,
            number=4,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\016yaml:"code_id"\342\336\037\006CodeID',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="init_msg",
            full_name="terra.wasm.v1beta1.ContractInfo.init_msg",
            index=4,
            number=5,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\017yaml:"init_msg"\372\336\037\030encoding/json.RawMessage',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\350\240\037\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=444,
    serialized_end=685,
)

DESCRIPTOR.message_types_by_name["Params"] = _PARAMS
DESCRIPTOR.message_types_by_name["CodeInfo"] = _CODEINFO
DESCRIPTOR.message_types_by_name["ContractInfo"] = _CONTRACTINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Params = _reflection.GeneratedProtocolMessageType(
    "Params",
    (_message.Message,),
    {
        "DESCRIPTOR": _PARAMS,
        "__module__": "terra.wasm.v1beta1.wasm_pb2"
        # @@protoc_insertion_point(class_scope:terra.wasm.v1beta1.Params)
    },
)
_sym_db.RegisterMessage(Params)

CodeInfo = _reflection.GeneratedProtocolMessageType(
    "CodeInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _CODEINFO,
        "__module__": "terra.wasm.v1beta1.wasm_pb2"
        # @@protoc_insertion_point(class_scope:terra.wasm.v1beta1.CodeInfo)
    },
)
_sym_db.RegisterMessage(CodeInfo)

ContractInfo = _reflection.GeneratedProtocolMessageType(
    "ContractInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONTRACTINFO,
        "__module__": "terra.wasm.v1beta1.wasm_pb2"
        # @@protoc_insertion_point(class_scope:terra.wasm.v1beta1.ContractInfo)
    },
)
_sym_db.RegisterMessage(ContractInfo)


DESCRIPTOR._options = None
_PARAMS.fields_by_name["max_contract_size"]._options = None
_PARAMS.fields_by_name["max_contract_gas"]._options = None
_PARAMS.fields_by_name["max_contract_msg_size"]._options = None
_PARAMS._options = None
_CODEINFO.fields_by_name["code_id"]._options = None
_CODEINFO.fields_by_name["code_hash"]._options = None
_CODEINFO.fields_by_name["creator"]._options = None
_CONTRACTINFO.fields_by_name["address"]._options = None
_CONTRACTINFO.fields_by_name["creator"]._options = None
_CONTRACTINFO.fields_by_name["admin"]._options = None
_CONTRACTINFO.fields_by_name["code_id"]._options = None
_CONTRACTINFO.fields_by_name["init_msg"]._options = None
_CONTRACTINFO._options = None
# @@protoc_insertion_point(module_scope)
