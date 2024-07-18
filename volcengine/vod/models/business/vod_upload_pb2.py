# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: volcengine/vod/business/vod_upload.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from volcengine.vod.models.business import vod_common_pb2 as volcengine_dot_vod_dot_business_dot_vod__common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(volcengine/vod/business/vod_upload.proto\x12\x1eVolcengine.Vod.Models.Business\x1a(volcengine/vod/business/vod_common.proto\"\x99\x04\n\x12VodUrlUploadURLSet\x12\x11\n\tSourceUrl\x18\x01 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x02 \x01(\t\x12\x0b\n\x03Md5\x18\x03 \x01(\t\x12\x12\n\nTemplateId\x18\x04 \x01(\t\x12\r\n\x05Title\x18\x05 \x01(\t\x12\x13\n\x0b\x44\x65scription\x18\x06 \x01(\t\x12\x0c\n\x04Tags\x18\x07 \x01(\t\x12\x10\n\x08\x43\x61tegory\x18\x08 \x01(\t\x12\x10\n\x08\x46ileName\x18\t \x01(\t\x12\x18\n\x10\x43lassificationId\x18\n \x01(\x03\x12\x14\n\x0cStorageClass\x18\x0b \x01(\x05\x12\x15\n\rFileExtension\x18\x0c \x01(\t\x12\x1e\n\x16UrlEncryptionAlgorithm\x18\r \x01(\t\x12\x19\n\x11\x45nableLowPriority\x18\x0e \x01(\x08\x12\x62\n\x10\x43ustomURLHeaders\x18\x0f \x03(\x0b\x32H.Volcengine.Vod.Models.Business.VodUrlUploadURLSet.CustomURLHeadersEntry\x12\x44\n\tTemplates\x18\x10 \x03(\x0b\x32\x31.Volcengine.Vod.Models.Business.VodUploadTemplate\x1a\x37\n\x15\x43ustomURLHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"M\n\x12VodUrlResponseData\x12\x37\n\x04\x44\x61ta\x18\x01 \x03(\x0b\x32).Volcengine.Vod.Models.Business.ValuePair\"-\n\tValuePair\x12\r\n\x05JobId\x18\x01 \x01(\t\x12\x11\n\tSourceUrl\x18\x02 \x01(\t\"R\n\x0cVodQueryData\x12\x42\n\x04\x44\x61ta\x18\x01 \x01(\x0b\x32\x34.Volcengine.Vod.Models.Business.VodQueryUploadResult\"p\n\x14VodQueryUploadResult\x12@\n\rMediaInfoList\x18\x01 \x03(\x0b\x32).Volcengine.Vod.Models.Business.VodURLSet\x12\x16\n\x0eNotExistJobIds\x18\x02 \x03(\t\"^\n\rVodCommitData\x12M\n\x04\x44\x61ta\x18\x01 \x01(\x0b\x32?.Volcengine.Vod.Models.Business.VodCommitUploadInfoResponseData\"\xa7\x01\n\x1fVodCommitUploadInfoResponseData\x12\x0b\n\x03Vid\x18\x01 \x01(\t\x12\x41\n\nSourceInfo\x18\x02 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.VodSourceInfo\x12\x11\n\tPosterUri\x18\x03 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x04 \x01(\t\x12\x0b\n\x03Mid\x18\x05 \x01(\t\"\xdb\x01\n\tVodURLSet\x12\x11\n\tRequestId\x18\x01 \x01(\t\x12\r\n\x05JobId\x18\x02 \x01(\t\x12\x11\n\tSourceUrl\x18\x03 \x01(\t\x12\r\n\x05State\x18\x04 \x01(\t\x12\x0b\n\x03Vid\x18\x05 \x01(\t\x12\x11\n\tSpaceName\x18\x06 \x01(\t\x12\x11\n\tAccountId\x18\x07 \x01(\t\x12\x41\n\nSourceInfo\x18\x08 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.VodSourceInfo\x12\x14\n\x0c\x43\x61llbackArgs\x18\t \x01(\t\"`\n\x18VodApplyUploadInfoResult\x12\x44\n\x04\x44\x61ta\x18\x01 \x01(\x0b\x32\x36.Volcengine.Vod.Models.Business.VodApplyUploadInfoData\"\xbd\x01\n\x16VodApplyUploadInfoData\x12G\n\rUploadAddress\x18\x01 \x01(\x0b\x32\x30.Volcengine.Vod.Models.Business.VodUploadAddress\x12Z\n\x18\x43\x61ndidateUploadAddresses\x18\x02 \x01(\x0b\x32\x38.Volcengine.Vod.Models.Business.CandidateUploadAddresses\"\xc2\x01\n\x10VodUploadAddress\x12@\n\nStoreInfos\x18\x01 \x03(\x0b\x32,.Volcengine.Vod.Models.Business.VodStoreInfo\x12\x13\n\x0bUploadHosts\x18\x02 \x03(\t\x12\x43\n\x0cUploadHeader\x18\x03 \x03(\x0b\x32-.Volcengine.Vod.Models.Business.VodHeaderPair\x12\x12\n\nSessionKey\x18\x04 \x01(\t\"\x84\x02\n\x18\x43\x61ndidateUploadAddresses\x12J\n\x13MainUploadAddresses\x18\x01 \x03(\x0b\x32-.Volcengine.Vod.Models.Business.UploadAddress\x12L\n\x15\x42\x61\x63kupUploadAddresses\x18\x02 \x03(\x0b\x32-.Volcengine.Vod.Models.Business.UploadAddress\x12N\n\x17\x46\x61llbackUploadAddresses\x18\x03 \x03(\x0b\x32-.Volcengine.Vod.Models.Business.UploadAddress\".\n\x0cVodStoreInfo\x12\x10\n\x08StoreUri\x18\x01 \x01(\t\x12\x0c\n\x04\x41uth\x18\x02 \x01(\t\"+\n\rVodHeaderPair\x12\x0b\n\x03Key\x18\x01 \x01(\t\x12\r\n\x05Value\x18\x02 \x01(\t\"b\n\x19VodCommitUploadInfoResult\x12\x45\n\x04\x44\x61ta\x18\x01 \x01(\x0b\x32\x37.Volcengine.Vod.Models.Business.VodCommitUploadInfoData\"\x89\x01\n\x17VodCommitUploadInfoData\x12\x0b\n\x03Vid\x18\x01 \x01(\t\x12\x11\n\tPosterUri\x18\x02 \x01(\t\x12\x41\n\nSourceInfo\x18\x03 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.VodSourceInfo\x12\x0b\n\x03Mid\x18\x04 \x01(\t\"\xbc\x03\n\x16VodUploadFunctionInput\x12\x14\n\x0cSnapshotTime\x18\x01 \x01(\x01\x12\r\n\x05Title\x18\x02 \x01(\t\x12\x0c\n\x04Tags\x18\x03 \x01(\t\x12\x13\n\x0b\x44\x65scription\x18\x04 \x01(\t\x12\x10\n\x08\x43\x61tegory\x18\x05 \x01(\t\x12\x12\n\nRecordType\x18\x06 \x01(\x05\x12\x0e\n\x06\x46ormat\x18\x07 \x01(\t\x12\x18\n\x10\x43lassificationId\x18\x08 \x01(\x05\x12\x12\n\nTemplateId\x18\t \x01(\t\x12\x0b\n\x03Vid\x18\n \x01(\t\x12\x0b\n\x03\x46id\x18\x0b \x01(\t\x12\x10\n\x08Language\x18\x0c \x01(\t\x12\x10\n\x08StoreUri\x18\r \x01(\t\x12\x0e\n\x06Source\x18\x0e \x01(\t\x12\x0b\n\x03Tag\x18\x0f \x01(\t\x12\x13\n\x0b\x41utoPublish\x18\x10 \x01(\x08\x12\x12\n\nActionType\x18\x11 \x01(\t\x12\x16\n\x0eIsHlsIndexOnly\x18\x12 \x01(\x08\x12\x14\n\x0cHlsMediaSize\x18\x13 \x01(\t\x12\x44\n\tTemplates\x18\x14 \x03(\x0b\x32\x31.Volcengine.Vod.Models.Business.VodUploadTemplate\"h\n\x11VodUploadFunction\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x45\n\x05Input\x18\x02 \x01(\x0b\x32\x36.Volcengine.Vod.Models.Business.VodUploadFunctionInput\"\xc8\x01\n\x15\x43ommitUploadInfoParam\x12\x11\n\tSpaceName\x18\x01 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x02 \x01(\t\x12\x12\n\nSessionKey\x18\x03 \x01(\t\x12\x44\n\tFunctions\x18\x04 \x03(\x0b\x32\x31.Volcengine.Vod.Models.Business.VodUploadFunction\x12\x13\n\x0bGetMetaMode\x18\x05 \x01(\t\x12\x17\n\x0fVodUploadSource\x18\x06 \x01(\t\"\x95\x01\n\x15\x43ommitRequestBodyJson\x12\x11\n\tSpaceName\x18\x01 \x01(\t\x12\x12\n\nSessionKey\x18\x02 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x03 \x01(\t\x12\x11\n\tFunctions\x18\x04 \x01(\t\x12\x13\n\x0bGetMetaMode\x18\x05 \x01(\t\x12\x17\n\x0fVodUploadSource\x18\x06 \x01(\t\"\x9e\x02\n\x14\x41pplyUploadInfoParam\x12\x11\n\tSpaceName\x18\x01 \x01(\t\x12\x10\n\x08\x46ileType\x18\x02 \x01(\t\x12\x12\n\nSessionKey\x18\x03 \x01(\t\x12\x10\n\x08\x46ileSize\x18\x04 \x01(\x01\x12\x11\n\tMediaType\x18\x05 \x01(\t\x12\x0f\n\x07TosKeys\x18\x06 \x01(\t\x12\x15\n\rFileExtension\x18\x07 \x01(\t\x12\x12\n\nFilePrefix\x18\x08 \x01(\t\x12\x17\n\x0f\x46lushUploadMode\x18\t \x01(\x05\x12\x0b\n\x03Md5\x18\n \x01(\t\x12\x14\n\x0cStorageClass\x18\x0b \x01(\x05\x12\x19\n\x11\x43lientNetWorkMode\x18\x65 \x01(\t\x12\x15\n\rClientIDCMode\x18\x66 \x01(\t\"\x96\x01\n\x0e\x43ommitResponse\x12\x0b\n\x03Vid\x18\x01 \x01(\t\x12\x0b\n\x03Mid\x18\x02 \x01(\t\x12\x41\n\nSourceInfo\x18\x03 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.VodSourceInfo\x12\x11\n\tPosterUri\x18\x04 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x05 \x01(\t\">\n\x11VodUploadTemplate\x12\x13\n\x0bTemplateIds\x18\x01 \x03(\t\x12\x14\n\x0cTemplateType\x18\x02 \x01(\t\"\x84\x01\n\x13VodUploadOptionInfo\x12\x12\n\nTemplateId\x18\x01 \x01(\t\x12\x13\n\x0bTemplateIds\x18\x02 \x03(\t\x12\x44\n\tTemplates\x18\x03 \x03(\x0b\x32\x31.Volcengine.Vod.Models.Business.VodUploadTemplate\"\x98\x02\n\x15VodUploadCallbackData\x12\x0c\n\x04\x43ode\x18\x01 \x01(\t\x12\x0f\n\x07Message\x18\x02 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x03 \x01(\t\x12\x0b\n\x03Vid\x18\x04 \x01(\t\x12\x0b\n\x03Mid\x18\x05 \x01(\t\x12\x11\n\tSpaceName\x18\x06 \x01(\t\x12\x41\n\nSourceInfo\x18\x07 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.VodSourceInfo\x12\x11\n\tPosterUri\x18\x08 \x01(\t\x12G\n\nOptionInfo\x18\t \x01(\x0b\x32\x33.Volcengine.Vod.Models.Business.VodUploadOptionInfo\"\xa1\x01\n\x10\x43\x61llbackResponse\x12\x11\n\tRequestId\x18\x01 \x01(\t\x12\x0f\n\x07Version\x18\x02 \x01(\t\x12\x11\n\tEventTime\x18\x03 \x01(\t\x12\x11\n\tEventType\x18\x04 \x01(\t\x12\x43\n\x04\x44\x61ta\x18\x05 \x01(\x0b\x32\x35.Volcengine.Vod.Models.Business.VodUploadCallbackData\"+\n\tStoreInfo\x12\x10\n\x08StoreUri\x18\x01 \x01(\t\x12\x0c\n\x04\x41uth\x18\x02 \x01(\t\"(\n\nHeaderPair\x12\x0b\n\x03Key\x18\x01 \x01(\t\x12\r\n\x05Value\x18\x02 \x01(\t\"\xb9\x01\n\rUploadAddress\x12=\n\nStoreInfos\x18\x01 \x03(\x0b\x32).Volcengine.Vod.Models.Business.StoreInfo\x12\x13\n\x0bUploadHosts\x18\x02 \x03(\t\x12@\n\x0cUploadHeader\x18\x03 \x03(\x0b\x32*.Volcengine.Vod.Models.Business.HeaderPair\x12\x12\n\nSessionKey\x18\x04 \x01(\t\"\xae\x01\n\x11\x46lushUploadResult\x12\x13\n\x0b\x46lushUpload\x18\x01 \x01(\x08\x12\x0b\n\x03Vid\x18\x02 \x01(\t\x12\x0b\n\x03Mid\x18\x03 \x01(\t\x12\x41\n\nSourceInfo\x18\x04 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.VodSourceInfo\x12\x11\n\tPosterUri\x18\x05 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x06 \x01(\t\"\xb5\x01\n\rApplyResponse\x12\x44\n\rUploadAddress\x18\x01 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.UploadAddress\x12L\n\x11\x46lushUploadResult\x18\x02 \x01(\x0b\x32\x31.Volcengine.Vod.Models.Business.FlushUploadResult\x12\x10\n\x08SDKParam\x18\x03 \x01(\t\"\xa7\x01\n\x19SubmitMoveObjectTaskParam\x12\x13\n\x0bSourceSpace\x18\x01 \x01(\t\x12\x16\n\x0eSourceFileName\x18\x02 \x01(\t\x12\x13\n\x0bTargetSpace\x18\x03 \x01(\t\x12\x16\n\x0eTargetFileName\x18\x04 \x01(\t\x12\x18\n\x10SaveSourceObject\x18\x05 \x01(\x08\x12\x16\n\x0e\x46orceOverwrite\x18\x06 \x01(\x08\"m\n\x1fVodSubmitMoveObjectTaskRespData\x12J\n\x04\x44\x61ta\x18\x01 \x01(\x0b\x32<.Volcengine.Vod.Models.Business.SubmitMoveObjectTaskRespData\"X\n\x1cSubmitMoveObjectTaskRespData\x12\x0e\n\x06TaskId\x18\x01 \x01(\t\x12\x13\n\x0bSourceSpace\x18\x02 \x01(\t\x12\x13\n\x0bTargetSpace\x18\x03 \x01(\t\"X\n\x1cQueryMoveObjectTaskInfoParam\x12\x0e\n\x06TaskId\x18\x01 \x01(\t\x12\x13\n\x0bSourceSpace\x18\x02 \x01(\t\x12\x13\n\x0bTargetSpace\x18\x03 \x01(\t\"r\n!VodQueryMoveObjectTaskInfoResData\x12M\n\x04\x44\x61ta\x18\x01 \x01(\x0b\x32?.Volcengine.Vod.Models.Business.QueryMoveObjectTaskInfoRespData\"\x81\x01\n\x1fQueryMoveObjectTaskInfoRespData\x12\x0e\n\x06TaskId\x18\x01 \x01(\t\x12\x13\n\x0bSourceSpace\x18\x02 \x01(\t\x12\x13\n\x0bTargetSpace\x18\x03 \x01(\t\x12\r\n\x05State\x18\x04 \x01(\t\x12\x15\n\rTaskRunResult\x18\x05 \x01(\t*B\n\x10StorageClassType\x12\x0b\n\x07\x44\x65\x66\x61ult\x10\x00\x12\x0c\n\x08Standard\x10\x01\x12\x0b\n\x07\x41rchive\x10\x02\x12\x06\n\x02IA\x10\x03\x42\xcd\x01\n)com.volcengine.service.vod.model.businessB\tVodUploadP\x01ZAgithub.com/volcengine/volc-sdk-golang/service/vod/models/business\xa0\x01\x01\xd8\x01\x01\xc2\x02\x00\xca\x02 Volc\\Service\\Vod\\Models\\Business\xe2\x02#Volc\\Service\\Vod\\Models\\GPBMetadatab\x06proto3')

