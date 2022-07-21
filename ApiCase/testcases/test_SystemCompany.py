# -*- coding: utf-8 -*-
import pytest,requests,allure

from ApiCase.common.httpclient import HttpClient
from ApiCase.common.loadyaml import read_yaml, read_includeyaml
from ApiCase.common.yaml_util import YamlUtil
from ApiCase.common.logger import logger
import ApiCase.business.commons as common

path = 'E:\Program Files\Sendi_Project\ApiCase\yaml_file\System_Company'


class TestCase:
    Token = YamlUtil().read_extract_yaml('Token')
    Token1 = YamlUtil().read_extract_yaml('Token1')

    @pytest.mark.run(order=10)
    @pytest.mark.skip(reason="跳过")
    @pytest.mark.parametrize('udata',read_includeyaml(path+'\Company_GetAgreementList.yaml','../System_Company'))
    def test_GetAgreementList(self,udata):
        url = udata['url']
        herders = {"authorization": common.get_token()}
        data = udata['data']
        # 关闭https校验请求
        requests.packages.urllib3.disable_warnings()
        res = HttpClient().send_request(url=url,param_type=udata['parmams_type'],method=udata['method'],data=data,
                                  headers=herders,verify=False)

        logger.debug(f'获取委托协议列表：{res}')
        print('-----------------------获取委托协议列表-----------------------')
        print(res.json())
        assert res.status_code == 200
        assert res.json()['Code'] == 100
        assert res.json()['Body']['AgreementList'] != None
        # print(udata)
    # 创建委托协议
    @pytest.mark.run(order=1)
    @pytest.mark.skip(reason="跳过新增委托协议")
    @pytest.mark.parametrize('udata', read_yaml('/System_Company/Company_CreateAgreement.yaml'))
    def test_CreateAgreement(self,udata):
        herders = {"authorization": TestCase.Token}
        res = common.CreateAgreement(udata,herders)
        print(res.json())
        assert res.json()['Msg'] == "成功"

    # 确认委托协议
    @pytest.mark.run(order=3)
    # @pytest.mark.skip(reason="跳过确认委托协议")
    @pytest.mark.parametrize('udata', read_yaml('/System_Company/Company_ConfirmAgreement.yaml'))
    def test_ConfirmAgreement(self,udata):
        url = udata['url']
        herders = {"authorization": TestCase.Token1}
        data = udata['data']
        # 关闭https校验请求
        requests.packages.urllib3.disable_warnings()
        res = HttpClient().send_request(url=url, param_type=udata['parmams_type'], method=udata['method'], data=data,
                                        headers=herders, verify=False)
        logger.debug(f'确认委托协议信息：{res}')
        print('-----------------------确认委托协议信息-----------------------')
        print(res.json())
        # assert res.status_code == 200
        assert res.json()["Code"] == 100
        res1 = TestCase().test_GetAgreementList(udata)
        print(res1.json())

    # 修改委托协议
    def test_ModifyAgreement(self):
        pass


    # 终止委托协议
    def test_StopAgreement(self):
        pass

    # 补充委托协议
    def test_RepairAgreement(self):
        pass