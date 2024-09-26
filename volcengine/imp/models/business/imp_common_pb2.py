# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: imp/business/imp_common.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='imp/business/imp_common.proto',
  package='Volcengine.Imp.Models.Business',
  syntax='proto3',
  serialized_options=b'\n)com.volcengine.service.imp.model.businessB\013ImpWorkflowP\001ZAgithub.com/volcengine/volc-sdk-golang/service/imp/models/business\240\001\001\330\001\001\312\002 Volc\\Service\\Imp\\Models\\Business\342\002#Volc\\Service\\Imp\\Models\\GPBMetadata',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1dimp/business/imp_common.proto\x12\x1eVolcengine.Imp.Models.Business\"R\n\tInputPath\x12\x0c\n\x04Type\x18\x01 \x01(\t\x12\x11\n\tTosBucket\x18\x02 \x01(\t\x12\x14\n\x0cVodSpaceName\x18\x03 \x01(\t\x12\x0e\n\x06\x46ileId\x18\x04 \x01(\t\"\xc8\x01\n\tJobOutput\x12\x12\n\nTemplateId\x18\x01 \x01(\t\x12\x12\n\nProperties\x18\x02 \x01(\t\x12\x0c\n\x04\x43ode\x18\x03 \x01(\t\x12\x15\n\rFileMessageId\x18\x04 \x01(\t\x12\x10\n\x08TaskType\x18\x05 \x01(\t\x12\x0e\n\x06Status\x18\x06 \x01(\t\x12\x12\n\nActivityId\x18\x07 \x01(\t\x12\x11\n\tStartTime\x18\x08 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\t \x01(\t\x12\x14\n\x0cTemplateName\x18\n \x01(\t\"\x8e\x02\n\x0cJobExecution\x12\r\n\x05JobId\x18\x01 \x01(\t\x12<\n\tInputPath\x18\x02 \x01(\x0b\x32).Volcengine.Imp.Models.Business.InputPath\x12\x39\n\x06Output\x18\x03 \x03(\x0b\x32).Volcengine.Imp.Models.Business.JobOutput\x12\x0e\n\x06Status\x18\x04 \x01(\t\x12\x10\n\x08\x43reateAt\x18\x05 \x01(\t\x12\x12\n\nFinishedAt\x18\x06 \x01(\t\x12\x12\n\nTemplateId\x18\x07 \x01(\t\x12\x19\n\x11\x45nableLowPriority\x18\x08 \x01(\t\x12\x11\n\tJobSource\x18\t \x01(\t\"P\n\x06Params\x12\x46\n\x0eOverrideParams\x18\x01 \x01(\x0b\x32..Volcengine.Imp.Models.Business.OverrideParams\"\xa4\x01\n\x0eOverrideParams\x12L\n\nSmartErase\x18\x01 \x03(\x0b\x32\x38.Volcengine.Imp.Models.Business.SmartEraseOverrideParams\x12\x44\n\x06Output\x18\x02 \x03(\x0b\x32\x34.Volcengine.Imp.Models.Business.OutputOverrideParams\"\x9e\x01\n\x18SmartEraseOverrideParams\x12\x12\n\nActivityId\x18\x01 \x03(\t\x12<\n\tWatermark\x18\x02 \x01(\x0b\x32).Volcengine.Imp.Models.Business.Watermark\x12\x30\n\x03OCR\x18\x03 \x01(\x0b\x32#.Volcengine.Imp.Models.Business.OCR\"K\n\tWatermark\x12>\n\nDetectRect\x18\x01 \x03(\x0b\x32*.Volcengine.Imp.Models.Business.DetectRect\"E\n\x03OCR\x12>\n\nDetectRect\x18\x01 \x03(\x0b\x32*.Volcengine.Imp.Models.Business.DetectRect\"<\n\nDetectRect\x12\n\n\x02X1\x18\x01 \x01(\x01\x12\n\n\x02Y1\x18\x02 \x01(\x01\x12\n\n\x02X2\x18\x03 \x01(\x01\x12\n\n\x02Y2\x18\x04 \x01(\x01\"j\n\x14OutputOverrideParams\x12\x12\n\nActivityId\x18\x01 \x03(\t\x12>\n\nOutputPath\x18\x02 \x01(\x0b\x32*.Volcengine.Imp.Models.Business.OutputPath\"U\n\nOutputPath\x12\x0c\n\x04Type\x18\x01 \x01(\t\x12\x11\n\tTosBucket\x18\x02 \x01(\t\x12\x14\n\x0cVodSpaceName\x18\x03 \x01(\t\x12\x10\n\x08\x46ileName\x18\x04 \x01(\tB\xcc\x01\n)com.volcengine.service.imp.model.businessB\x0bImpWorkflowP\x01ZAgithub.com/volcengine/volc-sdk-golang/service/imp/models/business\xa0\x01\x01\xd8\x01\x01\xca\x02 Volc\\Service\\Imp\\Models\\Business\xe2\x02#Volc\\Service\\Imp\\Models\\GPBMetadatab\x06proto3'
)




