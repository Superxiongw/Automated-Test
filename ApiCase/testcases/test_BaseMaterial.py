# -*- coding: utf-8 -*-
import pytest,allure,requests

from ApiCase.common.httpclient import HttpClient
from ApiCase.common.loadyaml import read_yaml
from ApiCase.common.yaml_util import YamlUtil
from ApiCase.common.logger import logger

@allure.feature('Mah系统-物料信息管理模块')
class TestCase:
    Token = YamlUtil().read_extract_yaml('Token')
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('udata',read_yaml('/Base_Material/Base_GetMaterialList.yaml'))
    def test_GetMaterialList(self,udata):
        url = udata['url']
        headers = {'authorization': TestCase.Token}
        data = udata['data']
        # 关闭https校验请求
        requests.packages.urllib3.disable_warnings()
        res = HttpClient().send_request(url=url,method=udata['method'],param_type=udata['parmams_type'],data=data,
                                        headers=headers,verify=False)
        print('-----------------------获取物料信息-----------------------')
        logger.debug(f'获取物料信息:{res}')
        print(res.json())
        # assert res.status_code == 200

    @pytest.mark.skip(reason="跳过创建原辅料")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("udata",read_yaml("/Base_Material/Base_CreateMaterial.yaml"))
    def test_CreateMaterial(self, udata):
        url = udata['url']
        headers = {'authorization': TestCase.Token}
        data = udata['data']
        # 关闭https校验请求
        requests.packages.urllib3.disable_warnings()
        res = HttpClient().send_request(url=url, method=udata['method'],param_type=udata['parmams_type'] ,data=data,
                                        headers=headers,verify=False)
        print('-----------------------创建物料信息-----------------------')
        print(res.json())

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("udata",read_yaml("/Base_Material/Base_ModifyMaterial.yaml"))
    def test_ModifyMaterial(self, udata):
        url = udata['url']
        headers = {'authorization': TestCase.Token}
        data = udata['data']
        # 关闭https校验请求
        requests.packages.urllib3.disable_warnings()
        res = HttpClient().send_request(url=url, method=udata['method'],param_type=udata['parmams_type'] ,data=data,
                                        headers=headers,verify=False)
        print('-----------------------修改物料信息-----------------------')
        logger.debug(f'修改物料信息:{res}')
        print(res.json())