# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eth.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import fiber.types_pb2 as types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\teth.proto\x12\x03\x65th\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0btypes.proto\"\x84\x01\n\x0b\x42lockNumber\x12(\n\x06latest\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12)\n\x07pending\x18\x02 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12\x10\n\x06number\x18\x03 \x01(\x04H\x00\x42\x0e\n\x0c\x62lock_number\"P\n\x07\x42lockId\x12\x1b\n\x04hash\x18\x01 \x01(\x0b\x32\x0b.types.H256H\x00\x12\"\n\x06number\x18\x02 \x01(\x0b\x32\x10.eth.BlockNumberH\x00\x42\x04\n\x02id\"`\n\x18\x43\x61nonicalTransactionData\x12\x1f\n\nblock_hash\x18\x01 \x01(\x0b\x32\x0b.types.H256\x12\x14\n\x0c\x62lock_number\x18\x02 \x01(\x04\x12\r\n\x05index\x18\x03 \x01(\x04\"J\n\x0e\x41\x63\x63\x65ssListItem\x12\x1c\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x0b.types.H160\x12\x1a\n\x05slots\x18\x02 \x03(\x0b\x32\x0b.types.H256\"\xaa\x02\n\x0bTransaction\x12\x0f\n\x02to\x18\x01 \x01(\x0cH\x00\x88\x01\x01\x12\x0b\n\x03gas\x18\x02 \x01(\x04\x12\x11\n\tgas_price\x18\x03 \x01(\x04\x12\x0c\n\x04hash\x18\x04 \x01(\x0c\x12\r\n\x05input\x18\x05 \x01(\x0c\x12\r\n\x05nonce\x18\x06 \x01(\x04\x12\r\n\x05value\x18\x07 \x01(\x0c\x12\x11\n\x04\x66rom\x18\x08 \x01(\x0cH\x01\x88\x01\x01\x12\x0c\n\x04type\x18\t \x01(\r\x12\x0f\n\x07max_fee\x18\n \x01(\x04\x12\x14\n\x0cpriority_fee\x18\x0b \x01(\x04\x12\t\n\x01v\x18\x0c \x01(\x04\x12\t\n\x01r\x18\r \x01(\x0c\x12\t\n\x01s\x18\x0e \x01(\x0c\x12\x0f\n\x07\x63hainId\x18\x0f \x01(\r\x12%\n\x0b\x61\x63\x63\x65ss_list\x18\x10 \x03(\x0b\x32\x10.eth.AccessTupleB\x05\n\x03_toB\x07\n\x05_from\"4\n\x0b\x41\x63\x63\x65ssTuple\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x14\n\x0cstorage_keys\x18\x02 \x03(\x0c\"\xc6\x02\n\x05\x42lock\x12\x0e\n\x06number\x18\x01 \x01(\x04\x12\x0c\n\x04hash\x18\x02 \x01(\x0c\x12\x13\n\x0bparent_hash\x18\x03 \x01(\x0c\x12\x13\n\x0bprev_randao\x18\x04 \x01(\x0c\x12\x12\n\nstate_root\x18\x05 \x01(\x0c\x12\x14\n\x0creceipt_root\x18\x06 \x01(\x0c\x12\x15\n\rfee_recipient\x18\x07 \x01(\x0c\x12\x17\n\nextra_data\x18\x08 \x01(\x0cH\x00\x88\x01\x01\x12\x11\n\tgas_limit\x18\t \x01(\x04\x12\x10\n\x08gas_used\x18\n \x01(\x04\x12\x11\n\ttimestamp\x18\x0b \x01(\x04\x12\x12\n\nlogs_bloom\x18\x0c \x01(\x0c\x12\x18\n\x10\x62\x61se_fee_per_gas\x18\r \x01(\x0c\x12&\n\x0ctransactions\x18\x0e \x03(\x0b\x32\x10.eth.TransactionB\r\n\x0b_extra_datab\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eth_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BLOCKNUMBER._serialized_start=61
  _BLOCKNUMBER._serialized_end=193
  _BLOCKID._serialized_start=195
  _BLOCKID._serialized_end=275
  _CANONICALTRANSACTIONDATA._serialized_start=277
  _CANONICALTRANSACTIONDATA._serialized_end=373
  _ACCESSLISTITEM._serialized_start=375
  _ACCESSLISTITEM._serialized_end=449
  _TRANSACTION._serialized_start=452
  _TRANSACTION._serialized_end=750
  _ACCESSTUPLE._serialized_start=752
  _ACCESSTUPLE._serialized_end=804
  _BLOCK._serialized_start=807
  _BLOCK._serialized_end=1133
# @@protoc_insertion_point(module_scope)