_INPUTPATH = _descriptor.Descriptor(
  name='InputPath',
  full_name='Volcengine.Imp.Models.Business.InputPath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='Volcengine.Imp.Models.Business.InputPath.Type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='TosBucket', full_name='Volcengine.Imp.Models.Business.InputPath.TosBucket', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='VodSpaceName', full_name='Volcengine.Imp.Models.Business.InputPath.VodSpaceName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='FileId', full_name='Volcengine.Imp.Models.Business.InputPath.FileId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=65,
  serialized_end=147,
)


_JOBOUTPUT = _descriptor.Descriptor(
  name='JobOutput',
  full_name='Volcengine.Imp.Models.Business.JobOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='TemplateId', full_name='Volcengine.Imp.Models.Business.JobOutput.TemplateId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Properties', full_name='Volcengine.Imp.Models.Business.JobOutput.Properties', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Code', full_name='Volcengine.Imp.Models.Business.JobOutput.Code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='FileMessageId', full_name='Volcengine.Imp.Models.Business.JobOutput.FileMessageId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='TaskType', full_name='Volcengine.Imp.Models.Business.JobOutput.TaskType', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Status', full_name='Volcengine.Imp.Models.Business.JobOutput.Status', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ActivityId', full_name='Volcengine.Imp.Models.Business.JobOutput.ActivityId', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='StartTime', full_name='Volcengine.Imp.Models.Business.JobOutput.StartTime', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='EndTime', full_name='Volcengine.Imp.Models.Business.JobOutput.EndTime', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='TemplateName', full_name='Volcengine.Imp.Models.Business.JobOutput.TemplateName', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=150,
  serialized_end=350,
)


_JOBEXECUTION = _descriptor.Descriptor(
  name='JobExecution',
  full_name='Volcengine.Imp.Models.Business.JobExecution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='JobId', full_name='Volcengine.Imp.Models.Business.JobExecution.JobId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='InputPath', full_name='Volcengine.Imp.Models.Business.JobExecution.InputPath', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Output', full_name='Volcengine.Imp.Models.Business.JobExecution.Output', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Status', full_name='Volcengine.Imp.Models.Business.JobExecution.Status', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='CreateAt', full_name='Volcengine.Imp.Models.Business.JobExecution.CreateAt', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='FinishedAt', full_name='Volcengine.Imp.Models.Business.JobExecution.FinishedAt', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='TemplateId', full_name='Volcengine.Imp.Models.Business.JobExecution.TemplateId', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='EnableLowPriority', full_name='Volcengine.Imp.Models.Business.JobExecution.EnableLowPriority', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='JobSource', full_name='Volcengine.Imp.Models.Business.JobExecution.JobSource', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=353,
  serialized_end=623,
)


_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='Volcengine.Imp.Models.Business.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='OverrideParams', full_name='Volcengine.Imp.Models.Business.Params.OverrideParams', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=625,
  serialized_end=705,
)


_OVERRIDEPARAMS = _descriptor.Descriptor(
  name='OverrideParams',
  full_name='Volcengine.Imp.Models.Business.OverrideParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='SmartErase', full_name='Volcengine.Imp.Models.Business.OverrideParams.SmartErase', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Output', full_name='Volcengine.Imp.Models.Business.OverrideParams.Output', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=708,
  serialized_end=872,
)


