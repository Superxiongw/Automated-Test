# -*- coding: utf-8 -*-
import json
import allure
import pytest,requests
from ApiCase.common.yaml_util import YamlUtil
from ApiCase.common.httpclient import HttpClient
from ApiCase.common.loadyaml import read_yaml

@allure.epic("MAH接口测试")
@allure.feature("基础数据管理模块")
class TestCase:
    Token = YamlUtil().read_extract_yaml('Token')
    # print(Token)
    @pytest.mark.run(order=1)
    @allure.story("获取物料生产商信息列表")
    @allure.title("查询物料生产商信息")
    @pytest.mark.parametrize('udata',read_yaml('/Base_GetFactory.yaml'))
    def test_GetFactory(self,udata):
        # Token = YamlUtil().read_extract_yaml('Token')
        # print(Token)
        url = udata['url']
        hearder = {'authorization': TestCase.Token}
        data = udata['data']
        # 关闭https校验请求
        requests.packages.urllib3.disable_warnings()
        res = HttpClient().send_request(method=udata['method'],url=url,param_type=udata['parmams_type'],data=data,
                                        headers=hearder,verify=False)
        print(res.json())

    @allure.story("新增物料生产商信息")
    @allure.title("创建物料生产商信息")
    @allure.description("校验创建物料生产商是否正常")
    @allure.severity("critical")
    @pytest.mark.skip(reason="跳过新增")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('udata',read_yaml('/Base_CreateFactory.yaml'))
    def test_CreateFactory(self,udata):
        # Token = YamlUtil().read_extract_yaml('Token')
        # print(Token)
        url=udata['url']
        hearder = {'authorization': TestCase.Token}
        data=udata['data']
        # 关闭https校验请求
        requests.packages.urllib3.disable_warnings()
        res = HttpClient().send_request(method=udata['method'],url=url,param_type=udata['parmams_type'],data=data,
                                        headers=hearder,verify=False)
        print('-----------------------新增物料生产商信息-----------------------')
        print(res.json())

    @allure.story("编辑物料生产商信息")
    @allure.title("编辑物料生产商信息")
    @pytest.mark.skip(reason="跳过编辑")
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('udata',read_yaml('/Base_ModifyFactory.yaml'))
    def test_ModifyFactory(self,udata):
        url = udata['url']
        hearder = {'authorization': TestCase.Token}
        data = udata['data']
        # 关闭https校验请求
        requests.packages.urllib3.disable_warnings()
        res = HttpClient().send_request(method=udata['method'], url=url, param_type=udata['parmams_type'], data=data,
                                        headers=hearder, verify=False)
        print('-----------------------编辑物料生产商信息-----------------------')
        print(res.json())

    @allure.story("审核物料生产商信息")
    @pytest.mark.skip(reason="跳过提交审核")
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('udata', read_yaml('/Base_ApplyFactory.yaml'))
    def test_ApplyFactory(self,udata):
        url = udata['url']
        hearder = {'authorization': TestCase.Token}
        data = udata['data']
        res = HttpClient().send_request(method=udata['method'],url=url,headers=hearder,data=data,
                                        param_type=udata['parmams_type'],verify=False)
        print('-----------------------提交审批物料生产商信息-----------------------')
        print(res.json())
    @allure.story("审核物料生产商信息")
    @pytest.mark.skip(reason="跳过审核")
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('udata',read_yaml('/Base_RatifyFactory.yaml'))
    def test_RatifyFactory(self,udata):
        url = udata['url']
        hearder = {'authorization': TestCase.Token}
        data = udata['data']
        # 关闭https校验请求
        requests.packages.urllib3.disable_warnings()
        res = HttpClient().send_request(method=udata['method'],url=url,param_type=udata['parmams_type'],data=data,
                                        headers=hearder,verify=False)
        print('-----------------------审核物料生产商信息-----------------------')
        print(res.json())
