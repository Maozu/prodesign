from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.iai.v20180301 import iai_client, models


def getres(url):
    try:
        cred = credential.Credential("AKIDSmxtbmRO0Pn45tqeeZHjW6SZXFpLZbOy", "UmodLn1ziCbkkX5U1MRM4a3GQOAnwrV6")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "iai.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = iai_client.IaiClient(cred, "ap-chongqing", clientProfile)
        req = models.SearchFacesRequest()
        params = '{"GroupIds":["1"],"Url":"' + url + '"}'
        req.from_json_string(params)
        resp = client.SearchFaces(req)
        return resp
    except TencentCloudSDKException as err:
        return err