_SMARTERASEOVERRIDEPARAMS = _descriptor.Descriptor(
  name='SmartEraseOverrideParams',
  full_name='Volcengine.Imp.Models.Business.SmartEraseOverrideParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ActivityId', full_name='Volcengine.Imp.Models.Business.SmartEraseOverrideParams.ActivityId', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Watermark', full_name='Volcengine.Imp.Models.Business.SmartEraseOverrideParams.Watermark', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='OCR', full_name='Volcengine.Imp.Models.Business.SmartEraseOverrideParams.OCR', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=875,
  serialized_end=1033,
)


_WATERMARK = _descriptor.Descriptor(
  name='Watermark',
  full_name='Volcengine.Imp.Models.Business.Watermark',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='DetectRect', full_name='Volcengine.Imp.Models.Business.Watermark.DetectRect', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1035,
  serialized_end=1110,
)


_OCR = _descriptor.Descriptor(
  name='OCR',
  full_name='Volcengine.Imp.Models.Business.OCR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='DetectRect', full_name='Volcengine.Imp.Models.Business.OCR.DetectRect', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1112,
  serialized_end=1181,
)


_DETECTRECT = _descriptor.Descriptor(
  name='DetectRect',
  full_name='Volcengine.Imp.Models.Business.DetectRect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='X1', full_name='Volcengine.Imp.Models.Business.DetectRect.X1', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Y1', full_name='Volcengine.Imp.Models.Business.DetectRect.Y1', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='X2', full_name='Volcengine.Imp.Models.Business.DetectRect.X2', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Y2', full_name='Volcengine.Imp.Models.Business.DetectRect.Y2', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1183,
  serialized_end=1243,
)


_OUTPUTOVERRIDEPARAMS = _descriptor.Descriptor(
  name='OutputOverrideParams',
  full_name='Volcengine.Imp.Models.Business.OutputOverrideParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ActivityId', full_name='Volcengine.Imp.Models.Business.OutputOverrideParams.ActivityId', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='OutputPath', full_name='Volcengine.Imp.Models.Business.OutputOverrideParams.OutputPath', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1245,
  serialized_end=1351,
)


_OUTPUTPATH = _descriptor.Descriptor(
  name='OutputPath',
  full_name='Volcengine.Imp.Models.Business.OutputPath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='Volcengine.Imp.Models.Business.OutputPath.Type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='TosBucket', full_name='Volcengine.Imp.Models.Business.OutputPath.TosBucket', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='VodSpaceName', full_name='Volcengine.Imp.Models.Business.OutputPath.VodSpaceName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='FileName', full_name='Volcengine.Imp.Models.Business.OutputPath.FileName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1353,
  serialized_end=1438,
)

_JOBEXECUTION.fields_by_name['InputPath'].message_type = _INPUTPATH
_JOBEXECUTION.fields_by_name['Output'].message_type = _JOBOUTPUT
_PARAMS.fields_by_name['OverrideParams'].message_type = _OVERRIDEPARAMS
_OVERRIDEPARAMS.fields_by_name['SmartErase'].message_type = _SMARTERASEOVERRIDEPARAMS
_OVERRIDEPARAMS.fields_by_name['Output'].message_type = _OUTPUTOVERRIDEPARAMS
_SMARTERASEOVERRIDEPARAMS.fields_by_name['Watermark'].message_type = _WATERMARK
_SMARTERASEOVERRIDEPARAMS.fields_by_name['OCR'].message_type = _OCR
_WATERMARK.fields_by_name['DetectRect'].message_type = _DETECTRECT
_OCR.fields_by_name['DetectRect'].message_type = _DETECTRECT
_OUTPUTOVERRIDEPARAMS.fields_by_name['OutputPath'].message_type = _OUTPUTPATH
DESCRIPTOR.message_types_by_name['InputPath'] = _INPUTPATH
DESCRIPTOR.message_types_by_name['JobOutput'] = _JOBOUTPUT
DESCRIPTOR.message_types_by_name['JobExecution'] = _JOBEXECUTION
DESCRIPTOR.message_types_by_name['Params'] = _PARAMS
DESCRIPTOR.message_types_by_name['OverrideParams'] = _OVERRIDEPARAMS
DESCRIPTOR.message_types_by_name['SmartEraseOverrideParams'] = _SMARTERASEOVERRIDEPARAMS
DESCRIPTOR.message_types_by_name['Watermark'] = _WATERMARK
DESCRIPTOR.message_types_by_name['OCR'] = _OCR
DESCRIPTOR.message_types_by_name['DetectRect'] = _DETECTRECT
DESCRIPTOR.message_types_by_name['OutputOverrideParams'] = _OUTPUTOVERRIDEPARAMS
DESCRIPTOR.message_types_by_name['OutputPath'] = _OUTPUTPATH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InputPath = _reflection.GeneratedProtocolMessageType('InputPath', (_message.Message,), {
  'DESCRIPTOR' : _INPUTPATH,
  '__module__' : 'imp.business.imp_common_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Imp.Models.Business.InputPath)
  })
