# coding:utf-8
from __future__ import print_function

from volcengine.vod.VodService import VodService
from volcengine.vod.models.request.request_vod_pb2 import VodUpdateDomainUrlAuthConfigV2Request

if __name__ == '__main__':
    # Create a VOD instance in the specified region.
    # vod_service = VodService('cn-north-1')
    vod_service = VodService()

    # Configure your Access Key ID (AK) and Secret Access Key (SK) in the environment variables or in the local ~/.volc/config file. For detailed instructions, see https://www.volcengine.com/docs/4/65646.
    # The SDK will automatically fetch the AK and SK from the environment variables or the ~/.volc/config file as needed.
    # During testing, you may use the following code snippet. However, do not store the AK and SK directly in your project code to prevent potential leakage and safeguard the security of all resources associated with your account.
    # vod_service.set_ak('your ak')
    # vod_service.set_sk('your sk')

    try:
        req = VodUpdateDomainUrlAuthConfigV2Request()
        req.SpaceName = 'your space name'
        req.DomainType= 'your DomainType'
        req.Domain    = 'your Domain'
        req.MainKey   = 'your MainKey'
        req.BackupKey = 'your BackupKey'
        req.Status    = 'your Status'
        resp = vod_service.update_domain_url_auth_config(req)
    except Exception:
        raise
    else:
        print(resp)
        if resp.ResponseMetadata.Error.Code != '':
            print(resp.ResponseMetadata.Error)
