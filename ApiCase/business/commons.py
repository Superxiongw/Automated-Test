# -*- coding: utf-8 -*-
import requests,pytest
from ApiCase.common.logger import logger
from ApiCase.common.httpclient import HttpClient
from ApiCase.common.yaml_util import YamlUtil



# 获取Token----------------公共方法
@pytest.fixture(scope="session",autouse=True)
def get_token():
    Token = YamlUtil().read_extract_yaml('Token')
    return Token
# 创建委托协议
def CreateAgreement(udata,herders):
    url= udata['url']
    data = udata['data']
    # 关闭https校验请求
    requests.packages.urllib3.disable_warnings()
    res = HttpClient().send_request(url=url, param_type=udata['parmams_type'], method=udata['method'], data=data,
                                        headers=herders, verify=False)
    logger.debug(f'新增委托协议信息：{res}')
    return res