_sym_db.RegisterMessage(InputPath)

JobOutput = _reflection.GeneratedProtocolMessageType('JobOutput', (_message.Message,), {
  'DESCRIPTOR' : _JOBOUTPUT,
  '__module__' : 'imp.business.imp_common_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Imp.Models.Business.JobOutput)
  })
_sym_db.RegisterMessage(JobOutput)

JobExecution = _reflection.GeneratedProtocolMessageType('JobExecution', (_message.Message,), {
  'DESCRIPTOR' : _JOBEXECUTION,
  '__module__' : 'imp.business.imp_common_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Imp.Models.Business.JobExecution)
  })
_sym_db.RegisterMessage(JobExecution)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'imp.business.imp_common_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Imp.Models.Business.Params)
  })
_sym_db.RegisterMessage(Params)

OverrideParams = _reflection.GeneratedProtocolMessageType('OverrideParams', (_message.Message,), {
  'DESCRIPTOR' : _OVERRIDEPARAMS,
  '__module__' : 'imp.business.imp_common_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Imp.Models.Business.OverrideParams)
  })
_sym_db.RegisterMessage(OverrideParams)

SmartEraseOverrideParams = _reflection.GeneratedProtocolMessageType('SmartEraseOverrideParams', (_message.Message,), {
  'DESCRIPTOR' : _SMARTERASEOVERRIDEPARAMS,
  '__module__' : 'imp.business.imp_common_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Imp.Models.Business.SmartEraseOverrideParams)
  })
_sym_db.RegisterMessage(SmartEraseOverrideParams)

Watermark = _reflection.GeneratedProtocolMessageType('Watermark', (_message.Message,), {
  'DESCRIPTOR' : _WATERMARK,
  '__module__' : 'imp.business.imp_common_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Imp.Models.Business.Watermark)
  })
_sym_db.RegisterMessage(Watermark)

OCR = _reflection.GeneratedProtocolMessageType('OCR', (_message.Message,), {
  'DESCRIPTOR' : _OCR,
  '__module__' : 'imp.business.imp_common_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Imp.Models.Business.OCR)
  })
_sym_db.RegisterMessage(OCR)

DetectRect = _reflection.GeneratedProtocolMessageType('DetectRect', (_message.Message,), {
  'DESCRIPTOR' : _DETECTRECT,
  '__module__' : 'imp.business.imp_common_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Imp.Models.Business.DetectRect)
  })
_sym_db.RegisterMessage(DetectRect)

OutputOverrideParams = _reflection.GeneratedProtocolMessageType('OutputOverrideParams', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUTOVERRIDEPARAMS,
  '__module__' : 'imp.business.imp_common_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Imp.Models.Business.OutputOverrideParams)
  })
_sym_db.RegisterMessage(OutputOverrideParams)

OutputPath = _reflection.GeneratedProtocolMessageType('OutputPath', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUTPATH,
  '__module__' : 'imp.business.imp_common_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Imp.Models.Business.OutputPath)
  })
_sym_db.RegisterMessage(OutputPath)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