_STORAGECLASSTYPE = DESCRIPTOR.enum_types_by_name['StorageClassType']
StorageClassType = enum_type_wrapper.EnumTypeWrapper(_STORAGECLASSTYPE)
Default = 0
Standard = 1
Archive = 2
IA = 3


_VODURLUPLOADURLSET = DESCRIPTOR.message_types_by_name['VodUrlUploadURLSet']
_VODURLUPLOADURLSET_CUSTOMURLHEADERSENTRY = _VODURLUPLOADURLSET.nested_types_by_name['CustomURLHeadersEntry']
_VODURLRESPONSEDATA = DESCRIPTOR.message_types_by_name['VodUrlResponseData']
_VALUEPAIR = DESCRIPTOR.message_types_by_name['ValuePair']
_VODQUERYDATA = DESCRIPTOR.message_types_by_name['VodQueryData']
_VODQUERYUPLOADRESULT = DESCRIPTOR.message_types_by_name['VodQueryUploadResult']
_VODCOMMITDATA = DESCRIPTOR.message_types_by_name['VodCommitData']
_VODCOMMITUPLOADINFORESPONSEDATA = DESCRIPTOR.message_types_by_name['VodCommitUploadInfoResponseData']
_VODURLSET = DESCRIPTOR.message_types_by_name['VodURLSet']
_VODAPPLYUPLOADINFORESULT = DESCRIPTOR.message_types_by_name['VodApplyUploadInfoResult']
_VODAPPLYUPLOADINFODATA = DESCRIPTOR.message_types_by_name['VodApplyUploadInfoData']
_VODUPLOADADDRESS = DESCRIPTOR.message_types_by_name['VodUploadAddress']
_CANDIDATEUPLOADADDRESSES = DESCRIPTOR.message_types_by_name['CandidateUploadAddresses']
_VODSTOREINFO = DESCRIPTOR.message_types_by_name['VodStoreInfo']
_VODHEADERPAIR = DESCRIPTOR.message_types_by_name['VodHeaderPair']
_VODCOMMITUPLOADINFORESULT = DESCRIPTOR.message_types_by_name['VodCommitUploadInfoResult']
_VODCOMMITUPLOADINFODATA = DESCRIPTOR.message_types_by_name['VodCommitUploadInfoData']
_VODUPLOADFUNCTIONINPUT = DESCRIPTOR.message_types_by_name['VodUploadFunctionInput']
_VODUPLOADFUNCTION = DESCRIPTOR.message_types_by_name['VodUploadFunction']
_COMMITUPLOADINFOPARAM = DESCRIPTOR.message_types_by_name['CommitUploadInfoParam']
_COMMITREQUESTBODYJSON = DESCRIPTOR.message_types_by_name['CommitRequestBodyJson']
_APPLYUPLOADINFOPARAM = DESCRIPTOR.message_types_by_name['ApplyUploadInfoParam']
_COMMITRESPONSE = DESCRIPTOR.message_types_by_name['CommitResponse']
_VODUPLOADTEMPLATE = DESCRIPTOR.message_types_by_name['VodUploadTemplate']
_VODUPLOADOPTIONINFO = DESCRIPTOR.message_types_by_name['VodUploadOptionInfo']
_VODUPLOADCALLBACKDATA = DESCRIPTOR.message_types_by_name['VodUploadCallbackData']
_CALLBACKRESPONSE = DESCRIPTOR.message_types_by_name['CallbackResponse']
_STOREINFO = DESCRIPTOR.message_types_by_name['StoreInfo']
_HEADERPAIR = DESCRIPTOR.message_types_by_name['HeaderPair']
_UPLOADADDRESS = DESCRIPTOR.message_types_by_name['UploadAddress']
_FLUSHUPLOADRESULT = DESCRIPTOR.message_types_by_name['FlushUploadResult']
_APPLYRESPONSE = DESCRIPTOR.message_types_by_name['ApplyResponse']
_SUBMITMOVEOBJECTTASKPARAM = DESCRIPTOR.message_types_by_name['SubmitMoveObjectTaskParam']
_VODSUBMITMOVEOBJECTTASKRESPDATA = DESCRIPTOR.message_types_by_name['VodSubmitMoveObjectTaskRespData']
_SUBMITMOVEOBJECTTASKRESPDATA = DESCRIPTOR.message_types_by_name['SubmitMoveObjectTaskRespData']
_QUERYMOVEOBJECTTASKINFOPARAM = DESCRIPTOR.message_types_by_name['QueryMoveObjectTaskInfoParam']
_VODQUERYMOVEOBJECTTASKINFORESDATA = DESCRIPTOR.message_types_by_name['VodQueryMoveObjectTaskInfoResData']
_QUERYMOVEOBJECTTASKINFORESPDATA = DESCRIPTOR.message_types_by_name['QueryMoveObjectTaskInfoRespData']
VodUrlUploadURLSet = _reflection.GeneratedProtocolMessageType('VodUrlUploadURLSet', (_message.Message,), {

  'CustomURLHeadersEntry' : _reflection.GeneratedProtocolMessageType('CustomURLHeadersEntry', (_message.Message,), {
    'DESCRIPTOR' : _VODURLUPLOADURLSET_CUSTOMURLHEADERSENTRY,
    '__module__' : 'volcengine.vod.business.vod_upload_pb2'
    # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUrlUploadURLSet.CustomURLHeadersEntry)
    })
  ,
  'DESCRIPTOR' : _VODURLUPLOADURLSET,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUrlUploadURLSet)
  })
