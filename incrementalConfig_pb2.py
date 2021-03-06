# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='incrementalConfig.proto',
  package='poem',
  serialized_pb='\n\x17incrementalConfig.proto\x12\x04poem\"A\n\nfield_info\x12\x10\n\x08key_name\x18\x01 \x02(\t\x12\x12\n\nvalue_type\x18\x02 \x02(\x05\x12\r\n\x05value\x18\x03 \x02(\t\"E\n\x10\x63onfig_item_info\x12\n\n\x02id\x18\x01 \x02(\x05\x12%\n\x0b\x64iff_fields\x18\x02 \x03(\x0b\x32\x10.poem.field_info\"N\n\x10\x63onfig_file_info\x12\x13\n\x0b\x63onfig_name\x18\x01 \x02(\t\x12%\n\x05items\x18\x02 \x03(\x0b\x32\x16.poem.config_item_info\"X\n\x11incrementResponse\x12\x16\n\x0e\x63onfig_version\x18\x01 \x02(\x05\x12+\n\x0b\x63onfig_diff\x18\x02 \x03(\x0b\x32\x16.poem.config_file_info\"*\n\x10incrementRequest\x12\x16\n\x0e\x63onfig_version\x18\x01 \x02(\x05\x42\x02H\x03')




_FIELD_INFO = descriptor.Descriptor(
  name='field_info',
  full_name='poem.field_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='key_name', full_name='poem.field_info.key_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value_type', full_name='poem.field_info.value_type', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='poem.field_info.value', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=33,
  serialized_end=98,
)


_CONFIG_ITEM_INFO = descriptor.Descriptor(
  name='config_item_info',
  full_name='poem.config_item_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='poem.config_item_info.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='diff_fields', full_name='poem.config_item_info.diff_fields', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=100,
  serialized_end=169,
)


_CONFIG_FILE_INFO = descriptor.Descriptor(
  name='config_file_info',
  full_name='poem.config_file_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='config_name', full_name='poem.config_file_info.config_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='items', full_name='poem.config_file_info.items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=171,
  serialized_end=249,
)


_INCREMENTRESPONSE = descriptor.Descriptor(
  name='incrementResponse',
  full_name='poem.incrementResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='config_version', full_name='poem.incrementResponse.config_version', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='config_diff', full_name='poem.incrementResponse.config_diff', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=251,
  serialized_end=339,
)


_INCREMENTREQUEST = descriptor.Descriptor(
  name='incrementRequest',
  full_name='poem.incrementRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='config_version', full_name='poem.incrementRequest.config_version', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=341,
  serialized_end=383,
)

_CONFIG_ITEM_INFO.fields_by_name['diff_fields'].message_type = _FIELD_INFO
_CONFIG_FILE_INFO.fields_by_name['items'].message_type = _CONFIG_ITEM_INFO
_INCREMENTRESPONSE.fields_by_name['config_diff'].message_type = _CONFIG_FILE_INFO
DESCRIPTOR.message_types_by_name['field_info'] = _FIELD_INFO
DESCRIPTOR.message_types_by_name['config_item_info'] = _CONFIG_ITEM_INFO
DESCRIPTOR.message_types_by_name['config_file_info'] = _CONFIG_FILE_INFO
DESCRIPTOR.message_types_by_name['incrementResponse'] = _INCREMENTRESPONSE
DESCRIPTOR.message_types_by_name['incrementRequest'] = _INCREMENTREQUEST

class field_info(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FIELD_INFO
  
  # @@protoc_insertion_point(class_scope:poem.field_info)

class config_item_info(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CONFIG_ITEM_INFO
  
  # @@protoc_insertion_point(class_scope:poem.config_item_info)

class config_file_info(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CONFIG_FILE_INFO
  
  # @@protoc_insertion_point(class_scope:poem.config_file_info)

class incrementResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INCREMENTRESPONSE
  
  # @@protoc_insertion_point(class_scope:poem.incrementResponse)

class incrementRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INCREMENTREQUEST
  
  # @@protoc_insertion_point(class_scope:poem.incrementRequest)

# @@protoc_insertion_point(module_scope)
