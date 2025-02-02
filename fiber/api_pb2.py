# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import fiber.eth_pb2 as eth__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tapi.proto\x12\x03\x61pi\x1a\teth.proto\x1a\x1bgoogle/protobuf/empty.proto\"3\n\rTxSequenceMsg\x12\"\n\x08sequence\x18\x01 \x03(\x0b\x32\x10.eth.Transaction\"#\n\x10RawTxSequenceMsg\x12\x0f\n\x07raw_txs\x18\x01 \x03(\x0c\"I\n\x12TxSequenceResponse\x12\x33\n\x11sequence_response\x18\x01 \x03(\x0b\x32\x18.api.TransactionResponse\"\x1b\n\x08TxFilter\x12\x0f\n\x07\x65ncoded\x18\x01 \x01(\x0c\"\x1f\n\x0b\x42lockFilter\x12\x10\n\x08producer\x18\x01 \x01(\t\"\x19\n\x08RawTxMsg\x12\r\n\x05rawTx\x18\x01 \x01(\x0c\"6\n\x13TransactionResponse\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\"8\n\nBackrunMsg\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\x1c\n\x02tx\x18\x02 \x01(\x0b\x32\x10.eth.Transaction\",\n\rRawBackrunMsg\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\r\n\x05rawTx\x18\x02 \x01(\x0c\x32\xa7\x03\n\x03\x41PI\x12\x36\n\x0fSubscribeNewTxs\x12\r.api.TxFilter\x1a\x10.eth.Transaction\"\x00\x30\x01\x12\x43\n\x0fSendTransaction\x12\x10.eth.Transaction\x1a\x18.api.TransactionResponse\"\x00(\x01\x30\x01\x12\x43\n\x12SendRawTransaction\x12\r.api.RawTxMsg\x1a\x18.api.TransactionResponse\"\x00(\x01\x30\x01\x12L\n\x17SendTransactionSequence\x12\x12.api.TxSequenceMsg\x1a\x17.api.TxSequenceResponse\"\x00(\x01\x30\x01\x12R\n\x1aSendRawTransactionSequence\x12\x15.api.RawTxSequenceMsg\x1a\x17.api.TxSequenceResponse\"\x00(\x01\x30\x01\x12<\n\x12SubscribeNewBlocks\x12\x16.google.protobuf.Empty\x1a\n.eth.Block\"\x00\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TXSEQUENCEMSG._serialized_start=58
  _TXSEQUENCEMSG._serialized_end=109
  _RAWTXSEQUENCEMSG._serialized_start=111
  _RAWTXSEQUENCEMSG._serialized_end=146
  _TXSEQUENCERESPONSE._serialized_start=148
  _TXSEQUENCERESPONSE._serialized_end=221
  _TXFILTER._serialized_start=223
  _TXFILTER._serialized_end=250
  _BLOCKFILTER._serialized_start=252
  _BLOCKFILTER._serialized_end=283
  _RAWTXMSG._serialized_start=285
  _RAWTXMSG._serialized_end=310
  _TRANSACTIONRESPONSE._serialized_start=312
  _TRANSACTIONRESPONSE._serialized_end=366
  _BACKRUNMSG._serialized_start=368
  _BACKRUNMSG._serialized_end=424
  _RAWBACKRUNMSG._serialized_start=426
  _RAWBACKRUNMSG._serialized_end=470
  _API._serialized_start=473
  _API._serialized_end=896
# @@protoc_insertion_point(module_scope)