_sym_db.RegisterMessage(VodUrlUploadURLSet)
_sym_db.RegisterMessage(VodUrlUploadURLSet.CustomURLHeadersEntry)

VodUrlResponseData = _reflection.GeneratedProtocolMessageType('VodUrlResponseData', (_message.Message,), {
  'DESCRIPTOR' : _VODURLRESPONSEDATA,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUrlResponseData)
  })
_sym_db.RegisterMessage(VodUrlResponseData)

ValuePair = _reflection.GeneratedProtocolMessageType('ValuePair', (_message.Message,), {
  'DESCRIPTOR' : _VALUEPAIR,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.ValuePair)
  })
_sym_db.RegisterMessage(ValuePair)

VodQueryData = _reflection.GeneratedProtocolMessageType('VodQueryData', (_message.Message,), {
  'DESCRIPTOR' : _VODQUERYDATA,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodQueryData)
  })
_sym_db.RegisterMessage(VodQueryData)

VodQueryUploadResult = _reflection.GeneratedProtocolMessageType('VodQueryUploadResult', (_message.Message,), {
  'DESCRIPTOR' : _VODQUERYUPLOADRESULT,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodQueryUploadResult)
  })
_sym_db.RegisterMessage(VodQueryUploadResult)

VodCommitData = _reflection.GeneratedProtocolMessageType('VodCommitData', (_message.Message,), {
  'DESCRIPTOR' : _VODCOMMITDATA,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCommitData)
  })
