# -*- coding: utf-8 -*-
import logging
import os.path
import traceback
import yaml,sys
# yaml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"yaml_file/data.yaml")
# yaml_path = 'E:\Program Files\Sendi_Project\ApiCase\yaml_file\user_login.yaml.yaml'
def read_yaml(yaml_path):
    with open('E:/Program Files/Sendi_Project/ApiCase/yaml_file' + yaml_path,'r', encoding='gbk') as f:
        data=yaml.load(stream=f,Loader=yaml.FullLoader)
        return data
        # print(data)
