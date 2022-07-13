# -*- coding: utf-8 -*-
import pytest,os

if __name__ == '__main__':
    # pytest.main(['ApiCase/testcases/test_Login.py','-sv','-q','--alluredir','./result'])
    # pytest.main(['ApiCase/testcases/test_CreateFactory.py','-sv','-q','--alluredir','./result'])
    pytest.main(['ApiCase/testcases/test_BaseMaterial.py','-sv','-q','--alluredir','./result'])
    os.system('allure generate ./result -o ./ApiCase/report --clean')
    # CreateFactory.py