_sym_db.RegisterMessage(VodCommitData)

VodCommitUploadInfoResponseData = _reflection.GeneratedProtocolMessageType('VodCommitUploadInfoResponseData', (_message.Message,), {
  'DESCRIPTOR' : _VODCOMMITUPLOADINFORESPONSEDATA,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCommitUploadInfoResponseData)
  })
_sym_db.RegisterMessage(VodCommitUploadInfoResponseData)

VodURLSet = _reflection.GeneratedProtocolMessageType('VodURLSet', (_message.Message,), {
  'DESCRIPTOR' : _VODURLSET,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodURLSet)
  })
_sym_db.RegisterMessage(VodURLSet)

VodApplyUploadInfoResult = _reflection.GeneratedProtocolMessageType('VodApplyUploadInfoResult', (_message.Message,), {
  'DESCRIPTOR' : _VODAPPLYUPLOADINFORESULT,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodApplyUploadInfoResult)
  })
_sym_db.RegisterMessage(VodApplyUploadInfoResult)

VodApplyUploadInfoData = _reflection.GeneratedProtocolMessageType('VodApplyUploadInfoData', (_message.Message,), {
  'DESCRIPTOR' : _VODAPPLYUPLOADINFODATA,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodApplyUploadInfoData)
  })
_sym_db.RegisterMessage(VodApplyUploadInfoData)

