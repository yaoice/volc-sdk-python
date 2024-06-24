# coding:utf-8

from volcengine.ServiceInfo import ServiceInfo
from volcengine.Credentials import Credentials
from volcengine.ApiInfo import ApiInfo

service_info_map = {
    'cn-north-1': ServiceInfo(
        'live.volcengineapi.com',
        {'Accept': 'application/json'},
        Credentials('', '', 'live', 'cn-north-1'),
        10, 10, "https")
}

api_info = {
    "DeleteTranscodePreset": ApiInfo("POST", "/", {"Action": "DeleteTranscodePreset", "Version": "2023-01-01"}, {}, {}),
    "UpdateTranscodePreset": ApiInfo("POST", "/", {"Action": "UpdateTranscodePreset", "Version": "2023-01-01"}, {}, {}),
    "ListCommonTransPresetDetail": ApiInfo("POST", "/", {"Action": "ListCommonTransPresetDetail", "Version": "2023-01-01"}, {}, {}),
    "TranscodingJobStatus": ApiInfo("GET", "/", {"Action": "TranscodingJobStatus", "Version": "2023-01-01"}, {}, {}),
    "ListVhostTransCodePreset": ApiInfo("POST", "/", {"Action": "ListVhostTransCodePreset", "Version": "2023-01-01"}, {}, {}),
    "CreateTranscodePreset": ApiInfo("POST", "/", {"Action": "CreateTranscodePreset", "Version": "2023-01-01"}, {}, {}),
    "RestartTranscodingJob": ApiInfo("GET", "/", {"Action": "RestartTranscodingJob", "Version": "2023-01-01"}, {}, {}),
    "CreateWatermarkPreset": ApiInfo("POST", "/", {"Action": "CreateWatermarkPreset", "Version": "2023-01-01"}, {}, {}),
    "UpdateWatermarkPreset": ApiInfo("POST", "/", {"Action": "UpdateWatermarkPreset", "Version": "2023-01-01"}, {}, {}),
    "DeleteWatermarkPreset": ApiInfo("POST", "/", {"Action": "DeleteWatermarkPreset", "Version": "2023-01-01"}, {}, {}),
    "ListWatermarkPreset": ApiInfo("POST", "/", {"Action": "ListWatermarkPreset", "Version": "2023-01-01"}, {}, {}),
    "ListVhostWatermarkPreset": ApiInfo("POST", "/", {"Action": "ListVhostWatermarkPreset", "Version": "2023-01-01"}, {}, {}),
    "StopPullRecordTask": ApiInfo("POST", "/", {"Action": "StopPullRecordTask", "Version": "2023-01-01"}, {}, {}),
    "CreateLiveStreamRecordIndexFiles": ApiInfo("POST", "/", {"Action": "CreateLiveStreamRecordIndexFiles", "Version": "2023-01-01"}, {}, {}),
    "CreatePullRecordTask": ApiInfo("POST", "/", {"Action": "CreatePullRecordTask", "Version": "2023-01-01"}, {}, {}),
    "DeleteRecordPreset": ApiInfo("POST", "/", {"Action": "DeleteRecordPreset", "Version": "2023-01-01"}, {}, {}),
    "UpdateRecordPresetV2": ApiInfo("POST", "/", {"Action": "UpdateRecordPresetV2", "Version": "2023-01-01"}, {}, {}),
    "GetPullRecordTask": ApiInfo("POST", "/", {"Action": "GetPullRecordTask", "Version": "2023-01-01"}, {}, {}),
    "DescribeRecordTaskFileHistory": ApiInfo("POST", "/", {"Action": "DescribeRecordTaskFileHistory", "Version": "2023-01-01"}, {}, {}),
    "ListVhostRecordPresetV2": ApiInfo("POST", "/", {"Action": "ListVhostRecordPresetV2", "Version": "2023-01-01"}, {}, {}),
    "ListPullRecordTask": ApiInfo("POST", "/", {"Action": "ListPullRecordTask", "Version": "2023-01-01"}, {}, {}),
    "CreateRecordPresetV2": ApiInfo("POST", "/", {"Action": "CreateRecordPresetV2", "Version": "2023-01-01"}, {}, {}),
    "DeleteSnapshotPreset": ApiInfo("POST", "/", {"Action": "DeleteSnapshotPreset", "Version": "2023-01-01"}, {}, {}),
    "UpdateSnapshotPresetV2": ApiInfo("POST", "/", {"Action": "UpdateSnapshotPresetV2", "Version": "2023-01-01"}, {}, {}),
    "UpdateSnapshotPreset": ApiInfo("POST", "/", {"Action": "UpdateSnapshotPreset", "Version": "2023-01-01"}, {}, {}),
    "DescribeCDNSnapshotHistory": ApiInfo("POST", "/", {"Action": "DescribeCDNSnapshotHistory", "Version": "2023-01-01"}, {}, {}),
    "ListVhostSnapshotPresetV2": ApiInfo("POST", "/", {"Action": "ListVhostSnapshotPresetV2", "Version": "2023-01-01"}, {}, {}),
    "ListVhostSnapshotPreset": ApiInfo("POST", "/", {"Action": "ListVhostSnapshotPreset", "Version": "2023-01-01"}, {}, {}),
    "CreateSnapshotPresetV2": ApiInfo("POST", "/", {"Action": "CreateSnapshotPresetV2", "Version": "2023-01-01"}, {}, {}),
    "CreateSnapshotPreset": ApiInfo("POST", "/", {"Action": "CreateSnapshotPreset", "Version": "2023-01-01"}, {}, {}),
    "DeleteTimeShiftPresetV3": ApiInfo("POST", "/", {"Action": "DeleteTimeShiftPresetV3", "Version": "2023-01-01"}, {}, {}),
    "UpdateTimeShiftPresetV3": ApiInfo("POST", "/", {"Action": "UpdateTimeShiftPresetV3", "Version": "2023-01-01"}, {}, {}),
    "ListTimeShiftPresetV2": ApiInfo("POST", "/", {"Action": "ListTimeShiftPresetV2", "Version": "2023-01-01"}, {}, {}),
    "CreateTimeShiftPresetV3": ApiInfo("POST", "/", {"Action": "CreateTimeShiftPresetV3", "Version": "2023-01-01"}, {}, {}),
    "DeleteCallback": ApiInfo("POST", "/", {"Action": "DeleteCallback", "Version": "2023-01-01"}, {}, {}),
    "DescribeCallback": ApiInfo("POST", "/", {"Action": "DescribeCallback", "Version": "2023-01-01"}, {}, {}),
    "UpdateCallback": ApiInfo("POST", "/", {"Action": "UpdateCallback", "Version": "2023-01-01"}, {}, {}),
    "DeleteCert": ApiInfo("POST", "/", {"Action": "DeleteCert", "Version": "2023-01-01"}, {}, {}),
    "DescribeCertDetailSecretV2": ApiInfo("POST", "/", {"Action": "DescribeCertDetailSecretV2", "Version": "2023-01-01"}, {}, {}),
    "ListCertV2": ApiInfo("POST", "/", {"Action": "ListCertV2", "Version": "2023-01-01"}, {}, {}),
    "CreateCert": ApiInfo("POST", "/", {"Action": "CreateCert", "Version": "2023-01-01"}, {}, {}),
    "BindCert": ApiInfo("POST", "/", {"Action": "BindCert", "Version": "2023-01-01"}, {}, {}),
    "UnbindCert": ApiInfo("POST", "/", {"Action": "UnbindCert", "Version": "2023-01-01"}, {}, {}),
    "DeleteDomain": ApiInfo("POST", "/", {"Action": "DeleteDomain", "Version": "2023-01-01"}, {}, {}),
    "EnableDomain": ApiInfo("POST", "/", {"Action": "EnableDomain", "Version": "2023-01-01"}, {}, {}),
    "CreateDomainV2": ApiInfo("POST", "/", {"Action": "CreateDomainV2", "Version": "2023-01-01"}, {}, {}),
    "UpdateDomainVhost": ApiInfo("POST", "/", {"Action": "UpdateDomainVhost", "Version": "2023-01-01"}, {}, {}),
    "DescribeDomain": ApiInfo("POST", "/", {"Action": "DescribeDomain", "Version": "2023-01-01"}, {}, {}),
    "ListDomainDetail": ApiInfo("POST", "/", {"Action": "ListDomainDetail", "Version": "2023-01-01"}, {}, {}),
    "CreateDomain": ApiInfo("POST", "/", {"Action": "CreateDomain", "Version": "2023-01-01"}, {}, {}),
    "DisableDomain": ApiInfo("POST", "/", {"Action": "DisableDomain", "Version": "2023-01-01"}, {}, {}),
    "StopPullToPushTask": ApiInfo("POST", "/", {"Action": "StopPullToPushTask", "Version": "2023-01-01"}, {}, {}),
    "CreatePullToPushTask": ApiInfo("POST", "/", {"Action": "CreatePullToPushTask", "Version": "2023-01-01"}, {}, {}),
    "DeletePullToPushTask": ApiInfo("POST", "/", {"Action": "DeletePullToPushTask", "Version": "2023-01-01"}, {}, {}),
    "RestartPullToPushTask": ApiInfo("POST", "/", {"Action": "RestartPullToPushTask", "Version": "2023-01-01"}, {}, {}),
    "UpdatePullToPushTask": ApiInfo("POST", "/", {"Action": "UpdatePullToPushTask", "Version": "2023-01-01"}, {}, {}),
    "ListPullToPushTask": ApiInfo("GET", "/", {"Action": "ListPullToPushTask", "Version": "2023-01-01"}, {}, {}),
    "DeleteRelaySourceV4": ApiInfo("POST", "/", {"Action": "DeleteRelaySourceV4", "Version": "2023-01-01"}, {}, {}),
    "DeleteRelaySourceV3": ApiInfo("POST", "/", {"Action": "DeleteRelaySourceV3", "Version": "2023-01-01"}, {}, {}),
    "UpdateRelaySourceV4": ApiInfo("POST", "/", {"Action": "UpdateRelaySourceV4", "Version": "2023-01-01"}, {}, {}),
    "ListRelaySourceV4": ApiInfo("POST", "/", {"Action": "ListRelaySourceV4", "Version": "2023-01-01"}, {}, {}),
    "DescribeRelaySourceV3": ApiInfo("POST", "/", {"Action": "DescribeRelaySourceV3", "Version": "2023-01-01"}, {}, {}),
    "CreateRelaySourceV4": ApiInfo("POST", "/", {"Action": "CreateRelaySourceV4", "Version": "2023-01-01"}, {}, {}),
    "UpdateRelaySourceV3": ApiInfo("POST", "/", {"Action": "UpdateRelaySourceV3", "Version": "2023-01-01"}, {}, {}),
    "KillStream": ApiInfo("POST", "/", {"Action": "KillStream", "Version": "2023-01-01"}, {}, {}),
    "DescribeClosedStreamInfoByPage": ApiInfo("GET", "/", {"Action": "DescribeClosedStreamInfoByPage", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveStreamInfoByPage": ApiInfo("GET", "/", {"Action": "DescribeLiveStreamInfoByPage", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveStreamState": ApiInfo("GET", "/", {"Action": "DescribeLiveStreamState", "Version": "2023-01-01"}, {}, {}),
    "DescribeForbiddenStreamInfoByPage": ApiInfo("GET", "/", {"Action": "DescribeForbiddenStreamInfoByPage", "Version": "2023-01-01"}, {}, {}),
    "ForbidStream": ApiInfo("POST", "/", {"Action": "ForbidStream", "Version": "2023-01-01"}, {}, {}),
    "ResumeStream": ApiInfo("POST", "/", {"Action": "ResumeStream", "Version": "2023-01-01"}, {}, {}),
    "GeneratePlayURL": ApiInfo("POST", "/", {"Action": "GeneratePlayURL", "Version": "2023-01-01"}, {}, {}),
    "GeneratePushURL": ApiInfo("POST", "/", {"Action": "GeneratePushURL", "Version": "2023-01-01"}, {}, {}),
    "DeleteStreamQuotaConfig": ApiInfo("POST", "/", {"Action": "DeleteStreamQuotaConfig", "Version": "2023-01-01"}, {}, {}),
    "DescribeStreamQuotaConfig": ApiInfo("POST", "/", {"Action": "DescribeStreamQuotaConfig", "Version": "2023-01-01"}, {}, {}),
    "UpdateStreamQuotaConfig": ApiInfo("POST", "/", {"Action": "UpdateStreamQuotaConfig", "Version": "2023-01-01"}, {}, {}),
    "DeleteSnapshotAuditPreset": ApiInfo("POST", "/", {"Action": "DeleteSnapshotAuditPreset", "Version": "2023-01-01"}, {}, {}),
    "UpdateSnapshotAuditPreset": ApiInfo("POST", "/", {"Action": "UpdateSnapshotAuditPreset", "Version": "2023-01-01"}, {}, {}),
    "ListVhostSnapshotAuditPreset": ApiInfo("POST", "/", {"Action": "ListVhostSnapshotAuditPreset", "Version": "2023-01-01"}, {}, {}),
    "CreateSnapshotAuditPreset": ApiInfo("POST", "/", {"Action": "CreateSnapshotAuditPreset", "Version": "2023-01-01"}, {}, {}),
    "DescribeIpInfo": ApiInfo("POST", "/", {"Action": "DescribeIpInfo", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveRegionData": ApiInfo("POST", "/", {"Action": "DescribeLiveRegionData", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveSourceStreamMetrics": ApiInfo("POST", "/", {"Action": "DescribeLiveSourceStreamMetrics", "Version": "2023-01-01"}, {}, {}),
    "DescribeLivePushStreamMetrics": ApiInfo("POST", "/", {"Action": "DescribeLivePushStreamMetrics", "Version": "2023-01-01"}, {}, {}),
    "DescribeLivePlayStatusCodeData": ApiInfo("POST", "/", {"Action": "DescribeLivePlayStatusCodeData", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveBatchSourceStreamMetrics": ApiInfo("POST", "/", {"Action": "DescribeLiveBatchSourceStreamMetrics", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveBatchSourceStreamAvgMetrics": ApiInfo("POST", "/", {"Action": "DescribeLiveBatchSourceStreamAvgMetrics", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveBatchPushStreamMetrics": ApiInfo("POST", "/", {"Action": "DescribeLiveBatchPushStreamMetrics", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveBatchPushStreamAvgMetrics": ApiInfo("POST", "/", {"Action": "DescribeLiveBatchPushStreamAvgMetrics", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveStreamCountData": ApiInfo("POST", "/", {"Action": "DescribeLiveStreamCountData", "Version": "2023-01-01"}, {}, {}),
    "DescribeLivePushStreamCountData": ApiInfo("POST", "/", {"Action": "DescribeLivePushStreamCountData", "Version": "2023-01-01"}, {}, {}),
    "DescribeLivePushStreamInfoData": ApiInfo("POST", "/", {"Action": "DescribeLivePushStreamInfoData", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveTranscodeInfoData": ApiInfo("POST", "/", {"Action": "DescribeLiveTranscodeInfoData", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveSourceBandwidthData": ApiInfo("POST", "/", {"Action": "DescribeLiveSourceBandwidthData", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveSourceTrafficData": ApiInfo("POST", "/", {"Action": "DescribeLiveSourceTrafficData", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveMetricBandwidthData": ApiInfo("POST", "/", {"Action": "DescribeLiveMetricBandwidthData", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveMetricTrafficData": ApiInfo("POST", "/", {"Action": "DescribeLiveMetricTrafficData", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveStreamSessionData": ApiInfo("POST", "/", {"Action": "DescribeLiveStreamSessionData", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveISPData": ApiInfo("POST", "/", {"Action": "DescribeLiveISPData", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveP95PeakBandwidthData": ApiInfo("POST", "/", {"Action": "DescribeLiveP95PeakBandwidthData", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveAuditData": ApiInfo("POST", "/", {"Action": "DescribeLiveAuditData", "Version": "2023-01-01"}, {}, {}),
    "DescribeLivePullToPushBandwidthData": ApiInfo("POST", "/", {"Action": "DescribeLivePullToPushBandwidthData", "Version": "2023-01-01"}, {}, {}),
    "DescribeLivePullToPushData": ApiInfo("POST", "/", {"Action": "DescribeLivePullToPushData", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveBandwidthData": ApiInfo("POST", "/", {"Action": "DescribeLiveBandwidthData", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveRecordData": ApiInfo("POST", "/", {"Action": "DescribeLiveRecordData", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveSnapshotData": ApiInfo("POST", "/", {"Action": "DescribeLiveSnapshotData", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveTrafficData": ApiInfo("POST", "/", {"Action": "DescribeLiveTrafficData", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveTranscodeData": ApiInfo("POST", "/", {"Action": "DescribeLiveTranscodeData", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveTimeShiftData": ApiInfo("POST", "/", {"Action": "DescribeLiveTimeShiftData", "Version": "2023-01-01"}, {}, {}),
    "DescribeLiveLogData": ApiInfo("POST", "/", {"Action": "DescribeLiveLogData", "Version": "2023-01-01"}, {}, {}),
    "DeleteReferer": ApiInfo("POST", "/", {"Action": "DeleteReferer", "Version": "2023-01-01"}, {}, {}),
    "DescribeDenyConfig": ApiInfo("POST", "/", {"Action": "DescribeDenyConfig", "Version": "2023-01-01"}, {}, {}),
    "DescribeReferer": ApiInfo("POST", "/", {"Action": "DescribeReferer", "Version": "2023-01-01"}, {}, {}),
    "DescribeAuth": ApiInfo("POST", "/", {"Action": "DescribeAuth", "Version": "2023-01-01"}, {}, {}),
    "UpdateDenyConfig": ApiInfo("POST", "/", {"Action": "UpdateDenyConfig", "Version": "2023-01-01"}, {}, {}),
    "UpdateReferer": ApiInfo("POST", "/", {"Action": "UpdateReferer", "Version": "2023-01-01"}, {}, {}),
    "UpdateAuthKey": ApiInfo("POST", "/", {"Action": "UpdateAuthKey", "Version": "2023-01-01"}, {}, {}),
    "DeleteHTTPHeaderConfig": ApiInfo("POST", "/", {"Action": "DeleteHTTPHeaderConfig", "Version": "2023-01-01"}, {}, {}),
    "EnableHTTPHeaderConfig": ApiInfo("POST", "/", {"Action": "EnableHTTPHeaderConfig", "Version": "2023-01-01"}, {}, {}),
    "DescribeHTTPHeaderConfig": ApiInfo("POST", "/", {"Action": "DescribeHTTPHeaderConfig", "Version": "2023-01-01"}, {}, {}),
    "UpdateHTTPHeaderConfig": ApiInfo("POST", "/", {"Action": "UpdateHTTPHeaderConfig", "Version": "2023-01-01"}, {}, {}),
    "UpdateEncryptDRM": ApiInfo("POST", "/", {"Action": "UpdateEncryptDRM", "Version": "2023-01-01"}, {}, {}),
    "DescribeLicenseDRM": ApiInfo("POST", "/", {"Action": "DescribeLicenseDRM", "Version": "2023-01-01"}, {}, {}),
    "DescribeCertDRM": ApiInfo("GET", "/", {"Action": "DescribeCertDRM", "Version": "2023-01-01"}, {}, {}),
    "DescribeEncryptDRM": ApiInfo("POST", "/", {"Action": "DescribeEncryptDRM", "Version": "2023-01-01"}, {}, {}),
    "BindEncryptDRM": ApiInfo("POST", "/", {"Action": "BindEncryptDRM", "Version": "2023-01-01"}, {}, {}),
    "UnBindEncryptDRM": ApiInfo("POST", "/", {"Action": "UnBindEncryptDRM", "Version": "2023-01-01"}, {}, {}),
    "ListBindEncryptDRM": ApiInfo("POST", "/", {"Action": "ListBindEncryptDRM", "Version": "2023-01-01"}, {}, {}),
    "DeleteIPAccessRule": ApiInfo("POST", "/", {"Action": "DeleteIPAccessRule", "Version": "2023-01-01"}, {}, {}),
    "UpdateIPAccessRule": ApiInfo("POST", "/", {"Action": "UpdateIPAccessRule", "Version": "2023-01-01"}, {}, {}),
    "DescribeIPAccessRule": ApiInfo("POST", "/", {"Action": "DescribeIPAccessRule", "Version": "2023-01-01"}, {}, {})
}