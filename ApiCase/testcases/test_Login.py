# -*- coding: utf-8 -*-
import requests,pytest
from ApiCase.common.yaml_util import YamlUtil
from ApiCase.common.httpclient import HttpClient
from ApiCase.common.loadyaml import read_yaml

class TestCase:
    # 全局变量 类变量 公共变量 都可以使用
    token=None
    httpclient=None
    @classmethod
    def setup_class(cls):
        TestCase.httpclient = HttpClient()
        # config=configparser.ConfigParser()
        # config.read('env.ini',encoding='utf-8')
        # TestCase.url=config.get('apidemo01','URL')
    @classmethod
    def teardown_class(cls):
        pass


    # 登录MAH系统
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('udata',read_yaml('/user_login.yaml'))
    def test_Login(self,udata):
        url = udata['url']
        data = udata['data']
        # 关闭https校验请求
        requests.packages.urllib3.disable_warnings()
        res = TestCase.httpclient.send_request(method=udata['method'],url=url,param_type=udata['parmams_type'],data=data,verify=False)
        print('-----------------------获取登录后返回值-----------------------')
        print(res.json())
        # TestCase.token = res.json()['Body']['Token']
        # TestCase.UserId = res.json()['Body']['UserId']
        # TestCase.CompanyId = res.json()['Body']['CompanyId']
        # print('-----------------------获取Token-----------------------')
        # print('登录用户Token：',TestCase.token)
        # print('登录用户UserId：',TestCase.UserId)
        # print('登录用户CompanyId：',TestCase.CompanyId)
        YamlUtil().write_extract_yaml({'Token':res.json()['Body']['Token']})
        YamlUtil().write_extract_yaml({'UserId': res.json()['Body']['UserId']})
        YamlUtil().write_extract_yaml({'CompanyId': res.json()['Body']['CompanyId']})

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('udata',read_yaml('/user_info.yaml'))
    def test_userinfo(self,udata):
        Token = YamlUtil().read_extract_yaml('Token')
        UserId = YamlUtil().read_extract_yaml('UserId')
        CompanyId = YamlUtil().read_extract_yaml('CompanyId')
        # print('-----------------------人员列表获取Token-----------------------')
        # print('提取Token值为：',Token)
        # print('提取UserId值为：',UserId)
        # print('提取CompanyId值为：',CompanyId)
        # 人员列表接口
        url = udata['url']
        hearder = {'authorization': Token}
        data = {
                "CompanyId": "", # 企业id
                "PageIndex": 0,
                "PageSize": 10,
                "SearchKey": "",
                "Identity": 0,# 企业身份(0=管理员，1=持有人，2=受托方，3=双重身份)
                "LoginUserId": UserId,# 登录用户id
                "LoginCompanyId": CompanyId # 企业用户id
        }
        res = TestCase.httpclient.send_request(method='post', url=url, param_type='json',data=data,headers=hearder)
        print('-----------------------获取人员信息列表-----------------------')
        print(res.json())

if __name__ == '__main__':
    pytest.main(['test_Login.py','-sv'])