VodUploadAddress = _reflection.GeneratedProtocolMessageType('VodUploadAddress', (_message.Message,), {
  'DESCRIPTOR' : _VODUPLOADADDRESS,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUploadAddress)
  })
_sym_db.RegisterMessage(VodUploadAddress)

CandidateUploadAddresses = _reflection.GeneratedProtocolMessageType('CandidateUploadAddresses', (_message.Message,), {
  'DESCRIPTOR' : _CANDIDATEUPLOADADDRESSES,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.CandidateUploadAddresses)
  })
_sym_db.RegisterMessage(CandidateUploadAddresses)

VodStoreInfo = _reflection.GeneratedProtocolMessageType('VodStoreInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODSTOREINFO,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodStoreInfo)
  })
_sym_db.RegisterMessage(VodStoreInfo)

VodHeaderPair = _reflection.GeneratedProtocolMessageType('VodHeaderPair', (_message.Message,), {
  'DESCRIPTOR' : _VODHEADERPAIR,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodHeaderPair)
  })
_sym_db.RegisterMessage(VodHeaderPair)

VodCommitUploadInfoResult = _reflection.GeneratedProtocolMessageType('VodCommitUploadInfoResult', (_message.Message,), {
  'DESCRIPTOR' : _VODCOMMITUPLOADINFORESULT,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCommitUploadInfoResult)
  })
