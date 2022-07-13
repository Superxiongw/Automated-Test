# -*- coding: utf-8 -*-
import pytest,allure

from ApiCase.common.httpclient import HttpClient
from ApiCase.common.loadyaml import read_yaml
from ApiCase.common.yaml_util import YamlUtil

@allure.feature('Mah系统-物料信息管理模块')
class TestCase:
    Token = YamlUtil().read_extract_yaml('Token')
    @pytest.mark.parametrize('udata',read_yaml('/Base_GetMaterialList.yaml'))
    def test_GetMaterialList(self,udata):
        url = udata['url']
        headers = {'authorization': TestCase.Token}
        data = udata['data']
        res = HttpClient().send_request(url=url,method=udata['method'],param_type=udata['parmams_type'],data=data,
                                        headers=headers,verify=False)
        print('-----------------------获取物料信息-----------------------')
        print(res.json())