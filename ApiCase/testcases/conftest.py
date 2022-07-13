# -*- coding: utf-8 -*-
import pytest

from ApiCase.common.yaml_util import YamlUtil


@pytest.fixture(scope="function")
def conn_database():
    print("连接数据库")
    yield
    print("关闭数据库")

# @pytest.fixture(scope="session",autouse=True)
# def clear_yaml():
#     YamlUtil().clear_extract_yaml()