_sym_db.RegisterMessage(VodCommitUploadInfoResult)

VodCommitUploadInfoData = _reflection.GeneratedProtocolMessageType('VodCommitUploadInfoData', (_message.Message,), {
  'DESCRIPTOR' : _VODCOMMITUPLOADINFODATA,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCommitUploadInfoData)
  })
_sym_db.RegisterMessage(VodCommitUploadInfoData)

VodUploadFunctionInput = _reflection.GeneratedProtocolMessageType('VodUploadFunctionInput', (_message.Message,), {
  'DESCRIPTOR' : _VODUPLOADFUNCTIONINPUT,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUploadFunctionInput)
  })
_sym_db.RegisterMessage(VodUploadFunctionInput)

VodUploadFunction = _reflection.GeneratedProtocolMessageType('VodUploadFunction', (_message.Message,), {
  'DESCRIPTOR' : _VODUPLOADFUNCTION,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUploadFunction)
  })
_sym_db.RegisterMessage(VodUploadFunction)

CommitUploadInfoParam = _reflection.GeneratedProtocolMessageType('CommitUploadInfoParam', (_message.Message,), {
  'DESCRIPTOR' : _COMMITUPLOADINFOPARAM,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.CommitUploadInfoParam)
  })
_sym_db.RegisterMessage(CommitUploadInfoParam)

CommitRequestBodyJson = _reflection.GeneratedProtocolMessageType('CommitRequestBodyJson', (_message.Message,), {
  'DESCRIPTOR' : _COMMITREQUESTBODYJSON,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.CommitRequestBodyJson)
  })
_sym_db.RegisterMessage(CommitRequestBodyJson)

ApplyUploadInfoParam = _reflection.GeneratedProtocolMessageType('ApplyUploadInfoParam', (_message.Message,), {
  'DESCRIPTOR' : _APPLYUPLOADINFOPARAM,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.ApplyUploadInfoParam)
  })
_sym_db.RegisterMessage(ApplyUploadInfoParam)

CommitResponse = _reflection.GeneratedProtocolMessageType('CommitResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMMITRESPONSE,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.CommitResponse)
  })
_sym_db.RegisterMessage(CommitResponse)

VodUploadTemplate = _reflection.GeneratedProtocolMessageType('VodUploadTemplate', (_message.Message,), {
  'DESCRIPTOR' : _VODUPLOADTEMPLATE,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUploadTemplate)
  })
_sym_db.RegisterMessage(VodUploadTemplate)

VodUploadOptionInfo = _reflection.GeneratedProtocolMessageType('VodUploadOptionInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODUPLOADOPTIONINFO,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUploadOptionInfo)
  })
_sym_db.RegisterMessage(VodUploadOptionInfo)

VodUploadCallbackData = _reflection.GeneratedProtocolMessageType('VodUploadCallbackData', (_message.Message,), {
  'DESCRIPTOR' : _VODUPLOADCALLBACKDATA,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUploadCallbackData)
  })
_sym_db.RegisterMessage(VodUploadCallbackData)

CallbackResponse = _reflection.GeneratedProtocolMessageType('CallbackResponse', (_message.Message,), {
  'DESCRIPTOR' : _CALLBACKRESPONSE,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.CallbackResponse)
  })
_sym_db.RegisterMessage(CallbackResponse)

StoreInfo = _reflection.GeneratedProtocolMessageType('StoreInfo', (_message.Message,), {
  'DESCRIPTOR' : _STOREINFO,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.StoreInfo)
  })
_sym_db.RegisterMessage(StoreInfo)

HeaderPair = _reflection.GeneratedProtocolMessageType('HeaderPair', (_message.Message,), {
  'DESCRIPTOR' : _HEADERPAIR,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.HeaderPair)
  })
_sym_db.RegisterMessage(HeaderPair)

UploadAddress = _reflection.GeneratedProtocolMessageType('UploadAddress', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADADDRESS,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.UploadAddress)
  })
_sym_db.RegisterMessage(UploadAddress)

FlushUploadResult = _reflection.GeneratedProtocolMessageType('FlushUploadResult', (_message.Message,), {
  'DESCRIPTOR' : _FLUSHUPLOADRESULT,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.FlushUploadResult)
  })
_sym_db.RegisterMessage(FlushUploadResult)

ApplyResponse = _reflection.GeneratedProtocolMessageType('ApplyResponse', (_message.Message,), {
  'DESCRIPTOR' : _APPLYRESPONSE,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.ApplyResponse)
  })
_sym_db.RegisterMessage(ApplyResponse)

SubmitMoveObjectTaskParam = _reflection.GeneratedProtocolMessageType('SubmitMoveObjectTaskParam', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITMOVEOBJECTTASKPARAM,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.SubmitMoveObjectTaskParam)
  })
_sym_db.RegisterMessage(SubmitMoveObjectTaskParam)

VodSubmitMoveObjectTaskRespData = _reflection.GeneratedProtocolMessageType('VodSubmitMoveObjectTaskRespData', (_message.Message,), {
  'DESCRIPTOR' : _VODSUBMITMOVEOBJECTTASKRESPDATA,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodSubmitMoveObjectTaskRespData)
  })
_sym_db.RegisterMessage(VodSubmitMoveObjectTaskRespData)

SubmitMoveObjectTaskRespData = _reflection.GeneratedProtocolMessageType('SubmitMoveObjectTaskRespData', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITMOVEOBJECTTASKRESPDATA,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.SubmitMoveObjectTaskRespData)
  })
_sym_db.RegisterMessage(SubmitMoveObjectTaskRespData)

QueryMoveObjectTaskInfoParam = _reflection.GeneratedProtocolMessageType('QueryMoveObjectTaskInfoParam', (_message.Message,), {
  'DESCRIPTOR' : _QUERYMOVEOBJECTTASKINFOPARAM,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.QueryMoveObjectTaskInfoParam)
  })
_sym_db.RegisterMessage(QueryMoveObjectTaskInfoParam)

VodQueryMoveObjectTaskInfoResData = _reflection.GeneratedProtocolMessageType('VodQueryMoveObjectTaskInfoResData', (_message.Message,), {
  'DESCRIPTOR' : _VODQUERYMOVEOBJECTTASKINFORESDATA,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodQueryMoveObjectTaskInfoResData)
  })
_sym_db.RegisterMessage(VodQueryMoveObjectTaskInfoResData)

QueryMoveObjectTaskInfoRespData = _reflection.GeneratedProtocolMessageType('QueryMoveObjectTaskInfoRespData', (_message.Message,), {
  'DESCRIPTOR' : _QUERYMOVEOBJECTTASKINFORESPDATA,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.QueryMoveObjectTaskInfoRespData)
  })
_sym_db.RegisterMessage(QueryMoveObjectTaskInfoRespData)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n)com.volcengine.service.vod.model.businessB\tVodUploadP\001ZAgithub.com/volcengine/volc-sdk-golang/service/vod/models/business\240\001\001\330\001\001\302\002\000\312\002 Volc\\Service\\Vod\\Models\\Business\342\002#Volc\\Service\\Vod\\Models\\GPBMetadata'
  _VODURLUPLOADURLSET_CUSTOMURLHEADERSENTRY._options = None
  _VODURLUPLOADURLSET_CUSTOMURLHEADERSENTRY._serialized_options = b'8\001'
  _STORAGECLASSTYPE._serialized_start=5894
  _STORAGECLASSTYPE._serialized_end=5960
  _VODURLUPLOADURLSET._serialized_start=119
  _VODURLUPLOADURLSET._serialized_end=656
  _VODURLUPLOADURLSET_CUSTOMURLHEADERSENTRY._serialized_start=601
  _VODURLUPLOADURLSET_CUSTOMURLHEADERSENTRY._serialized_end=656
  _VODURLRESPONSEDATA._serialized_start=658
  _VODURLRESPONSEDATA._serialized_end=735
  _VALUEPAIR._serialized_start=737
  _VALUEPAIR._serialized_end=782
  _VODQUERYDATA._serialized_start=784
  _VODQUERYDATA._serialized_end=866
  _VODQUERYUPLOADRESULT._serialized_start=868
  _VODQUERYUPLOADRESULT._serialized_end=980
  _VODCOMMITDATA._serialized_start=982
  _VODCOMMITDATA._serialized_end=1076
  _VODCOMMITUPLOADINFORESPONSEDATA._serialized_start=1079
  _VODCOMMITUPLOADINFORESPONSEDATA._serialized_end=1246
  _VODURLSET._serialized_start=1249
  _VODURLSET._serialized_end=1468
  _VODAPPLYUPLOADINFORESULT._serialized_start=1470
  _VODAPPLYUPLOADINFORESULT._serialized_end=1566
  _VODAPPLYUPLOADINFODATA._serialized_start=1569
  _VODAPPLYUPLOADINFODATA._serialized_end=1758
  _VODUPLOADADDRESS._serialized_start=1761
  _VODUPLOADADDRESS._serialized_end=1955
  _CANDIDATEUPLOADADDRESSES._serialized_start=1958
  _CANDIDATEUPLOADADDRESSES._serialized_end=2218
  _VODSTOREINFO._serialized_start=2220
  _VODSTOREINFO._serialized_end=2266
  _VODHEADERPAIR._serialized_start=2268
  _VODHEADERPAIR._serialized_end=2311
  _VODCOMMITUPLOADINFORESULT._serialized_start=2313
  _VODCOMMITUPLOADINFORESULT._serialized_end=2411
  _VODCOMMITUPLOADINFODATA._serialized_start=2414
  _VODCOMMITUPLOADINFODATA._serialized_end=2551
  _VODUPLOADFUNCTIONINPUT._serialized_start=2554
  _VODUPLOADFUNCTIONINPUT._serialized_end=2998
  _VODUPLOADFUNCTION._serialized_start=3000
  _VODUPLOADFUNCTION._serialized_end=3104
  _COMMITUPLOADINFOPARAM._serialized_start=3107
  _COMMITUPLOADINFOPARAM._serialized_end=3307
  _COMMITREQUESTBODYJSON._serialized_start=3310
  _COMMITREQUESTBODYJSON._serialized_end=3459
  _APPLYUPLOADINFOPARAM._serialized_start=3462
  _APPLYUPLOADINFOPARAM._serialized_end=3748
  _COMMITRESPONSE._serialized_start=3751
  _COMMITRESPONSE._serialized_end=3901
  _VODUPLOADTEMPLATE._serialized_start=3903
  _VODUPLOADTEMPLATE._serialized_end=3965
  _VODUPLOADOPTIONINFO._serialized_start=3968
  _VODUPLOADOPTIONINFO._serialized_end=4100
  _VODUPLOADCALLBACKDATA._serialized_start=4103
  _VODUPLOADCALLBACKDATA._serialized_end=4383
  _CALLBACKRESPONSE._serialized_start=4386
  _CALLBACKRESPONSE._serialized_end=4547
  _STOREINFO._serialized_start=4549
  _STOREINFO._serialized_end=4592
  _HEADERPAIR._serialized_start=4594
  _HEADERPAIR._serialized_end=4634
  _UPLOADADDRESS._serialized_start=4637
  _UPLOADADDRESS._serialized_end=4822
  _FLUSHUPLOADRESULT._serialized_start=4825
  _FLUSHUPLOADRESULT._serialized_end=4999
  _APPLYRESPONSE._serialized_start=5002
  _APPLYRESPONSE._serialized_end=5183
  _SUBMITMOVEOBJECTTASKPARAM._serialized_start=5186
  _SUBMITMOVEOBJECTTASKPARAM._serialized_end=5353
  _VODSUBMITMOVEOBJECTTASKRESPDATA._serialized_start=5355
  _VODSUBMITMOVEOBJECTTASKRESPDATA._serialized_end=5464
  _SUBMITMOVEOBJECTTASKRESPDATA._serialized_start=5466
  _SUBMITMOVEOBJECTTASKRESPDATA._serialized_end=5554
  _QUERYMOVEOBJECTTASKINFOPARAM._serialized_start=5556
  _QUERYMOVEOBJECTTASKINFOPARAM._serialized_end=5644
  _VODQUERYMOVEOBJECTTASKINFORESDATA._serialized_start=5646
  _VODQUERYMOVEOBJECTTASKINFORESDATA._serialized_end=5760
  _QUERYMOVEOBJECTTASKINFORESPDATA._serialized_start=5763
  _QUERYMOVEOBJECTTASKINFORESPDATA._serialized_end=5892
# @@protoc_insertion_point(module_scope)
